while True:
    try:
        fuel = input("Fraction :")
        x,y = fuel.split("/")
        x =  int(x)
        y = int(y)
        fuel = (x/y) * 100
        if fuel >= 0 and x <= y:
            break
    except (ValueError, ZeroDivisionError):
        pass

if fuel >= 99:
    print("F")
elif fuel <= 1:
    print("E")
else:
    print(round(fuel),"%",end="",sep="")

