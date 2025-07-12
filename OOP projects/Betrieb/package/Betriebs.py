class Mitarbeiter:
    def __init__(self,name,gehalt):
        self.name = name
        self.gehalt = gehalt

    def __iter__(self):  # Mit dieser Methode wird jede Eigenschaft iterierbar gemacht
        yield self.name
        yield self.gehalt

    def __str__(self):
        return f"Name: {self.name}\nGehalt: {self.gehalt}€\n"

class Abteilung:
    def __init__(self,name):
        self.name = name
        self.list = []

from tabulate import tabulate
class Firma:
    def __init__(self,name):
        self.name = name
        self.abteilungsliste = []
        print(f"Firma \"{self.name}\" gegründet.\n")

    def abteilung_erstellen(self, name): 
        if name not in self.abteilungsliste:
            neue_abteilung = Abteilung(name) # Hier erstellt man eine neue Abteilung,indem wir die Klasse Abteilung benutzt,die man oben erstellt hat
            self.abteilungsliste.append(neue_abteilung)
            print(f"{name} Abteilung erstellt.\n")
        else:
            print(f"{name} Abteilung schon in der Firma.\n")
        return neue_abteilung #Dieser Befehl ist wichtig,weil es gibt das neu erstellte Objekt Abteilung zurück und man kann die Methode der Klasse benutzen (Abteilung)
        
    def abteilung_löschen(self, abteilung):
        if abteilung in self.abteilungsliste:
            self.abteilungsliste.remove(abteilung)
            print(f"{abteilung.name} Abteilung entfernt.\n")
        else:
            print(f"{abteilung.name} Abteilung ist nicht in dieser Firma. Infolgedessen können wir sie nicht entfernen.\n")

    def mitarbeiter_hinzufügen(self, abteilung, *mitarbeitern): # Hier 
        for mitarbeiter in mitarbeitern: 
            if abteilung in self.abteilungsliste:
                abteilung.list.append(mitarbeiter)
                print(f"Neuer Mitarbeiter erfolgreich hinzugefügt. Hier sind seine Informationen:")
                print(mitarbeiter)
                
            else:
                print(f"Die gegebene Abteilung existiert nicht in dieser Firma.\n ")

    def mitarbeiter_entlassen(self, abteilung, *mitarbeitern): # Hier entlässt man ein Mitarbeiter von der Firma.
        for mitarbeiter in mitarbeitern:
            if abteilung in self.abteilungsliste:
                abteilung.list.remove(mitarbeiter)
            else:
                print(f"Die gegebene Abteilung existiert nicht in dieser Firma.\n ")

    def abteilungskosten(self, abteilung): # Hier wird die gesamte Kosten der Abteilung berechnet d.ß man berechnet das gesamte Summe von Geld,um die arbeiter zu bezahlen.
        total = 0
        for mitarbeiter in abteilung.list:
            total += mitarbeiter.gehalt
        print(f"Die \"{abteilung.name}\" gibt pro Monat {total}€ aus.\n")

    def get_alle_mitarbeiter(self,abteilung): # Hier wird eine liste von allen Mitarbeitern einer Abteilung in einer Tabelle angezeigt
        print(f"Liste von allen Mitarbeitern der \"{abteilung.name}\" Abteilung:")
        print(tabulate(abteilung.list, headers = ["NAMEN","GEHÄLTER"], tablefmt = "grid"))