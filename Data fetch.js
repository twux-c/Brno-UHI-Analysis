// 1. Define Brno boundary
var brno = ee.FeatureCollection("FAO/GAUL/2015/level2")
  .filter(ee.Filter.eq('ADM2_NAME', 'Brno-mesto'))
  .geometry();

// 2. Harmonization and Time-Band Functions


function processL5(image) {
  var qa = image.select('QA_PIXEL');
  var mask = qa.bitwiseAnd(1 << 4).eq(0).and(qa.bitwiseAnd(1 << 3).eq(0));
  var lst = image.select('ST_B6').multiply(0.00341802).add(149.0).subtract(273.15).rename('LST_C');
  var year = ee.Image(image.date().get('year')).float().rename('year');
  return ee.Image.cat(year, lst).updateMask(mask).clip(brno);
}

function processL8(image) {
  var qa = image.select('QA_PIXEL');
  var mask = qa.bitwiseAnd(1 << 4).eq(0).and(qa.bitwiseAnd(1 << 3).eq(0));
  var lst = image.select('ST_B10').multiply(0.00341802).add(149.0).subtract(273.15).rename('LST_C');
  var year = ee.Image(image.date().get('year')).float().rename('year');
  return ee.Image.cat(year, lst).updateMask(mask).clip(brno);
}

// 3. Process Both Archives (Summer months only)
var l5_summer = ee.ImageCollection("LANDSAT/LT05/C02/T1_L2")
  .filterBounds(brno).filter(ee.Filter.calendarRange(6, 8, 'month'))
  .filterDate('2001-01-01', '2011-12-31').map(processL5);

var l8_summer = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2")
  .filterBounds(brno).filter(ee.Filter.calendarRange(6, 8, 'month'))
  .filterDate('2013-01-01', '2025-12-31').map(processL8);

var combinedCollection = l5_summer.merge(l8_summer);

// 4. Calculate the Linear Trend (Slope) per pixel
// This mathematically proves which exact streets/zones are heating up the fastest
var trend = combinedCollection.select(['year', 'LST_C'])
  .reduce(ee.Reducer.linearFit());

// 5. Map Visualization
// A slope of 0.15 means the pixel is warming by 0.15°C per year
var trendVis = {
  min: -0.05, // Cooling trend (Blue)
  max: 0.15,  // Warming trend (Red)
  palette: ['#2c7bb6', '#ffffbf', '#d7191c'] 
};

// Center the map on Brno and add the trend layer with 75% opacity 

Map.centerObject(brno, 12);
Map.addLayer(trend.select('scale'), trendVis, '25-Year Warming Trend (°C/year)', 0.75);

// Draw a clean black outline of the city for professional context
var empty = ee.Image().byte();
var outline = empty.paint({
  featureCollection: ee.FeatureCollection("FAO/GAUL/2015/level2").filter(ee.Filter.eq('ADM2_NAME', 'Brno-mesto')),
  color: 1,
  width: 2
});
Map.addLayer(outline, {palette: 'black'}, 'Brno Boundary');
