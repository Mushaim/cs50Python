def calculate(mass):
    return mass * (300000000 ** 2)

def main():
    mass = int(input("m: "))
    print("E: ", calculate(mass))

main()