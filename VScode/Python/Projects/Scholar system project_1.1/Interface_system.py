from package import Scholar_System

school_1 = Scholar_System.School()

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