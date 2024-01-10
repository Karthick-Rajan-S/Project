import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"C:\Users\hp\Downloads\weather - weather.csv"

df = pd.read_csv(file_path)

selected_columns = ['MinTemp', 'MaxTemp', 'Rainfall', 'Evaporation']

subset_df = df[selected_columns]

correlation_matrix = subset_df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()
