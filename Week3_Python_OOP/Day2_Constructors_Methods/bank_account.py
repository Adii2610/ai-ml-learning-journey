class BankAccount:
    # Constructor method
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance
        print(f"Account created for {self.account_holder} with balance {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# Example usage
if __name__ == "__main__":
    account = BankAccount("Aditya", 1000)
    account.deposit(500)
    account.withdraw(200)
