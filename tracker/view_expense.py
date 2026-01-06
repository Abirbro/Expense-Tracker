import csv

FILE_PATH = "data/expenses.csv"

def view_expenses():
    try:
        with open(FILE_PATH, "r") as file:
            reader = csv.reader(file)
            print("\nDate | Category | Amount | Description")
            print("-" * 40)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("No expenses found. Add some first!")
