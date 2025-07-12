import os
import sqlite3
import time
import string
from tabulate import tabulate

class Contact():
    def __init__(self, name, number):
        self.name = string.capwords(name, sep=" ")
        self.number = number
        
    def __str__(self):
        return f"{self.name}: {self.number}"

    def __getitem__(self, index):   # this magic method makes the class subscriptable.
        if index == 0:              # It helps when we want to order the differents objects of the class based on one of the attributes.
            return self.name
        elif index == 1:
            return self.number
        
    def __iter__(self):
        yield self.name
        yield self.number

class ContactManager():
    def __init__(self):        
        database_folder = os.path.join(os.path.dirname(__file__), "Contact_database")
        os.makedirs(database_folder, exist_ok=True)
        self.database_path = os.path.join(database_folder, "contacts.db")
        
        self.setup_database()

    def setup_database(self):
        try:
            with sqlite3.connect(self.database_path) as conn:
                cur = conn.cursor()

                cur.execute("""CREATE TABLE IF NOT EXISTS contacts(
                            Names TEXT NOT NULLIUNIQUE
                            Telephone_numbers TEXT NOT NULL UNIQUE
                            )""")
        except sqlite3.Error as e:
            print(f"Error during seting up the Database: {e}")
        
    def add_contact(self):
        name =  input("Enter the name: ").lower().capitalize()
        number = input("Enter the Telephone number: ")
        if not name or not number:
            print("Name or Number musn't be empty")
            return
        
        formated_name = string.capwords(name, sep=" ")
        try:
            with sqlite3.connect(self.database_path) as conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO contacts (Names, Telephone_numbers) VALUES (?, ?)", (formated_name, number))
                print("Contact successfully added.")
        except sqlite3.IntegrityError:
            print("Error: The given Telephone number has been already registered")
        except sqlite3.Error as e:
            print(f"Error during the Registration of this Contact: {e}")
   

    def delete_contact(self):
        name =  input("Enter the name: ").lower().capitalize()
        if not name:
            print("No name entered. Retry")
            return
        
        formated_name = string.capwords(name, sep=" ")
        try:
             with sqlite3.connect(self.database_path) as conn:
                cur = conn.cursor()
                cur.execute("DELETE FROM contacts WHERE Names = ?", (formated_name,))

                delected_count = cur.rowcount

                if delected_count > 0:
                    time.sleep(1)
                    #print(f"{delected_count} Contact(s) sucessfully deleted")
                    print(f"'{formated_name}' has been deleted from your Contact list.")
                else:
                    print(f"Contact with the name '{formated_name}' not found.")
        except sqlite3.Error as e:
            print(f"Error during the supression of the Contact: {e}")
                    
    def all_contacts(self):
        try:
            with sqlite3.connect(self.database_path) as conn:
                cur = conn.cursor()

                cur.execute("SELECT * FROM contacts ORDER BY Names")
                rows = cur.fetchall()

                if rows:
                    print("\n Available Contacts:")
                    contact_list = [Contact(row[0], row[1]) for row in rows]
                    headers = ["Names", "Telephone numbers"]
                    print(tabulate(contact_list, headers=headers, tablefmt="grid"))
                else:
                    print("No Contacts available")
        except sqlite3.Error as e:
            print(f"Error during Loading all Contacts: {e}")   

    def research_contact(self):
        search = input("Enter the name of the person you are looking for: ").lower().capitalize()
        if not search:
            print("No entry. Retry")
            return
        
        try:
             with sqlite3.connect(self.database_path) as conn:
                cur = conn.cursor()

                cur.execute("SELECT Names, Telephone_numbers FROM contacts WHERE Names = ?", (search,))
                found = cur.fetchall()

                if found:
                    found_contact = [Contact(row[0], row[1]) for row in found]
                    print(tabulate(found_contact, headers= ["Names", "Telephone numbers"], tablefmt="grid"))
                else:
                    print("Contact not found.")
        except sqlite3.Error as e:
            print(f"Error during The Search of th contact: {e}")

    def clear_contacts(self):
        ans = input("Do you really want to clear your Contact list? (yes/no): ").lower()
        if ans == 'yes':
            try:
                with sqlite3.connect(self.database_path) as conn:
                    cur = conn.cursor()

                    cur.execute("DELETE FROM contacts")
                    deleted_count = cur.rowcount

                    if deleted_count > 0: 
                        print("Your Contact list has been cleared.")
                    else:
                        print("Your Contact list is already empty")
            except sqlite3.Error as e:
                print(f"Error during clearing the Contact list: {e}")
        elif ans == 'no':
            pass
        else:
            print("Invalid input.")
            
    def main_menu(self):
        while True:
            print("\n====== Contact Manager ======")
            print("Welcome to your Contact Manager📑.") 
            print("Here are the actions that you can operate: ")  
            print("1- Add a Contact")    
            print("2- Delete a Contact")  
            print("3- Show all Contacts")
            print("4- Research a Contact")
            print("5- Clear contact list")
            print("6- Quit")
            num = input("Your Choice: ")
            
            if num == '1':
                print("You choosed '1' so you want to add a contact.\n")
                self.add_contact()
            elif num == '2':
                print("You choosed '2' so you want to delete a contact.\n")
                self.delete_contact()
            elif num == '3':
                print("You choosed '3' so you want to show all the Contacts.\n")    
                self.all_contacts()
            elif num == '4':
                self.research_contact()
            elif num == '5':
                self.clear_contacts()
            elif num == '6':
                answer = input("Do you really want to quit 😥?(yes/no): ").lower()  
                if answer == 'yes':
                    print("Good bye👋. It was a pleasure to treat with you.")
                    break
                elif answer == 'no':
                    continue 
                else:
                    print("Invalid Input. Retry") 
    
if __name__ == "__main__":
    repertory = ContactManager()
    repertory.main_menu()     