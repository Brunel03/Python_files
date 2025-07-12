import Unternehmen as com

enterprise = com.Company()
while True:
    print("\nWillkommen im system Ihres Unternehmens. Hier sind die verfügbaren Operationen:")
    print("1- Angestellte einstellen")
    print("2- Abteilung erstellen")
    print("3- Alle verfügbare Abteilungen ansehen")
    print("4- Alle Angestellte ansehen")
    print("5- Informationen eines Angestelltes ändern")
    print("6- Operationen in einer spezifischer Abteilung durchführen")
    print("7- Angestellte in einer anderen Abteilung transferieren")
    print("8- Gehalt eines Angestelltes erhöhen/reduzieren")
    print("9- Angestellte kündigen")
    print("10- Abteilung entfernen")
    print("11- Quit")

    try:
        rep = int(input("Wählen sie eine Operation aus.(1-11): "))
        
        if rep == 1:
            enterprise.hire_employee()
        elif rep == 2:
            enterprise.create_department()
        elif rep == 3:
            enterprise.view_departments()
        elif rep == 4:
            enterprise.view_employees()
        elif rep == 5:
            enterprise.modify_informations()
        elif rep == 6:
            enterprise.operate_on_department()
        elif rep == 7:
            enterprise.transfer_employee()
        elif rep == 8:
            enterprise.increase_decrease_salary()
        elif rep == 9:
            enterprise.fire_employee()
        elif rep == 10:
            enterprise.delete_department()
        elif rep == 11:
            rep_1 = input("Möchten Sie beenden? (ja/nein):").lower()
            if rep_1 == 'ja':
                print("Auf wiedersehen")
                break
            elif rep_1 == 'nein':
                continue
            else:
                print("Sie sollen 'ja' oder 'nein' auswählen")
        else:
            print("Sie sollen zwischen 1 und 10 auswählen\n")
    except ValueError:
        print("Ungültige Eintrag. Nur numerische Einträge werden akzeptiert\n")