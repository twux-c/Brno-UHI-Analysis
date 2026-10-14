import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# 1. Professional Styling
sns.set_theme(style="ticks")
plt.figure(figsize=(9, 6))


df_corr = pd.read_csv('ndvi_lst_correlation.csv')


# 3. Plotting the correlation
ax = sns.regplot(
    x='NDVI',
    y='LST_C',
    data=df_corr,
    scatter_kws={'alpha': 0.5, 'color': '#d95f02', 's': 50, 'edgecolor': 'w'},
    line_kws={'color': '#1b9e77', 'linewidth': 3},
)

# 4. Contextual Formatting
plt.title('Mitigation Impact: Cooling Effect of Urban Vegetation', fontsize=14, weight='bold', pad=15)
plt.xlabel('Vegetation Density (NDVI)\n← Industrial/Concrete                                              Dense Parks/Forests →', fontsize=11)
plt.ylabel('Land Surface Temperature (°C)', fontsize=11)

# Add a subtle grid
plt.grid(axis='y', linestyle='--', alpha=0.7)
sns.despine() # Removes top and right borders for a cleaner look

# 5. Export high-resolution image
plt.tight_layout()
plt.savefig('vegetation_cooling_effect.png', dpi=300)
plt.show()