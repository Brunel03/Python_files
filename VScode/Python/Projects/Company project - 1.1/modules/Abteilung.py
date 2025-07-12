from tabulate import tabulate
import Angestellte as emp
import string

class Department():
    def __init__(self, name):
        self.name = string.capwords(name, sep=" ")
        self.employees = []

    def __str__(self):
        return f"Abteilungsname: {self.name}"
    
    def __len__(self):
        return len(self.employees)
    
    def __getitem__(self,index):
        if index == 0:
            return self.name

    def view_employee(self):
        if not self.employees:
            print("Keine Angestellte in dieser Abteilung.\n")
        else:
            self.employees.sort(key= lambda x:x[1])
            print(f"{len(self.employees)} employee(s) are working in this department")
            print(f"============= Employees of the {self.name} department =============")
            print(tabulate(self.employees, headers = ["Matriculation numbers", "Names", "Surnames", "Birthdates", "Birthplaces", "Salaries"], tablefmt="grid" ))