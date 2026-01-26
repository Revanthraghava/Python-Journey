def expense_analyzer():
    expense = []
    while True:
        element = input("Enter your expenses here(or done): ")
        if element =="done":
            break
        expense.append(int(element))

    return expense
def expense_calculation(expense):
    total_expense = 0
    total_numexpense = len(expense)
    highest_expense = expense[0]
    lowest_expense = expense[0]
    for i in expense:
        if i > highest_expense:
            highest_expense = i
    
        if i < lowest_expense:
            lowest_expense = i
        total_expense += i
    average_expense = total_expense/total_numexpense

    return total_numexpense,highest_expense,lowest_expense,average_expense
expense = expense_analyzer()


if expense:
    total_numexpense,highest_expense,lowest_expense,average_expense = expense_calculation(expense)
    print(f"""This is Expense Analyzer.Expenses given by user were {expense}.
          Total number of expenses given were {total_numexpense}.
          Highest expense was {highest_expense}.Lowest expense was{lowest_expense}.
          Average expense is {average_expense}.""")
    
else:
    print("NO EXPENSES WERE GIVEN.")
