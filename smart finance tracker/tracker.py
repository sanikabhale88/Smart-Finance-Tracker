import pandas as pd
import matplotlib.pyplot as plt

class SmartFinanceTracker:
    def __init__(self):
        # Initialize an empty DataFrame to store expenses
        self.df = pd.DataFrame(columns=['Date', 'Description', 'Category', 'Amount'])

    def add_expense(self, date, description, category, amount):
        # Adding a new expense
        new_expense = {'Date': date, 'Description': description, 'Category': category, 'Amount': amount}
        self.df = pd.concat([self.df, pd.DataFrame([new_expense])], ignore_index=True)
        print("Expense added successfully.")

    def edit_expense(self, index, date=None, description=None, category=None, amount=None):
        # Editing an existing expense by index
        if 0 <= index < len(self.df):
            if date:
                self.df.at[index, 'Date'] = date
            if description:
                self.df.at[index, 'Description'] = description
            if category:
                self.df.at[index, 'Category'] = category
            if amount:
                self.df.at[index, 'Amount'] = amount
            print("Expense updated successfully.")
        else:
            print("Invalid index.")

    def delete_expense(self, index):
        # Deleting an expense by index
        if 0 <= index < len(self.df):
            self.df = self.df.drop(index).reset_index(drop=True)
            print("Expense deleted successfully.")
        else:
            print("Invalid index.")

    def view_expenses(self):
        # Viewing all expenses
        if self.df.empty:
            print("No expenses found.")
        else:
            print(self.df)

    def visualize_expenses(self):
        # Visualizing expenses by category
        if self.df.empty:
            print("No expenses to visualize.")
        else:
            category_totals = self.df.groupby('Category')['Amount'].sum()
            category_totals.plot(kind='bar', color='skyblue')
            plt.title('Expenses by Category')
            plt.xlabel('Category')
            plt.ylabel('Total Amount')
            plt.show()

    def monthly_summary(self, month):
        # Summarize expenses for a specific month
        if self.df.empty:
            print("No expenses to summarize.")
        else:
            self.df['Date'] = pd.to_datetime(self.df['Date'])
            monthly_expenses = self.df[self.df['Date'].dt.month == month]
            if monthly_expenses.empty:
                print("No expenses found for the specified month.")
            else:
                print(monthly_expenses)
                total = monthly_expenses['Amount'].sum()
                print(f"Total expenses for month {month}: {total}")

    def set_saving_goal(self, goal_amount):
        # Set and track a savings goal
        total_expenses = self.df['Amount'].sum()
        print(f"Total expenses so far: {total_expenses}")
        remaining = goal_amount - total_expenses
        if remaining > 0:
            print(f"You need to save {remaining} more to reach your goal of {goal_amount}.")
        else:
            print(f"Congratulations! You've reached your savings goal of {goal_amount}.")

    def export_to_csv(self, filename):
        # Export the expenses to a CSV file
        if self.df.empty:
            print("No expenses to export.")
        else:
            self.df.to_csv(filename, index=False)
            print(f"Expenses exported to {filename}")

def main():
    tracker = SmartFinanceTracker()

    while True:
        print("\nSmart Finance Tracker Menu:")
        print("1. Add Expense")
        print("2. Edit Expense")
        print("3. Delete Expense")
        print("4. View Expenses")
        print("5. Visualize Expenses")
        print("6. Monthly Summary")
        print("7. Set Saving Goal")
        print("8. Export to CSV")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        if choice == '1':
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter the description: ")
            category = input("Enter the category: ")
            amount = float(input("Enter the amount: "))
            tracker.add_expense(date, description, category, amount)
        elif choice == '2':
            index = int(input("Enter the expense index to edit: "))
            date = input("Enter the new date (YYYY-MM-DD) or press Enter to skip: ")
            description = input("Enter the new description or press Enter to skip: ")
            category = input("Enter the new category or press Enter to skip: ")
            amount = input("Enter the new amount or press Enter to skip: ")
            tracker.edit_expense(index, date or None, description or None, category or None, float(amount) if amount else None)
        elif choice == '3':
            index = int(input("Enter the expense index to delete: "))
            tracker.delete_expense(index)
        elif choice == '4':
            tracker.view_expenses()
        elif choice == '5':
            tracker.visualize_expenses()
        elif choice == '6':
            month = int(input("Enter the month (1-12) to summarize: "))
            tracker.monthly_summary(month)
        elif choice == '7':
            goal_amount = float(input("Enter your savings goal amount: "))
            tracker.set_saving_goal(goal_amount)
        elif choice == '8':
            filename = input("Enter the filename (e.g., expenses.csv): ")
            tracker.export_to_csv(filename)
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
