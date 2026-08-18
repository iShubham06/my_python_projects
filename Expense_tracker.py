expenses = []

Menu = [
    "1. Add Expense",
    "2. View Expenses",
    "3. View Total",
    "4. Exit"
]

def add_expense(description, amount):
    expense = {
        "description": description.strip(),
        "amount": amount
    }
    expenses.append(expense)
    print("Expense added successfully!")

print(f"===== Expense Tracker =====")

while True:
    for item in Menu:
        print(item)

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        # Get and validate description
        description = input("Enter expense description: ")
        if not description.strip():
            print("Error: Description cannot be empty. Please try again.")
            continue
        
        # Get and validate amount
        try:
            amount = float(input("Enter expense amount: "))
            if amount < 0:
                print("Error: Amount cannot be negative. Please try again.")
                continue
        except ValueError:
            print("Error: Please enter a valid number for the amount. Please try again.")
            continue
        
        # If all validations pass, add the expense
        add_expense(description, amount)

    elif choice == '2':
        if not expenses:
            print("No expenses recorded.")
        else:
            print("===== Recorded Expenses =====")
            count = 1
            for expense in expenses:
                print(f"{count}. Description: {expense['description']}, Amount: ${expense['amount']:.2f}")
                count += 1

    elif choice == '3':
        total = sum(expense['amount'] for expense in expenses)
        print(f"Total expenses: ${total:.2f}")

    elif choice == '4':
        print("Exiting the Expense Tracker. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")