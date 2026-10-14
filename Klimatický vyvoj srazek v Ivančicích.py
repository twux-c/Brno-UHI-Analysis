import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


df = pd.read_csv('Brno_25_Year_LST_and_NDVI.csv').dropna()


sns.set_theme(style="white")
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plot 1: Temperature
color1 = '#e34a33'
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Average Surface Temperature (°C)', color=color1, fontsize=12, weight='bold')
sns.regplot(x='Year', y='Mean_Temp_C', data=df, ax=ax1, color=color1, scatter_kws={'alpha':0.6}, line_kws={'linewidth': 2})
ax1.tick_params(axis='y', labelcolor=color1)

# Create a second Y-axis that shares the same X-axis
ax2 = ax1.twinx()

# Plot 2: Greenery
color2 = '#2ca25f'
ax2.set_ylabel('Vegetation Density (NDVI)', color=color2, fontsize=12, weight='bold')
sns.regplot(x='Year', y='Mean_NDVI', data=df, ax=ax2, color=color2, scatter_kws={'alpha':0.6, 'marker':'s'}, line_kws={'linewidth': 2, 'linestyle':'--'})
ax2.tick_params(axis='y', labelcolor=color2)

plt.title('The Cost of Urban Sprawl:\nRising Temperatures Correlated with Vegetation Loss (2001-2025)', fontsize=14, weight='bold', pad=15)
plt.xticks(np.arange(2001, 2026, 4))
fig.tight_layout()
plt.savefig('temperature_vs_greenery.png', dpi=300)
plt.show()