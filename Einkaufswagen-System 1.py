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
        print("Das Produkt wurde erfolgreich hinzugefügt. Hier sind die Informationen des Produkts: ")
        print(f"Name: {produkt.name}\nPreis: {produkt.preis}€\nMenge: {produkt.menge}\n")

    def produkt_entfernen(self,produkt):
        if produkt in self.einkaufsliste:
            self.einkaufsliste.append(produkt) #Hier wird das Produkt in der Einkaufswagen entfernt
            print(f"Das Produkt {produkt.name} wurde erfolgreich entfernt.\n")
        else:
            print(f"Das Produkt {produkt.name} wurde nicht in der Einkaufsliste hinzugefügt. Deswegen Können sie das nicht entfernen.\n")

    def warenkorb_anzeigen(self):
        print(f"Ihre Einkausliste enthält diese Produkte: ")
        for element in self.einkaufsliste: 
            print(f"{element}\n")

class Kunde:
    def __init__(self,name):
        self.name = name
        self.einkaufswagen = []

    def produkt_kaufen(self,produkt):
        self.einkaufswagen.append(produkt)
        print("Das Produkt wurde erfolgreich gekauft. Hier sind die Informationen des Produkts: ")
        print(f"Name: {produkt.name}\nPreis: {produkt.preis}€\nMenge: {produkt.menge}\n")

    def warenkorb_leeren(self,list):
        for element in list.einkaufsliste:
            list.einkaufsliste.clear()
        print("Jetzt ist Ihre Einkaufswagen leer.","\n")

product1 = Produkt("Tisch",30.5,2)
product2 = Produkt("Brot",1,4)
product3 = Produkt("Smartphone",176.5,1)

list = Einkaufswagen()
list.produkt_hinzufügen(product1)
list.produkt_hinzufügen(product3)
list.produkt_entfernen(product2)
list.warenkorb_anzeigen()