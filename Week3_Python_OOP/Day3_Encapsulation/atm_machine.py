class Atm:

    def __init__(self):
        self.pin = ' '
        self.amount = 0
        self.menu()

    def menu(self):
        user_input = int(input("""
        1. Press 1 for Create pin
        2. Press 2 for Reset pin
        3. Press 3 for check balance
        4. Press 4 for withdraw amount
        5. Press anything to exit
        choose anything to
        """))

        if user_input == 1:
            self.create_pin()
        elif user_input == 2:
            self.reset_pin()
        elif user_input == 3:
            self.check_balance()
        elif user_input == 4:
            self.withdraw_amount()


    def create_pin(self):
        user_pin = int(input(f"Enter your pin: "))
        self.pin = user_pin

        user_balance = int(input(f"Enter your balance: "))
        self.amount = user_balance

        print(f'Pin created successfully')

        self.menu()
 
    def reset_pin(self):
        user_pin = int(input(f"Enter your current pin: "))
        if user_pin == self.pin:
            new_pin = int(input(f"Create your new pin: "))
            self.pin = new_pin
        else:
            print(f"Sorry Baby your pin is wrong")

        self.menu()

    def check_balance(self):
        user_pin = int(input(f"Enter your pin: "))
        if user_pin == self.pin:
            print(f'Your balance is {self.amount}')
        else:
            print(f"Chor saale nikal yaha se")

        self.menu()

    def withdraw_amount(self):
        user_pin = int(input(f"Enter your pin: "))
        if user_pin == self.pin:
            withdraw = int(input(f"Enter how much money you want to withdraw: "))
            if withdraw <= self.amount:
                self.amount = self.amount - withdraw
            else:
                print(f"bhai paise daal phle")

        self.menu()


obj = Atm()
