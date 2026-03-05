import pandas as pd
from datetime import datetime

# user inputs
amount = float(input("Enter amount: "))
category = input("Enter category: ")

date = datetime.today().strftime('%Y-%m-%d')

new_expense = pd.DataFrame([[date, amount, category]],
                           columns=["date","amount","category"])

# load existing file
file_path = "data/expense_log.csv"

df = pd.read_csv(file_path)

# append new expense
df = pd.concat([df, new_expense], ignore_index=True)

# save file
df.to_csv(file_path, index=False)

print("Expense saved successfully!")
