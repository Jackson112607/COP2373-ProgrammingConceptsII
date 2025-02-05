# This program asks the user to input different types of expenses they make and how much they cost.
# The program then calculates and displays the total amount of money spent and displays the highest and lowest expenses.

from functools import reduce

# user_expenses receives input from the user and creates the list of expenses.
def user_expenses():
    expenses = []
    go = input('This program will organize your expenses. Would you like to use it? Enter \'yes\' or \'no\'. ').lower()
    while go == 'yes':
        type = input('Enter the type of expense: ')
        try:
            amount = float(input('Enter the amount of the expense: '))
            expenses.append({'Type': type, 'Amount': amount})
        except ValueError:
            print('Invalid input. Please enter a number.')
        go = input('Would you like to enter more expenses? ').lower()
        if go != 'yes':
            print('Done!')
    return expenses

# analyze_expenses and reducer takes in the expenses and organizes them into highest and lowest, as well as
# calculate the total.
def analyze_expenses(expenses):
    def reducer(accumulator, expense):
        total = accumulator["total"] + expense["Amount"]  # Access "Amount" key
        highest = accumulator["highest"]
        lowest = accumulator["lowest"]

        if highest is None or expense["Amount"] > highest["Amount"]:
            highest = expense
        if lowest is None or expense["Amount"] < lowest["Amount"]:
            lowest = expense

        return {"total": total, "highest": highest, "lowest": lowest}

    # Initialize accumulator.
    initial_value = {"total": 0, "highest": None, "lowest": None}
    analysis = reduce(reducer, expenses, initial_value)
    return analysis

# print_analysis displays the result.
def print_analysis(analysis):
    print("\nExpense Analysis:")
    print(f"Total Expenses: ${analysis['total']:.2f}")

    if analysis['highest']:
        print(f"Highest Expense: {analysis['highest']['Type']} (${analysis['highest']['Amount']:.2f})") # Access "Type" and "Amount"
    else:
        print("No highest expense recorded.")

    if analysis['lowest']:
        print(f"Lowest Expense: {analysis['lowest']['Type']} (${analysis['lowest']['Amount']:.2f})") # Access "Type" and "Amount"
    else:
        print("No lowest expense recorded.")

# main calls the other functions to run the program.
def main():
    expenses = user_expenses()
    analysis = analyze_expenses(expenses)
    print_analysis(analysis)

# Call main.
main()