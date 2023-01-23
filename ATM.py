class ATM:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def account_detail(self):
        print("----------ACCOUNT DETAIL----------")
        print(f"Account Holder: {self.name.upper()}")
        print(f"Account Number: {self.account_number}")
        print(f"Available balance: Rs.{self.balance}")

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Current account balance: Rs.", self.balance)
        print()

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient fund!")
            print(f"Your balance is Rs.{self.balance} only.")
            print("Try with lesser amount than balance.")
            print()
        else:
            self.balance = self.balance - self.amount
            print(f"Rs.{amount} withdrawal successful!")
            print("Current account balance: ", self.balance)
            print()

    def check_balance(self):
        print("Available balance: Nu.", self.balance)
        print()

    def transaction(self):
        print("""Transaction:
        1.Account Detail:
        2.Check Balance:
        3.Deposit:
        4.Withdrawal:
        5.Exit:""")
        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 or 5:"))
            except:
                print("Error: Enter 1, 2, 3, 4, or 5 only!")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("How much you want to deposit(Rs.):"))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("How much you want to withdraw(Rs.):"))
                    atm.withdraw(amount)
                elif option == 5:
                    print("Transaction is now complete. Thank you for banking with us!")
                    break


print("Welcome to ACXT Bank")
name = input("Enter your name: ")
account_number = input("Enter your account number:")
print("account_number: ", account_number)
print("Congratulations! Account created successfully......")

atm = ATM(name, account_number)

while True:
    trans = input("Do you want to do any transaction?(y/n):")
    if trans == "y":
        atm.transaction()
    elif trans == "n":
        print("Thanks for visiting us!")
        break
    else:
        print("Wrong command!  Enter 'y' for yes and 'n' for NO.")
