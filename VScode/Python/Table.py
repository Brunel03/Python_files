from prettytable import PrettyTable
from tabulate import tabulate

data = []
with open(r"C:\Users\amour\Desktop\Python\Kursmaterialen\Kursmaterialien\data\names.csv") as file:
    for line in file:
        line = line.strip().split(",")
        if line[5] == "Count":
            continue
                
        counts = int(line[5])
    
        if counts > 100 :
            data.append(line)
            
                
    """    
    table = PrettyTable(["ID", "NAMES", "YEARS","GENDERS","STATES","COUNTS"])
    for element in data:
        table.add_row(element)   
    print(table)
    """
    #for element in sorted(data, key = lambda x:x[5]):
        #print(tabulate(element, headers = ))
    
    print(tabulate(data, headers = ["ID", "NAMES", "YEARS","GENDERS","STATES","COUNTS"], tablefmt = "grid"))
