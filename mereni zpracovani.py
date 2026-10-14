import pandas as pd
import matplotlib.pyplot as plt

nazev_souboru = 'finance.csv'
data = pd.read_csv(nazev_souboru)
# 1. Převod na formát data (pokud jsi to ještě neudělal, je to nutné pro správné řazení)
data['Date'] = pd.to_datetime(data['Date'],format = 'mixed' )

# 2. SEŘAZENÍ: Seřadíme tabulku od nejstaršího data po nejnovější
data = data.sort_values(by='Date')

data.dropna()
print(data.info())
print(data.head())

# 1. Odstraníme čárky z řetězců a převedeme je na čísla (float)
data['Close'] = data['Close'].str.replace(',', '').astype(float)

plt.figure(figsize=(6, 4))
plt.plot(data['Date'], data['Close'], color='red')
plt.show()