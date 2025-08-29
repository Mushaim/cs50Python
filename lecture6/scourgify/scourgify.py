import sys
import csv

students = []

if len(sys.argv) != 3:
    sys.exit("Number of argument not correct")
else:
    try:
        with open(sys.argv[1]) as file:
            r = csv.DictReader(file)
            for row in r:
                last,first = row["name"].split(", ")
                students.append({"first":first,"last":last,"house":row["house"]})
    except FileNotFoundError:
        sys.exit("File not found")

try:
    with open(sys.argv[2],"w") as file:
        r = csv.DictWriter(file,fieldnames = ["first","last","house"])
        r.writeheader()
        for student in students:
            r.writerow({"first":student["first"],"last":student["last"],"house":student["house"]})
except Exception as e:
    sys.exit(f"Error writing in output file {e}")
