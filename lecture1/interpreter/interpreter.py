def main():
    expression = input("Expression: ")
    x,y,z = expression.split(" ")

    calculate(int(x),y,int(z))

def calculate(x,y,z):
    if y == "+":
        print(f"{(x+z):.1f}")
    elif y == "-":
        print(f"{(x-z):.1f}")
    elif y == "*":
        print(f"{(x*z):.1f}")
    else:
        print(f"{(x/z):.1f}")

main()