import os
import csv
import time
import string

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

class ContactManager():
    def __init__(self):
        self.list_contacts = []
        self.load_data()        

    def load_data(self):
        database_path = os.path.join(os.path.dirname(__file__), "Contact_database")
        if not os.path.exists(database_path):
            os.makedirs(database_path) # a folder for the databases will be create, if it doesn't exists
            print(f"Database folder '{database_path}' created.")
            return
        
        print("Loading your contacts from the Database...")
        for file_name in os.listdir(database_path):
            if file_name.endswith(".csv"):
                file_path = os.path.join(database_path, file_name)

                try:
                    with open(file_path, "r", newline='', encoding='utf-8') as csvfile:
                        reader = csv.DictReader(csvfile, delimiter=';')
                        for line in reader:
                            contact_name = line.get("Name", "")
                            contact_number = line.get("Number", "")
                            contact = Contact(contact_name, contact_number)
                            self.list_contacts.append(contact)
                            time.sleep(1)
                    print(f"Loading complete. {len(self.list_contacts)} Contacts have been registered.")
                except FileNotFoundError:
                    print(f"Error during loading: file {file_name} not found")

    def save_data(self):
        database_path = os.path.join(os.path.dirname(__file__), "Contact_database")
        file_path = os.path.join(database_path, "contacts.csv")
        headers = ["Name", "Number"]
        try:
            with open(file_path, "w", newline='', encoding='utf-8')as csvfile:
                Writer = csv.DictWriter(csvfile, delimiter=";", fieldnames=headers)
                Writer.writeheader()
                for contact in self.list_contacts:
                    contact_data = {
                        "Name": contact.name,
                        "Number": contact.number
                    }
                    Writer.writerow(contact_data)
        except Exception as e:
            print(f"Error during Saving: {e}")
        
    def add_contact(self):
        name =  input("Enter the name: ").lower().capitalize()
        number = input("Enter the Telephone number: ")
        contact = Contact(name, number)
        self.list_contacts.append(contact)
        self.save_data()
        print("Contact successfully added.")
        return contact    
        
    def delete_contact(self):
        name =  input("Enter the name: ").lower().capitalize()
        #while not name.isalpha():
        #    print("Invalid input. Try again!\n")
        #    name =  input("Enter the name: ").lower().capitalize()

        for contact in self.list_contacts:
            if name in contact.name:
                self.list_contacts.remove(contact)
                self.save_data()
                print("Contact successfully removed.")
            else:
                print("Contact not founded.") 
                    
    def all_contacts(self):
        print("Your Contacts: ")
        for  i,contact in enumerate(sorted(self.list_contacts, key=lambda x:x[0]), start = 1):
            print(f"{i}- {contact}")   

    def research_contact(self):
        search = input("Enter the name of the person you are looking for: ").lower().capitalize()
        while not search.isalpha():
            print("Invalid input. Try again!")
            search = input("Enter the name of the person you are looking for: ").lower().capitalize()
        found = [contact for contact in self.list_contacts if search in contact.name]
        if found:
            for contact in found:
                print(f"{contact}") 
        else:
            print(f"Contact not found")

    def clear_contacts(self):
        ans = input("Do you really want to clear your Contact list? (yes/no): ").lower()
        if ans == 'yes':
            if self.list_contacts:
                self.list_contacts.clear()
                time.sleep(1)
                self.save_data()
                print("Your Contact list has been cleared.")
            else:
                print("Your Contact list is already empty")
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
