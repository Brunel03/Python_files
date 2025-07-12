import department as dep

class Company():
    def __init__(self):
        self.departments = []

    def __len__(self):
        return len(self.departments)
    
    def create_department(self):
        name = input("Name of the new department: ").lower()
        for department in self.departments:
            if name == department.name:
                print("This Department already exists\n")
                return
    
        department = dep.Department(name)
        self.departments.append(department)
        print("New department created\n")

    def delete_department(self):
        search = input("Name of the department: ").lower().capitalize()
        for department in self.departments:
            if search == department.name:
                ans_2 = input(f"Do you really want to delete the {department.name} department?(yes/no): ").lower()
                if ans_2 == 'yes':
                    self.departments.remove(department)
                    print(f"The {department.name} department has been deleted.\n")
                elif ans_2 == 'no':
                    continue
                else:
                    print("Choose 'yes' or 'no'\n")
            else:
                print("Department not found\n")

    def view_departments(self):
        if not self.departments:
            print("No Department in this company.\n")
        else:
            print(f"This Company has {len(self.departments)} department(s)")
            print("========== Available Department(s) ==========")
            for department in self.departments:
                print(department)
            print("\n")

    def operate_on_department(self):
        search_1 = input("Name of the department: ").lower().capitalize()
        found_1 = [department for department in self.departments if search_1 == department.name]
        if found_1:
            for department in found_1:
                print(department)
            while True:
                print("1- Hire an new employee")
                print("2- View all employees of this department")
                print("3- Fire an employee")
                print("4- Return back")

                try:
                    ans_1 = int(input("Choose an operation(1-5): "))
                    if ans_1 == 1:
                        department.add_employee()
                    elif ans_1 == 2:
                        department.view_employee()
                    elif ans_1 == 3:
                        #department.fire_employee()
                        continue
                    elif ans_1 == 4:
                        break
                    else:
                        print("Choose between 1 and 4\n")
                        
                except ValueError:
                    print("Invalid input. Only numeric entries are accepted.\n")
        else:
            print("Department not found\n")
