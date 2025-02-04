import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the processed DataFrame
df = pd.read_csv('processed_data.csv')

# Select the last 10 records
last_10 = df.tail(10)

# Pie Chart: Distribution of Departments
plt.figure(figsize=(8, 6))
last_10['Department'].value_counts().plot.pie(autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
plt.title('Department Distribution (Last 10 Records)')
plt.ylabel('')
plt.show()

# Bar Chart: Salary by Experience
plt.figure(figsize=(10, 6))
sns.barplot(x='Experience', y='Salary', data=last_10, palette='viridis')
plt.title('Salary by Experience (Last 10 Records)')
plt.xlabel('Experience (Years)')
plt.ylabel('Salary')
plt.show()

# Scatter Plot: Age vs. Salary
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Age', y='Salary', hue='Gender', data=last_10, palette='deep')
plt.title('Age vs. Salary (Last 10 Records)')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.legend(title='Gender')
plt.show()

# Line Chart: Salary Trend over Age
plt.figure(figsize=(10, 6))
sns.lineplot(x='Age', y='Salary', data=last_10, marker='o', color='b')
plt.title('Salary Trend over Age (Last 10 Records)')
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()

# Histogram: Age Distribution
plt.figure(figsize=(8, 6))
sns.histplot(last_10['Age'], bins=5, kde=True, color='purple')
plt.title('Age Distribution (Last 10 Records)')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()