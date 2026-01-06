import csv
from datetime import datetime

FILE_PATH = "data/expenses.csv"

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Rent, Travel, etc.): ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    try:
        amount = float(amount)
    except ValueError:
        print("Amount must be a number!")
        return

    with open(FILE_PATH, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("Expense added successfully!")
