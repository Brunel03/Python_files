import datetime
from tabulate import tabulate
import random
import string
import csv

used_matriculation_numbers = set() #database for matriculation numbers which have been already given.

class Student():
    def __init__(self,name,surname,birthdate,birthplace):
        self.name = string.capwords(name, sep =" ")
        self.surname = string.capwords(surname, sep =" ")
        self.birthdate = datetime.datetime.strptime(birthdate, "%d/%m/%Y").date()
        self.birthplace = string.capwords(birthplace, sep =" ")
        self.matriculation_number = self.generate_matriculation_number()
    
    def __str__(self) -> str:
        return f"Name: {self.name}\nSurname: {self.surname}\nDate of Birth: {self.birthdate}\nPlace of birth: {self.birthplace}"

    def __iter__(self):
        yield self.name
        yield self.surname
        yield self.birthdate
        yield self.birthplace
        yield self.matriculation_number

    def __getitem__(self,index):
        if index == 0:
            return self.name
        elif index == 1:
            return self.surname
        elif index == 2:
            return self.birthdate
        elif index == 3:
            return self.birthplace

    def generate_matriculation_number(self):
        letters = string.ascii_uppercase
        while True:
            matriculation_number = ''.join(random.choice(letters) for i in range(2)) + ''.join(random.choice('0123456789') for i in range(4))
            # here we verify if the matriculation number has been already given to a Student. The given matriculation number are store in the database called 'used_matriculation_numbers'
            if matriculation_number not in used_matriculation_numbers:
                used_matriculation_numbers.add(matriculation_number)
                return matriculation_number

    def modify(self):
        """
         This Function allows to modify informations of a student
        """
        print("\nWhich Information should be modify ?")
        print("1- Name")
        print("2- Surname")
        print("3- Birthdate")
        print("4- Birthplace")
        num = input("Your choice (1-4)>> ")
        while not num.isnumeric() or int(num) <= 0 or int(num) > 4:
            print("Your Input isn't valid. Retry!")
            num = input("Your choice (1-4)>> ")

        if num == '1':
            new_name = input("Enter the new name: ").lower().capitalize()
            self.name = string.capwords(new_name, sep =" ")
            print("Name succesfully modified.")
        elif num == '2':
            new_surname = input("Enter the new name: ").lower().capitalize()
            self.surname = string.capwords(new_surname, sep =" ")
            print("Surname succesfully modified.")
        elif num == '3':
            new_birthdate = input("Enter the new birthdate (dd/mm/yyyy): ")
            self.birthdate = datetime.datetime.strptime(new_birthdate, "%d/%m/%Y").date()
            print("Birthdate succesfully modified.")
        elif num == '4':
            new_birthplace = input("Enter the new Birthplace: ").lower().capitalize()
            self.birthplace = string.capwords(new_birthplace, sep =" ")
            print("Birthplace succesfully modified.")
        else:
            print("Invalid input. Try again!")
        return

class Classroom():
    def __init__(self,name) -> None:
        self.name = name.lower().upper()
        self.max_places = 50
        self.students = []
    
    def __str__(self):
        return f"Class: {self.name}"

    def __iter__(self):
        yield self.name
        yield self.max_places

    def __len__(self):      #to  determinate the lenght of the classroom
        return len(self.students)

    def __getitem__(self,index):
        if index == 0:
            return self.name

    def enroll_student(self):
        """
        This function permitt to enroll a student in a class. After entering the informations of the student
        you want to enroll, the function verify if the student is already in the Class by checking if a student of the class
        has the same whole name with the new student.
        """
        if len(self) < self.max_places:
            print("******** Enrollment of a Student ********")
            name = input("\nEnter the Name: ").lower().capitalize()
            surname = input("Enter the Surname: ").lower().capitalize()
            birthdate = input("Enter the Date of Birth (dd/mm/yyyy): ")
            birthplace = input("Enter the Place of birth: ").lower().capitalize()
            # We verify if the student is already enroll in the class before we enroll him.
            for student in self.students:
                if name == student.name and surname == student.surname:
                    print("This Student is already enroll in this Class.")
                    return

            student = Student(name,surname,birthdate,birthplace)

            
            self.students.append(student)
            print("New student sucessfully added.")
            return student
        else:
            print("The class is already full.\n")
        


    def view_classroom(self):
        """
        In this function will be show all the students which are enrolled in a class.
        """
        self.students.sort(key= lambda x:x[2])
        try:
            print(f"\n========== List of Students of '{self.name}' ===========")
            print(tabulate(self.students,  headers = ["Names", "Surnames", "Date of birth", "Place of birth","Matriculation Numbers"], tablefmt = "grid"))
        except NameError:
            print("The module 'tabulate' has not been imported or installed")
        #for student in self.students:
        #    print(f"{student}\n")
        

    def search_student(self):
        search = input("\nFor which student are you looking for🤨: ").lower().capitalize()
        for student in self.students:
            if search in student.name or search in student.surname:
                print(student)
            else:
                print("Student not found.\n")
        

    def operate(self):
        """
        Here we can operate actions on a student such as modifying his informations when there is an error
        in his informations and excluding him. You can also return back to the previously menu.
        """
        self.view_classroom()
        search = input("\nOn which student should we do an action 🤨: ").lower().capitalize()
        Found_1 = [student for student in self.students if search in student.name or search in student.surname] 
        if Found_1:
            for student in Found_1:
                print(student)
            while True:
                print("\nAvailable Operations:")
                print("1- modify some Informations")
                print("2- exclude")
                print("3- Return back")
                num = input("Your choice(1-3): ")
                #while not num.isnumeric():
                 #   print("Enter a Number not an other Character.")
                  #  num = input("Your choice(1-3): ")

                if num == '1':
                    student.modify()
                elif num == '2':
                    ans = input(("Are you sure? (yes/no): ")).lower()
                    if ans == 'yes':
                        self.students.remove(student)
                        print(f"Student '{student.name} {student.surname}' excluded from the class {self.name}")
                        self.view_classroom()
                    elif ans == 'no':
                        continue
                    else:
                        print("Invalid input: Choose between 'yes' or 'no'")
                elif num == '3':
                    break
        else:
            print("Student not found")
        

class School():
    def __init__(self) -> None:
        self.name = input("Please enter the name of the School: ").lower().upper()
        self.classrooms = []
        #self.classrooms = [Classroom("2nde C1"), Classroom("PC"), Classroom("PD1"), Classroom("PD2")]

    def __len__(self):
        return  len(self.classes)

    def create_classroom(self):
        print("******** Creation of a Class ********")
        name_1 = input("Enter the name of the Class: ").lower().upper()
        #newclass = Classroom(name_1)
        # We verify if the Class already exists.
        for newclass in self.classrooms:
            if name_1 == newclass.name:
                print("This Class exists already")
                return

        newclass = Classroom(name_1)
        self.classrooms.append(newclass)
        print("New Class sucessfully created")
        return newclass

    def view_classrooms(self):
        if not self.classrooms:
            print("No class registered.")
        else:
            try:
                self.classrooms.sort(key = lambda x:x[0])
                print(f"\n========== Classes of the '{self.name}' ==========")
                print(tabulate(self.classrooms, headers = ["Classes","Max Places"], tablefmt= "grid"))
            except NameError:
                print("The module 'tabulate' has not been imported or installed.")
            finally:
                print(f"\n========== Classes of the '{self.name}' ==========")
                for newclass in self.classrooms:
                    print(newclass)
        

    def empty_classroom(self):
        self.view_classrooms()
        search_1 = input("Which class do you want to empty🤨: ").lower().upper()
        Found_2 = [newclass for newclass in self.classrooms if search_1 in newclass.name]
        if Found_2:
            for newclass in Found_2:
                print(newclass)
            ans_2 = input(f"Are you sure you want to empty the classroom '{newclass.name}'? (yes/no): ").lower()
            if ans_2 == 'yes':
                newclass.students.clear()
                print(f"The class '{newclass.name}' has been emptied.\n")
            elif ans_2 == 'no':
                pass
                #continue
        else:
            print("This class is not in the Database.\n")
        
    
    def operate_classroom(self):
        self.view_classrooms()
        choice = input("On which class you would you like to do some action 🤨: ").lower().upper()
        Found_3 = [newclass for newclass in self.classrooms if choice == newclass.name]
        if Found_3:
            for newclass in Found_3:
                print("\n")
            while True:
                print("Available Operations:")
                print("1- Enroll a Student in this class")
                print("2- View Students of this Class")
                print("3- Perform actions on a Student of this class")
                print("4- Return to main menu")
                num_1 = input("Enter your choice(1-4): ")
                #while not num_1.isnumeric() or int(num_1) <= 0 or int(num_1) > 4:
                #    print("\nYou should enter a number between 1 and 3:")
                #    num_1 = input("Enter your choice: ")
                if num_1 == '1':
                    newclass.enroll_student()
                elif num_1 == '2':
                    newclass.view_classroom()
                elif num_1 == '3':
                    newclass.operate()
                elif num_1 == '4':
                    break
        else:
            print("Classroom not found.")
        
    """
    def main_menu(self):
        while True:
            print(f"\n\t========== {self.name}👨‍🏫🏫 ==========")
            print(f"Welcome to the system of the {self.name}")
            print("1- Create a Class")
            print("2- View Classes")
            print("3- Empty Class")
            print("4- Perform actions on a Class")
            print("5- Quit")
            #try:
            choice_1 = input("Enter your Choice(1-5): ")
            #except UnboundLocalError:
                #print("You must enter a number anything else.")

            if choice_1 == '1':
                self.create_classroom()
            elif choice_1 == '2':
                self.view_classrooms()
            elif choice_1 == '3':
                self.empty_classroom()
            elif choice_1 == '4':
                self.operate_classroom()
            elif choice_1 == '5':
                ans_2 = input("Do you really want to quit (yes/no): ").lower()
                while ans_2 != "yes" and ans_2 != "no":
                    print("\nYou must choose 'yes' or 'no'.")
                    ans_2 = input("Do you really want to quit (yes/no): ").lower()
                    
                if ans_2 == "yes":
                    print("Good Bye👋.")
                    break
                elif ans_2 == "no":
                    continue
    """

if __name__ == "__main__":
    school_1 = School()