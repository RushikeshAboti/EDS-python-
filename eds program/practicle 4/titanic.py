import pandas as pd
import numpy as np

# Load the Titanic dataset
data = pd.read_csv('Titanic-Dataset.csv')
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)
survivors_by_gender = data[data['Survived'] == 1]['Sex'].value_counts()
print(survivors_by_gender)

non_survivors_by_gender = data[data['Survived'] == 0]['Sex'].value_counts()
print(non_survivors_by_gender)

#3. Get the number of survivors by embarked location (Embarked_S)

survivors_by_embarked_s= data[data['Survived'] == 1] ['Embarked_S'].value_counts()

print(survivors_by_embarked_s)

#4. Get the number of non-survivors by embarked location (Embarked_S)

non_survivors_by_embarked_s= data[data['Survived'] == 0]['Embarked_S'].value_counts()

print(non_survivors_by_embarked_s)

#-5. Percentage of children (Age < 18) who survived

children = data [data['Age'] < 18]

children_survival_rate = children['Survived'].mean()

print(children_survival_rate)

#-6. Percentage of adults (Age >= 18) who survived

adults = data[data['Age'] >= 18]

adults_survival_rate = adults['Survived'].mean()

print(adults_survival_rate)