import sys
from tabulate import tabulate
import csv

if len(sys.argv) == 1:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

table = []
if sys.argv[1].endswith(".csv"):
    try:
        with open(sys.argv[1],"r") as file:
            r = csv.reader(file)
            r = list(r)
            headers = r[0]
            for row in r[1:]:
                table.append(row)
            print(tabulate(table, headers, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File not found")
else:
    sys.exit("Not csv file")

