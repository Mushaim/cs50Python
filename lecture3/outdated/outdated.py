months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    while True:
        try:
            date = input("Date: ")
            if "/" in date:
                month,day,year = date.split("/")
                if in_number(int(month),int(day),int(year)):
                    print(f"{int(year)}-{int(month):02}-{int(day):02}",end="")
                    break
            elif " " in date and "," in date:
                month,year = date.split(",")
                month,day = month.split(" ")
                if in_words(month.strip(),int(day),int(year.strip())):
                    month = months.index(month.title()) + 1
                    print(f"{int(year)}-{int(month):02}-{int(day):02}",end="")
                    break
        except EOFError:
            break
        except ValueError:
            pass

def in_number(m,d,y):
    if 0 < d < 32 and 0 < m < 13:
        return True

def in_words(m,d,y):
    if 0 < d < 32 and m.title() in months:
        return True

main()
