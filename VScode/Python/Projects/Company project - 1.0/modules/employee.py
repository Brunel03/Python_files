import string
import datetime
import random

used_matricule = set()
class Employee():
    def __init__(self,name,surname,birthdate,birthplace,salary,matricule=None):
        self.name = string.capwords(name, sep =" ")
        self.surname = string.capwords(surname, sep =" ")
        self.birthdate = datetime.datetime.strptime(birthdate, "%d/%m/%Y").date()
        self.birthplace = string.capwords(birthplace, sep =" ")
        self.salary = salary
        if matricule is None:
            self.matricule = self.generate_matricule()
        else:
            self.matricule = matricule

    def __str__(self):
        return f"Matricule: {self.matricule}\nName: {self.name}\nSurname: {self.surname}\nBirthdate: {self.birthdate}\nBirthplace: {self.birthplace}\nSalary: {self.salary}"
    
    def __iter__(self):
        yield self.matricule
        yield self.name
        yield self.surname
        yield self.birthdate
        yield self.birthplace
        yield self.salary

    def __getitem__(self,index):
        if index == 0:
            return self.matricule
        elif index == 1:
            return self.name
        elif index == 2:
            return self.surname
        elif index == 3:
            return self.birthdate
        elif index == 4:
            return self.birthplace
        elif index == 5:
            return self.salary
        
    def generate_matricule(self):
        global used_matricule
        letters = string.ascii_uppercase
        while True:
            matriculation_number = ''.join(random.choice(letters) for i in range(2)) +'-'+ ''.join(random.choice('0123456789') for i in range(4))
            if matriculation_number not in used_matricule:
                used_matricule.add(matriculation_number)
                return matriculation_number
            
    def modify_informations(self):
        print("\nWhich Information would you want to change:")
        print("1- Name")
        print("2- Surname")
        print("3- Birthdate")
        print("4- Birthplace")
        print("5- Salary")

        try:
            ans = int(input("Choose an Information(1-4): "))

            if ans == 1:
                new_name = input("Enter the name: ").lower()
                self.name = string.capwords(new_name, sep =" ")
                print("Name modified")
            elif ans == 2:
                new_surname = input("Enter the surname: ").lower()
                self.surname = string.capwords(new_surname , sep =" ")
                print("Surname modified")
            elif ans == 3:
                try:
                    new_birthdate = input("Enter the Birthdate (dd/mm/yyyy): ")
                    self.birthdate = datetime.datetime.strptime(new_birthdate, "%d/%m/%Y").date()
                    print("Birthdate modified")
                except ValueError:
                    print("Invalid date format")
            elif ans == 4:
                new_birthplace = input("Enter the Birthplace: ").lower()
                self.birthplace = string.capwords(new_birthplace , sep =" ")
                print("Birthplace modified")
            else:
                print("Invalid input. choose between 1 and 4")

        except ValueError:
            print("Invalid Input. Only numeric entries are accepted")
