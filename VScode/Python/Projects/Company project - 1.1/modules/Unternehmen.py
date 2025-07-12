import string
import datetime
import Abteilung as dep
import Angestellte as emp
from tabulate import tabulate

class Company():
    def __init__(self):
        self.departments = []
        self.angestellten = []

    def __len__(self):
        return len(self.departments)
    
    def create_department(self):
        name = input("Name der neuen Abteilung: ").lower()
        for department in self.departments:
            if name == department.name:
                print("Diese Abteilung existiert schon\n")
                return
    
        department = dep.Department(name)
        self.departments.append(department)
        print("Neue Abteilung erstellt\n")

    def delete_department(self):
        search = input("Name der Abteilung: ").lower()
        search = string.capwords(search, sep=" ")

        current_dep = None
        for department in self.departments:
            if search == department.name:
                current_dep = department
                break

        if not current_dep:
            print("Abteilung nicht gefunden\n")
        else:
            ans_1 = input(f"Wollen Sie wirklich die {department.name}sabteilung löschen?(ja/nein): ").lower()
            if ans_1 == 'ja':
                for employee in current_dep:
                    if employee in self.angestellten:
                        self.angestellten.remove(employee)

                self.departments.remove(current_dep)
                print(f"Die {current_dep.name}sabteilung wurde erfolgreich gelöscht.\n")
            elif ans_1 == 'nein':
                pass
            else:
                print("Geben Sie entweder 'ja' oder 'nein' ein\n")

    def view_departments(self):
        if not self.departments:
            print("Keine Abteilung(en) in diesem Unternehmen.\n")
        else:
            print(f"Dieses Unternehmen enthält {len(self.departments)} Abteilung(en)")
            print("========== Verfügbare Abteilung(en) ==========")
            for department in self.departments:
                print(department)
            print("\n")

    def hire_employee(self):
        if len(self.departments) == 0:
            print("Keine Abteilung(en) im Unternehmen. Zur Einstellung eines Angestelltes sollte das Unternehmen mindestens eine Abteilung enthalten.")
            return
        
        vorname = input("Vorname: ").lower()
        nachname = input("Nachname: ").lower()
        try:
            geburtsdatum = input("Geburtsdatum (dd/mm/yyyy): ")
        except ValueError:
            print("Ungültiges Datumsformat")
        geburtsort = input("Geburtsort: ").lower()
        gehalt = float(input("Gehalt (€): "))

        for employee in self.angestellten:
            if vorname == employee.vorname and nachname == employee.nachname:
                print("Dieser Angestellte wurde hier schon registriert\n")
                return
        
        employee = emp.Employee(vorname, nachname, geburtsdatum, geburtsort, gehalt)
        rep_1 = input("In welcher Abteilung sollte dieser Angestellte hinzugefügt werden? ").lower()
        rep_1 = string.capwords(rep_1, sep=" ")
        dp = [department for department in self.departments if rep_1 == department.name]
        if not dp:
            print("Abteilung nicht gefunden.")
        else:
            self.angestellten.append(employee)
            for department in dp:
                department.employees.append(employee)
                print(f"Neuer Angestellte in der {department.name}sabteilung eingestellt.")

    def fire_employee(self):
        if len(self.departments) == 0 or len(self.angestellten) == 0:
            print("Keine Angestellte im Unternehmen. Zur Entlassung eines Angestelltes sollte mindestens einen Angestellte hier arbeiten.")
            return

        self.view_employees()
        search_2 = input("Matrikelnummer des zu entlassenden Angestelltes: ").lower()

        found_employee = None
        for employee in self.angestellten:
            if search_2 == employee.Matrikel.lower():
                found_employee = employee
                break

        if found_employee:
            print(found_employee)
            rep = input("\nMöchten Sie wirklich dieser Angestellte entlassen?(ja/nein): ").lower()
            if rep == 'ja':
                for department in self.departments:
                    if found_employee in department.employees:
                        department.employees.remove(found_employee)

                self.angestellten.remove(employee)
                print(f"Herr/Frau {employee.nachname} sind jetzt gekündigt")
            elif rep == 'nein':
                pass
            else:
                print("Sie müssen entweder 'ja' oder 'nein' eingeben.")
        else:
            print("Angestellte nicht gefunden. Es kann sein, dass Sie eine falsche Matrikelnummer eingegeben haben.")

    def view_employees(self):
        if not self.angestellten:
            print("Keine Angestellte in diesem Unternehmen")
        else:
            print(f"Derzeit sind {len(self.angestellten)} in diesem Unternehmen tätig\n")
            print("============== Liste allen Angestellte ==============")
            print(tabulate(self.angestellten, headers=["Matrikelnummern", "Vornamen", "Nachnamen", "Geburtsdatum", "Geburtsorten", "Gehälter"], tablefmt= "grid"))

    def transfer_employee(self):
        if not self.angestellten:
            print("Keine Angestellte im Unternehmen.")
        elif len(self.departments) < 2:
            print("Keine genugende Abteilungen zur Transferierung eines Angestelltes.")

        search_2 = input("Matrikelnummer des zu transferierenden Angestelltes: ").lower()
        
        found_employee = None
        for employee in self.angestellten:
            if search_2 == employee.Matrikel.lower():
                found_employee = employee
                break

        current_dep = None
        for department in self.departments:
            if found_employee in department.employees:
                current_dep = department
                break

        if not found_employee:
            print("Angestellte nicht gefunden.")
        else:
            print(found_employee)
            dep_1 = input(f"In welchen Abteilung sollte dieser Angestellte transferiert werden: ")
            dep_1 = string.capwords(dep_1, sep=" ")

            final_dep = None
            for department in self.departments:
                if dep_1 == department.name:
                    final_dep = department
                    break

            if not final_dep:
                print("Diese Abteilung existiert nicht. Transfer nicht möglich.")
            elif (current_dep == final_dep) or (found_employee in final_dep.employees):
                print("Der Angestellte arbeitet schon in dieser Abteilung")
            else:
                current_dep.employees.remove(found_employee)
                final_dep.employees.append(found_employee)
                print(f"Herr/Frau {found_employee.nachname} in der {final_dep.name} abteilung erfolgreich transferiert.")



    def increase_decrease_salary(self):
        search_3 = input("Matrikelnummer des Angestelltes, dessen Gehalt erhöht oder reduziert werden: ").lower()
        found_3 = [employee for employee in self.angestellten if search_3 == employee.Matrikel.lower()]
        if not found_3:
            print("Angestellte nicht gefunden")
        else:
            for employee in found_3:
                print(employee)
                print("\n1- Gehalt erhöhen")
                print("2- Gehalt reduzieren")
                try:
                    rep_2 = int(input("Wählen Sie eine Operation aus: "))
                    if rep_2 == 1:
                        try:
                            amount_1 = float(input("Um wie viel sollte sein/ihr Gehalt erhöht werden (€)? "))
                            if amount_1 <= 0:
                                print("Der Betrag muss größer oder gleich null sein.")
                            else:
                                employee.gehalt += amount_1
                                print(f"Gehalt des Angestelltes N° {employee.Matrikel} um {amount_1}€ erhöht. Neues Gehalt: {employee.gehalt}€")
                        except ValueError:
                            print("Fehler bei der Eingabe.")
                    elif rep_2 == 2:
                        try:
                            amount_2 = float(input("Um wie viel sollte sein/ihr Gehalt reduziert werden (€)? "))
                            if amount_2 <= 0:
                                pass
                            elif amount_2 >= employee.gehalt:
                                print("Der Betrag muss kleiner als der gehalt sein.")
                            else:
                                employee.gehalt -= amount_2
                                print(f"Gehalt des Angestelltes N°{employee.Matrikel} um {amount_2}€ verringer. Neues Gehalt: {employee.gehalt}€")
                        except ValueError:
                            print("Fehler bei der Eingabe.")
                    else:
                        pass
                except ValueError:
                    print("Nur numerische Einträge sind akzeptiert.")

    def modify_informations(self):
        search_3 = input("Matrikelnummer des Angestellten, deren Informationen verändert werden sollten: ").lower()

        found_employee = None
        for employee in self.angestellten:
            if search_3 == employee.Matrikel.lower():
                found_employee = employee
                break

        print("\nWelche Information wollen sie ändern:")
        print("1- Vorname")
        print("2- Nachname")
        print("3- Geburtsdatum")
        print("4- Geburtsort")
        print("5- Gehalt")

        try:
            ans = int(input("Wählen Sie eine Operation aus (1-4): "))

            if ans == 1:
                new_vorname = input("Vorname: ").lower()
                found_employee.vorname = string.capwords(new_vorname, sep =" ")
                print("Vorname geändert")
            elif ans == 2:
                new_nachname = input("Nachname: ").lower()
                found_employee.nachname = string.capwords(new_nachname , sep =" ")
                print("Nachname geändert")
            elif ans == 3:
                try:
                    new_geburtsdatum = input("Geburtsdatum (dd/mm/yyyy): ")
                    found_employee.geburtsdatum = datetime.datetime.strptime(new_geburtsdatum, "%d/%m/%Y").date()
                    print("Geburtsdatum geändert")
                except ValueError:
                    print("Ungültiges Datumsformat")
            elif ans == 4:
                new_geburtsort = input("Geburtsort: ").lower()
                found_employee.geburtsort = string.capwords(new_geburtsort , sep =" ")
                print("Geburtsort geändert")
            else:
                print("Ungültiger Eintrag. Wählen Sie von 1 bis 4.")

        except ValueError:
            print("Ungültiger Eintrag. Nur numerische Einträge werden akzeptiert.")


    def operate_on_department(self):
        search_1 = input("Name der Abteilung: ").lower()
        search_1 = string.capwords(search_1, sep=" ")
        found_1 = [department for department in self.departments if search_1 == department.name]
        if found_1:
            for department in found_1:
                print(department)
            while True:
                print("1- Alle Angestellte der Abteilung ansehen")
                print("2- Rückgang zum Hauptmenu")

                try:
                    ans_1 = int(input("Wählen Sie eine operation aus(1-2): "))
                    if ans_1 == 1:
                        department.view_employee()
                    elif ans_1 == 2:
                        break
                    else:
                        print("Wählen Sie zwischen 1 und 2\n")
                        
                except ValueError:
                    print("Ungültiger Eintrag. Nur numerische Einträge sind akzeptiert\n")
        else:
            print("Abteilung nicht gefunden\n")
