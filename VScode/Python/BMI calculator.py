gewicht = float(input("Gib dein Gewicht (in kg) ein: "))
körpergröße = float(input("Gib deine Körpergröße (in m) ein: "))

BMI = gewicht / körpergröße ** 2
print("BMI = "+str(round(BMI, 2)))