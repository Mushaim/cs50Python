def main():
    fuel = input()
    per = convert(fuel)
    print(gauge(per))


def convert(fraction):
    try:
        x,y = fraction.split("/")
        if y == "0":
            raise ZeroDivisionError("Denominator cannot  be zero")
        if float(x) > float(y) or not x.isdigit() or not y.isdigit():
            raise ValueError("Not Valid")
        return round((float(x)/float(y)) * 100)
    except ZeroDivisionError:
        raise ZeroDivisionError("Denominator cannot  be zero")
    except ValueError:
        raise ValueError("Not Valid")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
