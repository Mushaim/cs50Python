from datetime import date,datetime
import inflect
import sys
p = inflect.engine()

def main():
    b_day = input("Date of birth: ")
    print(get_age(b_day))


def get_age(b_day):
    try:
        year,month,day = b_day.split("-")
        day = date(int(year),int(month),int(day))
        today = date.today()
        delta = today - day
        mins = delta.days * 24 * 60
        return f"{p.number_to_words(mins,andword= "").capitalize()} minutes"
    except ValueError:
        sys.exit("Invalid date")




if __name__ == "__main__":
    main()
