class BankAccount:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print("Amount withdrawn successfully.")

    def display(self):
        print("\nAccount Number:", self.acc_no)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


accounts = {}

while True:
    print("\n--- BANK MENU ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Display Account")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        acc_no = input("Enter account number: ")
        name = input("Enter account holder name: ")
        balance = int(input("Enter initial balance: "))
        accounts[acc_no] = BankAccount(acc_no, name, balance)
        print("Account created successfully.")

    elif choice == "2":
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            amount = int(input("Enter deposit amount: "))
            accounts[acc_no].deposit(amount)
        else:
            print("Account not found.")

    elif choice == "3":
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            amount = int(input("Enter withdrawal amount: "))
            accounts[acc_no].withdraw(amount)
        else:
            print("Account not found.")

    elif choice == "4":
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            accounts[acc_no].display()
        else:
            print("Account not found.")

    elif choice == "5":
        print("Thank you for using the bank system.")
        break

    else:
        print("Invalid choice. Try again.")
bank.py
