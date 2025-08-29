import sys


if len(sys.argv) == 1:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

count = 0

if sys.argv[1].endswith(".py"):
    try:
        with open(sys.argv[1],"r") as file:
            for line in file:
                if line.strip().startswith("#"):
                    continue
                elif line.strip() == "":
                     continue
                else:
                    count += 1

    except FileNotFoundError:
        sys.exit("File not found")
else:
    sys.exit("Not valid extension")

print(count)
