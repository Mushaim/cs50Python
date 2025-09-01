import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(r"^(\d{1,2})(?::(\d{1,2}))? (AM|PM) to (\d{1,2})(?::(\d{1,2}))? (AM|PM)$",s.strip())
    if not match:
        raise ValueError("Invalid Format")
    h1,m1,z1,h2,m2,z2  = match.groups()

    t1 = validate(int(h1),int(m1) if m1 else 0,z1)
    t2 = validate(int(h2),int(m2) if m2 else 0,z2)

    return f"{t1} to {t2}"

def validate(h,m,z):
    if not (0 < h <=12):
        raise ValueError("Invalid Hour")
    if not (0 <= m < 60):
        raise ValueError("Invalid minutes")

    if z == "AM":
        if h == 12:
            h = 0
    else:
        if h != 12:
            h +=12
    return f"{h:02}:{m:02}"


if __name__ == "__main__":
    main()
