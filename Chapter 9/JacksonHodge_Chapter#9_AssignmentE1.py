# This program uses object-oriented programming to store bank account information and make changes to it.

# Define class.
class BankAcct:
    # __init__ method
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # Function to adjust the interest rate.
    def adjust_interest_rate(self, new_interest_rate):
        self.interest_rate = new_interest_rate

    # Function to withdraw from account.
    def withdraw(self, withdrawal_amount):
        if withdrawal_amount <= self.amount:
            self.amount -= withdrawal_amount
        else:
            print("Insufficient funds.")

    # Function to deposit into an account.
    def deposit(self, deposit_amount):
        self.amount += deposit_amount

    # Function to get the balance of an account.
    def get_balance(self):
        return self.amount

    # Function to calculate the interest in an account.
    def calculate_interest(self, days):
        interest = self.amount * (self.interest_rate / 100) * (days / 365)
        return interest

    # __str__ method.
    def __str__(self):
        return f"Account: {self.account_number}, Name: {self.name}, Balance: ${self.amount:.2f}, Interest Rate: {self.interest_rate:.2f}%"

# Display output with a test bank account.
def test_bank_acct():
    account1 = BankAcct("Jane", "12345", 1000, 2.5)
    print(account1)

    account1.deposit(500)
    print(f"Balance after deposit: ${account1.get_balance():.2f}")

    account1.withdraw(200)
    print(f"Balance after withdrawal: ${account1.get_balance():.2f}")

    account1.adjust_interest_rate(3.0)
    print(f"Adjusted Interest Rate: {account1.interest_rate:.2f}%")

    interest = account1.calculate_interest(90)
    print(f"Interest for 90 days: ${interest:.2f}")

    print('Updated information: ', account1)

# Call the function.
test_bank_acct()
