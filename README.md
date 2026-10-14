# Brno-UHI-Analysis
Comprehensive analysis of 25 year historical Surface temp data in the Brno region
requirements:
pandas==2.1.1
matplotlib==3.8.0
seaborn==0.13.0
numpy==1.26.0
# Brno Urban Heat Island (UHI) Analysis (2001–2025)


## Methodology
- **Data Source:** USGS Landsat 5, 8, Collection 2, Level-2 Science Products (Surface Temperature).
- **Temporal Scope:** Meteorological summer months (June–August) from 2001 to 2025.
- **Processing Pipeline:** Google Earth Engine (GEE) was utilized for server-side processing
- **Quality Assurance:** Bitwise operations on the `QA_PIXEL` band were applied to mask clouds and shadows
- **Sensor Harmonization:** Thermal bands across missions (`ST_B6` and `ST_B10`) were standardized

## Tech Stack
* **Geospatial Processing:** Google Earth Engine API, JavaScript
* **Data Visualization:** Python (Pandas, Matplotlib, Seaborn)
