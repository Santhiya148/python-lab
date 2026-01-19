import pandas as pd
from functools import reduce

data = {
    'Name': ['Arun', 'Bala', 'Charan', 'Divya', 'Esha'],
    'Age': [25, 19, 35, 42, 28],
    'Income': [40000, 25000, 60000, 80000, 30000],
    'Credit_Score': [700, 620, 680, 750, 640],
    'Existing_Loan': [10000, 5000, 20000, 30000, 10000]
}

df = pd.DataFrame(data)

df['Age_Status'] = list(map(lambda x: 'Valid' if x >= 21 else 'Invalid', df['Age']))

eligible_income = list(filter(lambda x: x >= 30000, df['Income']))

total_income = reduce(lambda x, y: x + y, df['Income'])

def loan_eligibility(row):
    if (
        row['Age'] >= 21 and
        row['Income'] >= 30000 and
        row['Credit_Score'] >= 650 and
        row['Existing_Loan'] <= 0.5 * row['Income']
    ):
        return 'Eligible'
    else:
        return 'Not Eligible'

df['Loan_Status'] = df.apply(loan_eligibility, axis=1)

print(df)
print("Eligible Income:", eligible_income)
print("Total Income:", total_income)
