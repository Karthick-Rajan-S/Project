import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"C:\Users\hp\Downloads\weather - weather.csv"

df = pd.read_csv(file_path)

rainfall_column = df['Rainfall']

plt.figure(figsize=(10, 6))
sns.histplot(rainfall_column, kde=True, bins=30, color='red')
plt.title('Distribution of Rainfall')
plt.xlabel('Rainfall')
plt.ylabel('Frequency')
plt.show()
