import os
import csv
import time
import random
import string
#from tabulate import tabulate

used_account_numbers = set()
class Account():
    def __init__(self, owners_name,balance= 0, account_number = None) -> None:
        if account_number is None:
            self.account_number = self.generate_account_number()
        else:
            self.account_number = account_number
        self.owners_name = string.capwords(owners_name, sep = " ")
        self.balance = balance

    def __str__(self):
        return f"Account N° {self.account_number}\nOwner's name: {self.owners_name}\nBalance: {self.balance} €" 

    def __iter__(self):
        yield self.account_number
        yield self.owners_name
        yield self.balance

    def __getitem__(self, index):
        if index == 0:
            return self.account_number
        elif index == 1:
            return self.owners_name
        elif index == 2: 
            return self.balance
        
    def generate_account_number(self):
        global used_account_numbers
        while True:
            account_number = '1001' +'-'+ str(''.join(random.choice('0123456789') for i in range(9)) + '-'+ '18')
            # here we verify if the matriculation number has been already given to a Student. The given matriculation number are store in the database called 'used_matriculation_numbers'
            if account_number not in used_account_numbers:
                used_account_numbers.add(account_number)
                return account_number

    def deposit(self,amount):
        self.balance += amount
        bank.save_data()
        print(f"Transaction sucessfully performed. New balance: {self.balance} €")
        return

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            bank.save_data()
            print(f"Transaction sucessfully performed. New balance: {self.balance} €")
            return
        else:
            print("There isn't enough money in the account for this operation")
            return

class Bank():
    def __init__(self) -> None:
        self.accounts = []
        self.load_data()

    def __len__(self):
        return len(self.accounts)

    def load_data(self):
        database_path = os.path.join(os.path.dirname(__file__), "Bank_database")
        if not os.path.exists(database_path):
            os.makedirs(database_path) # a folder for the databases will be create, if it doesn't exists
            print(f"Database folder 'Bank_database' created. Here is the path: {database_path}")
            return
        
        print("Loading Accounts informations...")
        datas = os.path.join(os.path.dirname(__file__), "Bank_database", "Bank_accounts.csv")
        try:
            with open(datas, 'r', newline='', encoding='utf-8') as data:
                reader = csv.DictReader(data, delimiter=';')
                for line in reader:
                    account_number = line.get("Account number", "")
                    owners_name = line.get("Owner's name", "")
                    balance_str = line.get("Actual Balance", "0")
                    try:
                        balance = float(balance_str)
                    except ValueError:
                        print(f"Warning! Invalid Balance value '{balance_str}' for account N°{account_number}. Seting Balance to 0")
                        balance = 0.0
                    account = Account(owners_name, balance, account_number)
                    self.accounts.append(account)
                    if account_number:
                        used_account_numbers.add(account_number)
            time.sleep(1)
            print(f"Loading complete. {len(self.accounts)} Account(s) are registered in the Bank.")
        except FileNotFoundError:
            print(f"Error during loading: file not found")

    def save_data(self):
        datas = os.path.join(os.path.dirname(__file__), "Bank_database", "Bank_accounts.csv")
        headers = ["Account number", "Owner's name", "Actual Balance"]
        try:
            with open(datas, 'w', newline='', encoding= 'utf-8') as data:
                writer = csv.DictWriter(data, delimiter=';', fieldnames=headers)
                writer.writeheader()
                for account in self.accounts:
                    bank_data = {
                        "Account number": account.account_number,
                        "Owner's name": account.owners_name,
                        "Actual Balance": account.balance
                    }
                    writer.writerow(bank_data)
        except Exception as e:
            print(f"Error during Saving: {e}")

    def create_account(self):
        print("\n********** Creation of an account **********")
        name = input("Enter the name of the Owner: ")
        try:
            balance = float(input("How much money will be placed in the account: "))
        except ValueError:
            balance = 0.0
        account = Account(name, balance)
        self.accounts.append(account)
        self.save_data()
        print("Account sucessfully created")
        return account

    def view_accounts(self):
        if not self.accounts:
            print("--------- No account ---------")
            return
        else:
            self.accounts = sorted(self.accounts, key=lambda x:x[1])
            try:
                print("\n********** Available accounts **********")
                print(tabulate(self.accounts, headers = ["Account Number", "Owner's name", "Actual Balance (in Euro(€))"], tablefmt = "grid"))
            except NameError:
                print("The module 'tabulate' hasn't been imported or installed. This module permits to see all your datas in a table")
                time.sleep(2)
                print("Now accessing the datas...")
                time.sleep(3)
                print("\n********** Available accounts **********")
                for account in self.accounts:
                    print(account,"\n")

    def delete_account(self):
        if not self.accounts:
            print("--------- No account ---------")
            return
        else:
            print("\n********** Available accounts **********")
            for account in self.accounts:
                print(account,"\n")
            
            searched_account = input("Enter the account number of the account you want to delete: ")
            for account in self.accounts:
                if searched_account == account.account_number:
                    print(account)
            ans = input("Do you really want to delete this account? (yes/no): ").lower()
            if ans == 'yes':
                self.accounts.remove(account)
                self.save_data()
                print(f"Account N° {account.account_number} has been deleted.")
            elif ans == 'no':
                pass
            else:
                print("You must choose betwenn 'yes'and 'no'")

    def erase_database(self):
        rep_1 = input("Are you sure you want to erase the database? This operation is irreversible (yes/no)").lower()
        if rep_1 == 'yes':
            self.accounts.clear()
            self.save_data()
            print("The database has been erased.")
        elif rep_1 == 'no':
            pass
        else:
            print("Invalid entry.")

    def perform_transaction(self):
        if self.accounts:
            self.view_accounts()
            searched_account = input("Enter the account number of the account on which you want to perform transactions: ")
            for account in self.accounts:
                if searched_account == account.account_number:
                    print(account)
                    print("\n Available Operations")
                    print("1- Deposit money")
                    print("2- Withdraw money")
                    #print("3- Transfer money to an other account")
                    print("3- Come back to main menu")
                    choice_1 = input("Select the operation you want to perform (1-3): ")
                    if choice_1 == '1':
                        amount_1 = float(input("Enter the amount: "))
                        account.deposit(amount_1)
                    elif choice_1 == '2':
                        amount_2 = float(input("Enter the amount: "))
                        account.withdraw(amount_2)
                    elif choice_1 == '3':
                        break
                    else:
                        print("Account not found.\n")
        else:
            print("No Account to perform a transaction.")

    def main_menu(self):
        while True:
            print("\n ---------- Welcome to our Bank system🏦 ----------")
            print("Here we use euro(€). When you enter an amount of money, you don't need to specify the currency.")
            print("1. Create an account")
            print("2. View all the accounts")
            print("3. Perform transaction on an account")
            print("4. Delete an account")
            print("5. Erase The database")
            print("6. Quit")
            choice = input("Choose an option (1-6): ")
            if choice == '1':
                self.create_account()
            elif choice == '2':
                self.view_accounts()
            elif choice == '3':
                self.perform_transaction()
            elif choice == '4':
                self.delete_account()
            elif choice == '5':
                self.erase_database()
            elif choice == '6':
                print("Have a nice day")
                break

if __name__ == "__main__":
    bank = Bank()
    bank.main_menu()