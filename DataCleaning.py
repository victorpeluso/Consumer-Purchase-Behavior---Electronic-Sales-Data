from xml.sax.handler import property_interning_dict

import pandas as pd

df = pd.read_csv("C:/Users/alexp/PycharmProjects/ConsumerBehavior/data/Electronic_sales_Sep2023-Sep2024.csv")

# View the first few rows
print(df.head())

# DataFrame Summary
print(df.info())

# Basic statistics and potential outliers
print(df.describe())

# Check for missing values
print(df.isnull().sum())


# Lets remove the singular row where 'gender' is missing
df = df[df['Gender'].notna()]

# Now lets replace the missing values in 'Add-ons Purchased; with None
df['Add-ons Purchased'] = df['Add-ons Purchased'].fillna("None")

# Saving the cleaned dataset
df.to_csv("C:/Users/alexp/PycharmProjects/ConsumerBehavior/data/Cleaned_Electronic_Sales.csv", index=False)