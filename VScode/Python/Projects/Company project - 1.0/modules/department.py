from tabulate import tabulate
import employee as emp
import string

class Department():
    def __init__(self, name):
        self.name = string.capwords(name, sep=" ")
        self.employees = []

    def __str__(self):
        return f"Department's name: {self.name}"
    
    def __len__(self):
        return len(self.employees)
    
    def __getitem__(self,index):
        if index == 0:
            return self.name
        
    def add_employee(self):
        name = input("Name: ").lower()
        surname = input("Surname: ").lower()
        birthdate = input("Birthdate (dd/mm/yyyy): ")
        birthplace = input("Birthplace: ").lower()
        salary = float(input("Salary (€): "))

        for employee in self.employees:
            if name == employee.name and surname == employee.surname:
                print("This Employee is already registered here.\n")
                return
            
        employee = emp.Employee(name, surname, birthdate, birthplace, salary)
        self.employees.append(employee)
        print(f"New employee hired in the {self.name} department.\n")

    def view_employee(self):
        if not self.employees:
            print("No Employee in this Department.\n")
        else:
            self.employees.sort(key= lambda x:x[1])
            print(f"{len(self.employees)} employee(s) are working in this department")
            print(f"============= Employees of the {self.name} department =============")
            print(tabulate(self.employees, headers = ["Matriculation numbers", "Names", "Surnames", "Birthdates", "Birthplaces", "Salaries"], tablefmt="grid" ))

    def operate_on_employee(self):
        search = input("Enter the matricule of the employee who want to fire: ").lower()
        found = [employee for employee in self.employees if search == employee.matricule]

        if found:
            for employee in found:
                print(employee)
            while True:
                print("Available Operations:\n")
                print("1- Modify Informations")
                print("2- Fire this employee")
                print("3- Return back")
                
                try:
                    ans = int(input("Choose an option(1-3): "))

                    if ans == 1:
                        employee.modify_informations()
                    elif ans == 2:
                        ans_1 = input("Do you really want to fire this employee ?(yes/no)").lower()
                        if ans_1 == 'yes':
                            self.employees.remove(employee)
                            print(f"Employee with the matricule {employee.matricule} fired")
                        elif ans_1 == 'no':
                            continue
                        else:
                            print("Invalid input. Choose between 'yes' or 'no'")
                    elif ans == 3:
                        break
                except ValueError:
                    print("Invalid Input. Only numeric entries are accepted")
        else:
            print("No employee with this Matricule found.")