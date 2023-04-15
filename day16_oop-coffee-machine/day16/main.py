from prettytable import PrettyTable


table = PrettyTable()

# calling methods works as calling functionse
table.add_column("City name", ["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
table.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
table.add_column("Safety", ["not safe" if x % 2 == 0 else "safe"
                            for x in [1295, 5905, 112, 1357, 2058, 1566, 5386]])
table.align = "l"  # calling attributes works as assigning values to variables
print(table)