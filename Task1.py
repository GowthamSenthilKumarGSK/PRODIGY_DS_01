import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('cancer patient data sets.csv')

# Display the first few rows of the dataset
print(data.head())

# Distribution of Age
plt.figure(figsize=(12, 6))
sns.histplot(data['Age'], bins=10, kde=True, color='blue')
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Distribution of Gender
plt.figure(figsize=(8, 6))
sns.countplot(x='Gender', data=data, palette='pastel')
plt.title('Distribution of Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.grid(True)
plt.show()

# Distribution of Age by Gender
plt.figure(figsize=(12, 6))
sns.histplot(data, x='Age', hue='Gender', multiple='stack', palette='pastel', bins=10, kde=True)
plt.title('Distribution of Age by Gender')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
