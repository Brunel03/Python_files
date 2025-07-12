import company as com

enterprise = com.Company()
while True:
    print("Welcome to the System of your Company. Here are the available operations:")
    print("1- Create a Department")
    print("2- Delete a Department")
    print("3- View all Departments")
    print("4- operate on a specific Department")
    print("5- Exit")

    try:
        rep = int(input("Select an operation(1-5): "))
        if rep == 1:
            enterprise.create_department()
        elif rep == 2:
            enterprise.delete_department()
        elif rep == 3:
            enterprise.view_departments()
        elif rep == 4:
            enterprise.operate_on_department()
        elif rep == 5:
            rep_1 = input("Do you want to quit? (yes/no):").lower()
            if rep_1 == 'yes':
                print("Good bye Sir/Madam")
                break
            elif rep_1 == 'no':
                continue
            else:
                print("You should enter 'yes' or 'no'")
        else:
            print("You should choose between 1 and 5\n")
    except ValueError:
        print("Invalid Input. only numeric entries are accepted.\n")