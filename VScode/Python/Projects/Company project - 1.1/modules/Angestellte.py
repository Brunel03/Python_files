import string
import datetime
import random

benutzte_Matrikel = set()
class Employee():
    def __init__(self,vorname,nachname,geburtsdatum,geburtsort,gehalt,Matrikel=None):
        self.vorname = string.capwords(vorname, sep =" ")
        self.nachname = string.capwords(nachname, sep =" ")
        self.geburtsdatum = datetime.datetime.strptime(geburtsdatum, "%d/%m/%Y").date()
        self.geburtsort = string.capwords(geburtsort, sep =" ")
        self.gehalt = gehalt
        if Matrikel is None:
            self.Matrikel = self.generate_Matrikel()
        else:
            self.Matrikel = Matrikel

    def __str__(self):
        return f"Matrikel: {self.Matrikel}\nVorname: {self.vorname}\nNachname: {self.nachname}\nGeburtsdatum: {self.geburtsdatum}\nGeburtsort: {self.geburtsort}\nGehalt: {self.gehalt}"
    
    def __iter__(self):
        yield self.Matrikel
        yield self.vorname
        yield self.nachname
        yield self.geburtsdatum
        yield self.geburtsort
        yield self.gehalt

    def __getitem__(self,index):
        if index == 0:
            return self.Matrikel
        elif index == 1:
            return self.vorname
        elif index == 2:
            return self.nachname
        elif index == 3:
            return self.geburtsdatum
        elif index == 4:
            return self.geburtsort
        elif index == 5:
            return self.gehalt
        
    def generate_Matrikel(self):
        global benutzte_Matrikel
        letters = string.ascii_uppercase
        while True:
            matrikelnummer = ''.join(random.choice(letters) for i in range(2)) +'-'+ ''.join(random.choice('0123456789') for i in range(4))
            if matrikelnummer not in benutzte_Matrikel:
                benutzte_Matrikel.add(matrikelnummer)
                return matrikelnummer