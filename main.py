class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self._account_balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self._account_balance}")
        elif amount > self._account_balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def display_balance(self):
        print(f"Account Holder: {self._account_holder_name}")
        print(f"Account Number: {self._account_number}")
        print(f"Account Balance: ${self._account_balance}")


# Create an instance of the BankAccount class
account1 = BankAccount("12345", "alagiri veeramani", 1000.0)

# Test deposit and withdrawal functionality
account1.display_balance()  # Display initial balance
account1.deposit(500.0)     # Deposit $500
account1.withdraw(200.0)    # Withdraw $200
account1.withdraw(1500.0)   # Attempt to withdraw more than the balance
account1.deposit(-100.0)    # Attempt to deposit a negative amount
account1.display_balance()  # Display updated balance

