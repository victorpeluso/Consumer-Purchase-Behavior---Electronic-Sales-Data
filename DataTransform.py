import pandas as pd

# Loading the cleaned dataset
df = pd.read_csv('C:/Users/alexp/PycharmProjects/ConsumerBehavior/data/Cleaned_Electronic_Sales.csv')

# Categorical variable for age groups
df['Age Group'] = pd.cut(df['Age'], bins=[18, 26, 36, 46, 56, 65, float('inf')],
                         labels=['18-25', '26-35', '36-45', '46-55', '56-65', '66+'],
                         right=False)

# Determine loyalty status
df['Loyalty Status'] = df['Loyalty Member'].apply(lambda x: 'Active' if x == 'Yes' else 'Inactive')