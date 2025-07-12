from prettytable import PrettyTable

table = PrettyTable(["Names","Companies","Salaries"], horizontal_align_char = "-" )
for i in range(2):
    name = input("Name: ")
    company = input("Company: ")
    salary = input("Salary in $: ")
    table.add_row([name,company,salary+str("$")])
    print("\n")

"""
table.add_row(["Aldin","X","English Language","15"])
table.add_row(["Bruce","X","Maths","12"])
table.add_row(["Aldin","X","Physic","13"])
table.add_row(["Aldin","X","Chemistry","15"])
"""

print(table)