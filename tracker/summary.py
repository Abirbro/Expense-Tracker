import csv
from collections import defaultdict

FILE_PATH = "data/expenses.csv"

def monthly_summary():
    totals = defaultdict(float)

    try:
        with open(FILE_PATH, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                category = row[1]
                amount = float(row[2])
                totals[category] += amount

        if not totals:
            print("No expenses recorded yet.")
            return

        print("\n--- Category-wise Expense Summary ---")
        for category, total in totals.items():
            print(f"{category}: {total:.2f}")
    except FileNotFoundError:
        print("No data found. Add some expenses first!")

