from datetime import date
def determine_day(birth_day):
day1 = date.today()
day2 = input("Entrer votre date de naissance :")
diff = day2 - day1
print("vous avez vécu pendant",diff.days,"jours de vie")
