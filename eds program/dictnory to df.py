import pandas as pd
# Modifying a row
modify_index = int(input("Index of row to modify: "))
new_age_value = int(input("New age: "))
df.loc[modify_index, 'Age'] = new_age_value
# Display the DataFrame after modifying a row

print("After modifying a row:")
print(df)

# Deleting a row
delete_index = int(input("Index of row to delete: "))

df = df.drop(delete_index).reset_index(drop=True)

# Display the DataFrame after deleting a row
print("After deleting a row:")
print(df)

# Adding a new column
genders = input("Enter genders separated by space: ").split()

df['Gender'] = genders

# Display the DataFrame after adding a new column
print("After adding a new column:")
print(df)

# Modifying a column
df["Name"] = df["Name"].str.upper()

# Display the DataFrame after modifying a column
print("After modifying a column:")
print(df)

# Deleting a column
df = df.drop("Age", axis=1)

# Display the DataFrame after deleting a column
print("After deleting a column:")
print(df)
