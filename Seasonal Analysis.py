import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"C:\Users\hp\Downloads\weather - weather.csv"
df = pd.read_csv(file_path)

# Assuming 'Sunshine' is a categorical variable representing seasons
seasonal_means = df.groupby('Sunshine').mean()

plt.figure(figsize=(12, 6))
sns.barplot(x=seasonal_means.index, y=seasonal_means['MinTemp'], label='MinTemp', color='red')
sns.barplot(x=seasonal_means.index, y=seasonal_means['MaxTemp'], label='MaxTemp', color='blue')
sns.barplot(x=seasonal_means.index, y=seasonal_means['Rainfall'], label='Rainfall', color='green')
sns.barplot(x=seasonal_means.index, y=seasonal_means['Evaporation'], label='Evaporation', color='yellow')

plt.title('Average Values of Weather Variables Across Seasons')
plt.xlabel('Sunshine')
plt.ylabel('Average Value')
plt.legend()
plt.show()
