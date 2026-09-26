# Expense Tracker Project

# List of expenses in form of dictionary
expensesList = []

print("Welcome to Expense Tracker:")

while True:
    print("\n=== Menu ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # 1. ADD EXPENSE
    if choice == "1":
        date = input("Enter date: ")
        category = input("Enter category: ")
        description = input("Give detail: ")
        amount = float(input("Enter amount: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)

        print("\nDONE.. Expense is added successfully!")

    # 2. VIEW ALL EXPENSES
    elif choice == "2":
        if len(expensesList) == 0:
            print("No Expenses Added..")
        else:
            print("=== Your Expenses ===")

            count = 1

            for eachexpenses in expensesList:
                print(
                    f"Expense Number {count} -> "
                    f"{eachexpenses['date']}, "
                    f"{eachexpenses['category']}, "
                    f"{eachexpenses['description']}, "
                    f"{eachexpenses['amount']}"
                )

                count = count + 1

    # 3. VIEW TOTAL SPENDING
    elif choice == "3":
        total = 0

        for eachkrcha in expensesList:
            total = total + eachkrcha["amount"]

        print("\nTOTAL EXPENSES =", total)

    # 4. EXIT
    elif choice == "4":
        print("Thank You...")
        break

    else:
        print("Invalid choice... Try Again")