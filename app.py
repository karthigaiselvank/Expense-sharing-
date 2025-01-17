class Expense:
    def __init__(self, date, description, amount):
        self.date=date
        self.description=description
        self.amount=amount

class ExpenseTracker:
    
    def __init__(self):
        self.expenses=[]
    
    def add_expense(self, expense):
        self.expenses.append(expense)
    
    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed successfully.")
        else:
            print("Invalid expense index.")
    
    def view_expenses(self):
        if len(self.expenses)==0:
            print("No expenses found.")
        else:
            print("Expenses List.")
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date:{expense.date}, Description:{expense.description}, Amount: RS{expense.amount}")
    
    def total_expenses(self):
        total=sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: RS{total:.2f}")
    
    def menu(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Add Expense")
            print("2. Remove Expense")
            print("3. View Expenses")
            print("4. Total Expenses")
            print("5. Exit")
            choice=input("Enter your choice (1-5):")
            if choice=="1":
                date=input("Enter the date:")
                description=input("Enter the description: ")
                try:
                    amount = float(input("Enter the amount: "))
                    expense = Expense(date, description, amount)
                    self.add_expense(expense)
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")
               
            elif choice=="2":
                try:
                    index=int(input("Enter the expense index to remove: "))-1
                    self.remove_expense(index)
                except ValueError:
                    print("Invalid index. Please enter a numeric value.")
            elif choice=="3":
                self.view_expenses()
            elif choice=="4":
                self.total_expenses()
            elif choice=="5":
                print("GoodBye!")
                break
            else:
                print("Invalid choice. Please try again.")
def main():
    tracker = ExpenseTracker()
    tracker.menu()            

if __name__ == "__main__":
    main()
