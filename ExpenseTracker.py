#To Add Expense...
def AddExpense():
    print("\n ---Add Your Expense--- \n")
    date = input("Enter date(DD-MM-YYYY) : ")
    category = (input("Enter Expense category : "))
    amt = float(input("Enter Amount : "))

    expense = {
        "Date" : date,
        "Category" : category,
        "Amount" : amt
    }

    with open("expenses.txt", "a") as file:
        file.write(str(expense) + "\n")
     
#To Delete expense...
def DeleteExpense():
    print("\n ---Delete Your Expense--- \n")
    index = int(input("Enter expense number to delete : ")) -1

    with open("expenses.txt", "r") as file:
        expense = file.readlines()

    if (0 <= index < len(expense)):
        deleted_expense = expense.pop(index)

        with open("expenses.txt", "w") as file:
            file.writelines(expense)

        print("Deleted : ", deleted_expense.strip())
    
    else:
        print("Invalid index!")

  #To search expense...
def SearchExpense():
    import ast

    print("\n ---Search Your Expense--- \n")
    key = input("Enter Date(DD-MM-YYYY) OR Category to search: ")

    with open("expenses.txt", "r") as file:
        expenses = file.readlines()

        print("\nDate\t\tAmount\t\tCategory")
        print("-" * 40)
        found = False

        for expense in expenses:
            exp_rep = ast.literal_eval(expense)
            

            if key.lower() in expense.lower():
                
                
                print(
                f"{exp_rep["Date"]}\t"
                f"₹{exp_rep["Amount"]}\t\t"
                f"{exp_rep["Category"]}"
            )
            found = True
        if not found:
            print("Expense Not Found...")
        
#To print Monthly Spending...
def MonthlySpending():

    print("\n ---See Your Monthly Spending--- \n")
    import ast

    month = input("Enter Month(MM-YYYY) : ")
    total = 0
    with open("expenses.txt", "r") as file:
        expenses = file.readlines()

    for expense in expenses:
        expense_dict = ast.literal_eval(expense)

        if expense_dict["Date"].endswith(month):
            total += expense_dict["Amount"]

    print(f"\nTotal Spending in {month}: ₹{total}")

#To Generate reports...
def ExpenseReports():
    print("\n ---See Your Expense Reports--- \n")
    import ast

    with open("expenses.txt", "r") as file:
        expenses = file.readlines()
        
        print(f"{'Date':<15}{'Amount':<15}{'Category'}")
        print("-" * 40)

        for expense in expenses:
            exp_rep = ast.literal_eval(expense)

            print(
                f"{exp_rep['Date']:<15}"
                f"₹{exp_rep['Amount']:<14}"
                f"{exp_rep['Category']}"
            )

#Main function 
def main():
    print("\n ===EXPENSE TRACKER=== \n")
    print("\n ===Track Your Expenses=== \n")

    print(
        "1.Add Expense\n" \
        "2.Delete Expense\n" \
        "3.Search Expense\n" \
        "4.Monthly Spending\n" \
        "5.Expense Reports\n" \
        "6.Exit\n"
    )

    while True:
        choice = int(input("\nEnter Your Choice : "))

        if choice == 1:
            AddExpense()
        elif choice == 2:
            DeleteExpense()
        elif choice == 3:
            SearchExpense()
        elif choice == 4:
            MonthlySpending()
        elif choice == 5:
            ExpenseReports()
        elif choice == 6:
            print("Exiting...")
            break
        else:
            print("Invalid Choice")

main()