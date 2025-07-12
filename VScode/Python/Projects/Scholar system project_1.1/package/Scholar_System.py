import datetime
import random
import string
import csv
import os


used_matriculation_numbers = set() #database for matriculation numbers which have been already given.

class Student():
    def __init__(self, name, surname, birthdate_str, birthplace, matriculation_number=None):
        if matriculation_number is None:
             # generate a matriculation number if no one has been generated
            self.matriculation_number = self.generate_matriculation_number()
        else:
            # Vorhandene Matrikelnummer verwenden (beim Laden)
            self.matriculation_number = matriculation_number
        self.name = string.capwords(name, sep =" ")
        self.surname = string.capwords(surname, sep =" ")

        self._birthdate_str = birthdate_str # Interner String-Wert
        try:
             self.birthdate = datetime.datetime.strptime(birthdate_str, "%d/%m/%Y").date()
        except ValueError:
             self.birthdate = None # Oder handle Fehler anders

        self.birthplace = string.capwords(birthplace, sep =" ")
    
    def __str__(self) -> str:
        return f"Matriculation number: {self.matriculation_number}\nName: {self.name}\nSurname: {self.surname}\nDate of Birth: {self.birthdate}\nPlace of birth: {self.birthplace}"

    def __iter__(self):
        yield self.matriculation_number
        yield self.name
        yield self.surname
        yield self._birthdate_str
        yield self.birthplace

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
        global used_matriculation_numbers 
        letters = string.ascii_uppercase
        while True:
            matriculation_number = ''.join(random.choice(letters) for i in range(2)) +'-'+ ''.join(random.choice('0123456789') for i in range(4))
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
            new_birthdate_str = input("Enter the new birthdate (dd/mm/yyyy): ")
            self.birthdate = datetime.datetime.strptime(new_birthdate_str, "%d/%m/%Y").date()
            try:
                self.birthdate = datetime.datetime.strptime(new_birthdate_str, "%d/%m/%Y").date()
                self._birthdate_str = new_birthdate_str # String-Repräsentation aktualisieren
                print("Birthdate succesfully modified.")
            except ValueError:
                print("Invalid Date format.")
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
        
    def save_to_csv(self):
        database_path = os.path.join(os.path.dirname(__file__), "..", "Database")
        filepath = os.path.join(database_path, self.name + ".csv")

        try:
            # Öffnen im Schreibmodus ('w') löscht den alten Inhalt
            with open(filepath, 'w', newline='', encoding='utf-8') as data:
                 headers = ["Matriculation Number", "Name", "Surname", "Birthdate", "Birthplace"] # define Header
                 writer = csv.DictWriter(data, fieldnames=headers, delimiter=';')

                 writer.writeheader()

                 for student in self.students:
                     # Student-Daten in ein Dictionary umwandeln für DictWriter
                     student_data = {
                         "Matriculation Number": student.matriculation_number,
                         "Name": student.name,
                         "Surname": student.surname,
                         "Birthdate": student._birthdate_str, # String-Datum verwenden
                         "Birthplace": student.birthplace
                     }
                     writer.writerow(student_data)
            print(f"Class '{self.name}' Sucessfully registered.")
        except Exception as e:
            print(f"Fehler beim Speichern der Klasse '{self.name}': {e}")

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
                    print("This Student is already enroll in this Class.\n")
                    return

            student = Student(name,surname,birthdate,birthplace)
            self.students.append(student)
            print("New student sucessfully added.\n")
            self.save_to_csv()
            return student
        else:
            print("The class is already full.\n")
        


    def view_classroom(self):
        """
        In this function will be show all the students which are enrolled in a class.
        """
        if not self.students:
            print("No Students")
        else:
            print(f"\n========== List of students of '{self.name}' ==========")
            #self.students.sort(key= lambda x:x[3])
            for student in self.students:
                print(f"{student}\n")
        
    def operate(self):
        """
        Here we can operate actions on a student such as modifying his informations when there is an error
        in his informations and excluding him. You can also return back to the previously menu.
        """
        self.view_classroom()
        search = input("\nOn which student should we do an action 🤨(enter the matriculation number): ").lower().upper()
        Found_1 = [student for student in self.students if search == student.matriculation_number]
        if Found_1:
            for student in Found_1:
                print(student)
            while True:
                print("\nAvailable Operations:")
                print("1- modify some Informations")
                print("2- exclude")
                print("3- Return back")
                num = int(input("Your choice(1-3): "))
                #while not num.isnumeric():
                 #   print("Enter a Number not an other Character.")
                  #  num = input("Your choice(1-3): ")

                if num == 1:
                    student.modify()
                    self.save_to_csv()
                elif num == 2:
                    ans = input(("Are you sure? (yes/no): ")).lower()
                    if ans == 'yes':
                        self.students.remove(student)
                        self.save_to_csv()
                        print(f"Student '{student.name} {student.surname}' excluded from the class {self.name}")
                        self.view_classroom()
                    elif ans == 'no':
                        continue
                    else:
                        print("Invalid input: Choose between 'yes' or 'no'")
                elif num == 3:
                    break
        else:
            print("Student not found")
        

class School():
    def __init__(self) -> None:
        self.name = input("Please enter the name of the School: ").lower().upper()
        self.classrooms = []
        #self.used_matriculation_numbers = set()
        self.load_data()

    def __len__(self):
        return  len(self.classrooms)
    
    def load_data(self):
        database_path = os.path.join(os.path.dirname(__file__), "..", "Database")
        if not os.path.exists(database_path):
            os.makedirs(database_path) # a folder for the databases will be create, if it doesn't exists
            print(f"Datenbank-Ordner '{database_path}' erstellt.")
            return
        
        print("Loading Datas from CSV-Files...")
        for file_name in os.listdir(database_path):
            if file_name.endswith(".csv"):
                class_name = os.path.splitext(file_name)[0] # Filename without ending is the name of the class
                classroom = Classroom(class_name) # creates a new Classroom-Object
                file_path = os.path.join(database_path, file_name)

                try:
                    with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
                        # Annahme: CSV hat Header (DictReader ist gut dafür)
                        reader = csv.DictReader(csvfile, delimiter=';')
                        for row in reader:
                            try:
                                # converting datas from the CSV-lines to a student object
                                student_matricule = row.get("Matriculation Number", "")
                                student_name = row.get("Name", "")
                                student_surname = row.get("Surname", "")
                                student_birthdate_str = row.get("Birthdate", "")
                                student_birthplace = row.get("Birthplace", "")

                                # converting Birthdate from String into Date-Object
                                student_birthdate = None
                                if student_birthdate_str:
                                    student_birthdate = datetime.datetime.strptime(student_birthdate_str, "%d/%m/%Y").date()

                                # creating a new student-Object without generating a new matriculation number
                                # Dazu brauchen wir einen __init__ in Student, der Matrikelnummer akzeptiert
                                student = Student(student_name, student_surname, student_birthdate_str, student_birthplace, matriculation_number=student_matricule)
                                student.birthdate = student_birthdate # Datum-Objekt zuweisen

                                classroom.students.append(student) 
                                if student_matricule: # Matrikelnummer zum Set hinzufügen, wenn vorhanden
                                    used_matriculation_numbers.add(student_matricule)

                            except ValueError:
                                print(f"Warning: Invalid birthdate-Format in Data '{file_name}', Line {reader.line_num}: {row}")
                            except Exception as e:
                                print(f"Error beim Verarbeiten der Zeile in Datei '{file_name}', Line {reader.line_num}: {e}")


                    self.classrooms.append(classroom) # Classroom zur School-Liste hinzufügen
                    print(f"Class '{class_name}' with {len(classroom.students)} Students loaded.")

                except FileNotFoundError:
                     print(f"Error by Loading: Data '{file_name}' not found (sollte nicht passieren, da gelistet).")
                except Exception as e:
                    print(f"Error by reading the Data'{file_name}': {e}")


    def create_classroom(self):
        print("******** Creation of a Class ********")
        name_1 = input("Enter the name of the Class: ").lower().upper()
    
        # We verify if the Class already exists.
        database = os.path.join(os.path.dirname(__file__), "..", "Database")
        name = name_1 + ".csv"
        for file in os.listdir(database):
            if name == file:
                print(f"'{name_1}' already exists")
                return
       
        newclass = Classroom(name_1)
        self.classrooms.append(newclass)
        headers = ["Matriculation Number", "Name", "Surname", "Birthdate", "Birthplace"]
        with open(os.path.join(database, name), 'x', newline="", encoding="utf-8") as data:
            writer = csv.DictWriter(data, fieldnames= headers)
            writer.writeheader()
            pass
        print("New Class sucessfully created")
        return newclass
    
        

    def view_classrooms(self):
        if not self.classrooms:
            print("No class registered.")
        else:
            print(f"\n========== Classes of the '{self.name}' ==========")
            for newclass in self.classrooms:
                print(newclass)
        

    def empty_classroom(self):
        self.view_classrooms()
        search_1 = input("Which class do you want to empty🤨: ").lower().upper()
        Found_2 = next((newclass for newclass in self.classrooms if search_1 == newclass.name), None)
        if Found_2:
            for newclass in Found_2:
                #newclass = Classroom(newclass)
                print(newclass)
            ans_2 = input(f"Are you sure you want to empty the classroom '{Found_2.name}'? (yes/no): ").lower()
            if ans_2 == 'yes':
                Found_2.students.clear()
                Found_2.save_to_csv()
                print(f"The class '{Found_2.name}' has been emptied.\n")
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
                print("\nAvailable Operations:")
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

    def main_menu(self):
        while True:
            print(f"\n\t========== {school_1.name}👨‍🏫🏫 ==========")
            print(f"Welcome to the system of the {school_1.name}")
            print("1- Create a Class")
            print("2- View Classes")
            print("3- Empty Class")
            print("4- Perform actions on a Class")
            print("5- Quit")
            choice_1 = input("Enter your Choice(1-5): ")

            if choice_1 == '1':
                school_1.create_classroom()
            elif choice_1 == '2':
                school_1.view_classrooms()
            elif choice_1 == '3':
                school_1.empty_classroom()
            elif choice_1 == '4':
                school_1.operate_classroom()
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

if __name__ == "__main__":
    school_1 = School()
    school_1.main_menu()