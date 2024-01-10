import pandas as pd
import matplotlib.pyplot as plt


file_path = r"C:\Users\hp\Downloads\weather - weather.csv"

# Load the dataset
df = pd.read_csv(file_path)


selected_columns = ['MinTemp', 'MaxTemp', 'Rainfall', 'Humidity9am', 'Humidity3pm']


plt.figure(figsize=(12, 6))

for column in selected_columns:
    plt.plot(df.index, df[column], label=column, linewidth=2)

plt.title('Weather Trends and Variations')
plt.xlabel('Date')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.show()
