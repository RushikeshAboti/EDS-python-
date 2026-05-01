import pandas as pd
import matplotlib.pyplot as plt

# Load the Titanic dataset from the CSV file
df = pd.read_csv('titanic.csv')

# Set up the figure for 5 subplots
fig, axes = plt.subplots(3, 2, figsize=(12, 12))

# write the code..
axes[0, 0].bar(df['Pclass'].value_counts().index, df['Pclass'].value_counts(), color=['skyblue'])
axes[0, 0].set_title("Passenger Class Distribution")
axes[0, 0].set_xlabel("Pclass")
axes[0, 0].set_ylabel("Count")

#Plot 2: Gender distribution

axes[0, 1].pie(df['Gender'].value_counts(), labels=df[ 'Gender'].value_counts().index, autopct='%1.1f%%', colors=['lightblue', 'lightcoral'])

axes[0, 1].set_title("Gender Distribution")

#Plot 3: Age distribution

axes[1, 0].hist(df['Age'].dropna(), bins=8, color='lightgreen', edgecolor='black')

axes[1, 0].set_title("Age Distribution")

axes[1, 0].set_xlabel("Age")

axes[1, 0].set_ylabel("Frequency")

#Plot 4: Survival count

axes[1, 1].bar(df['Survived'].value_counts().index, df['Survived'].value_counts(), color=['lightblue', 'lightcoral'])

axes[1, 1].set_title("Survival Count")
plt.show()