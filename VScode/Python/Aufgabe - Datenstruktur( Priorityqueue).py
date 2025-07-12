
import queue
import csv
data = {}
with open(r"C:\Users\amour\Desktop\Python\Kursmaterialen\Kursmaterialien\data\names.csv", newline='') as file:
    csv_file = csv.reader(file, delimiter=",", quotechar='"')
    for line in csv_file:
        if line[5] == "Count":
            continue
            
        names = line[1]
        count = int(line[5])

        if names in data:     #Hier werden Alle Name in der Dictionary gespeichert, damit man die Häufigkeit jeder Namen zählt. 
            data[names] = data[names] + count
        else:
            data[names] = count
    print(data)
    print(data.get("Name"))
    
    Data = queue.PriorityQueue()  #Hier wird die Daten der Dictionary in der Warteschlange gespeichert mit einer bestimmten Sortierung.
    for name,count in data.items():
        Data.put((-count, name))
    for i in range(100):
        print(Data.get())
"""
import csv
with open(r"C:\Users\amour\Desktop\Python\Kursmaterialen\Kursmaterialien\data\astronauts.csv", newline='') as file:
    csv_file = csv.reader(file, delimiter=",", quotechar='"')
    for line in csv_file:
        print(line) 
"""   