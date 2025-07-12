
#help("mathplotlib")

import csv
data = []
with open(r"C:\Users\amour\Desktop\Python\Kursmaterialen\Kursmaterialien\data\names.csv", newline='') as file:
    csv_file = csv.reader(file, delimiter=",", quotechar='"')

    counter = 0
    for line in csv_file:
        """
        if line[1] == "Name":
            continue
        #print(line)
        """
        """
        if counter != 0:
            data.append(line[1])
        counter += 1  
        """

    occ = 0
    if line[1] == "Name":
        occ += 1
    print(f"There are {occ} \'Name\' in the  list.")
    """
    names = set(data)
    
    print(f"{len(names)} names are registered here.")
    """