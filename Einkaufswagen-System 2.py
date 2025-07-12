class Produkt:
    def __init__(self,name,preis,menge=1):
        self.name = name.lower().capitalize() # Hier wird jeder Name in Kleinbuchstaben und dann das erste buchstabe in Großbuchstabe geändert
        self.preis = preis
        self.menge = menge
        
    def __str__(self): 
        return f"Name: {self.name}\nPreis: {self.preis}€\nMenge: {self.menge}"

class Einkaufswagen:
    def __init__(self):
        self.einkaufsliste = []

    def produkt_hinzufügen(self,produkt):
        self.einkaufsliste.append(produkt) #Hier wird das Produkt in der Einkaufswagen hinzugefügt
        #print("Das Produkt wurde erfolgreich hinzugefügt. Hier sind die Informationen des Produkts: ")
        #print(f"Name: {produkt.name}\nPreis: {produkt.preis}€\nMenge: {produkt.menge}\n")

    def produkt_entfernen(self,*produkte):
        for produkt in produkte:
            if produkt in self.einkaufsliste:
                self.einkaufsliste.append(produkt) #Hier wird das Produkt in der Einkaufswagen entfernt
                print(f"Das Produkt {produkt.name} wurde erfolgreich entfernt.\n")
            else:
                print(f"Das Produkt {produkt.name} wurde nicht in dem Warenkorb hinzugefügt. Deswegen Können sie das nicht entfernen.\n")
    
class Kunde:
    def __init__(self,name):
        self.name = name.lower().capitalize()
        self.einkaufswagen = Einkaufswagen()    #Hier jede Kunde hat seine eigene Einkaufswagen Dieser befehl ermöglicht es: self.einkaufswagen = Einkaufswagen() 
        print(f"Willkommen bei uns Kunde \"{self.name}\".")

    def produkt_kaufen(self,*produkte):
        for produkt in produkte:
            self.einkaufswagen.produkt_hinzufügen(produkt)
            print("Das Produkt wurde erfolgreich gekauft. Hier sind die Informationen des Produkts: ")
            print(f"Name: {produkt.name}\nPreis: {produkt.preis}€\nMenge: {produkt.menge}\n")

    def gesamtkosten(self):
        kosten = 0
        for produkt in self.einkaufswagen.einkaufsliste:
            kosten += produkt.preis * produkt.menge
        print(f"Sie haben die folgenden Produkte gekauft: ")
        for element in self.einkaufswagen.einkaufsliste: 
            print(f"{element}\n")
        print(f"Insgesamt müssen Sie {kosten}€ bezahlen.\n")

    def warenkorb_anzeigen(self):
        if not self.einkaufswagen.einkaufsliste: #Hier wird überprüft ob der einkaufslite leer ist
            print("Leider ist Ihrer Warenkorb leer.\n")
        else:
            print(f"Ihre Warenkorb enthält diese Produkte: ")
            for element in self.einkaufswagen.einkaufsliste: 
                print(f"{element}\n")

    def warenkorb_leeren(self):
        self.einkaufswagen.einkaufsliste.clear()
        print("Ihre Einkaufswagen wurde geleert.","\n")  


#Beispiel der Nutzung des Systems
#hier werden Produkte erstellt. Sie sollen in diesem Format angegeben werden: Produkt("name des produkts",Einzelpreis,menge)
product1 = Produkt("Tisch",30.5,2)
product2 = Produkt("Brot",1,4)
product3 = Produkt("Smartphone",176.5,1)
product4 = Produkt("Laptop",450)
product5 = Produkt("T-shirt",23.99,2)

#hier wird einen Kunden erstellt
kunde1 = Kunde("freddy")
# produkt zum Warenkorb hinzufügen
kunde1.produkt_kaufen(product1,product4)
# Inhalt des Warenkorbs anzeigen
kunde1.warenkorb_anzeigen()
#Produkt aus dem Warenkorb entfernen
kunde1.einkaufswagen.produkt_entfernen(product3,product5,product2)
#Die Gesamtkosten des Kundes berechnen
kunde1.gesamtkosten()

kunde2 = Kunde("evans")
kunde2.produkt_kaufen(product3,product5)
kunde2.gesamtkosten()