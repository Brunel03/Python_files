import random
print("Welcome to the game Rock,Paper,Scissor")
options = ["rock","paper","scissor"]
com_choice = random.choice(options)

ans = ''
while ans != "no":
    p_choice = input("Please Enter rock,paper or scissor: ").lower()
    while p_choice not in options:
        print("Invalid input. Try again")
        p_choice = input("Please Enter rock,paper or scissor: ").lower()

    if p_choice == com_choice:
        print("You both have the same choice.")
        continue
    elif (p_choice == "rock" and com_choice== "scissor") or (p_choice == "paper" and com_choice == "rock") or (p_choice == "scissor" and com_choice == "paper"):
        print("You won!")
    else:
        print("Sorry,You lost!")
    ans = input("Would you like to continue(yes/no): ").lower()
