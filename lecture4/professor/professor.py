import random


def main():
    level = get_level()
    right = 0
    for i in range(10):
        x = generate_integer(level)
        y= generate_integer(level)
        for j in range(3):
            print(f"{x} + {y} = ",end="")
            ans = input()
            if j == 2 and (not ans.isdecimal() or int(ans) != x+y):
                print(f"{x} + {y} =",x+y)
            elif not ans.isdecimal():
                print("EEE")
            elif int(ans) != x+y:
                print("EEE")
            else:
                right +=1
                break

    print("Correct = ", right)

def get_level():
    while True:
        level = input("Level: ")
        if not level.isdecimal() or int(level) > 3 or int(level) < 1:
            continue
        else:
            return int(level)


def generate_integer(level):
    a = 0
    b = 0
    if level == 1:
        a = 0
        b=9
    elif level == 2:
        a=10
        b=99
    else:
        a=100
        b=999
    x= random.randint(a,b)
    return x


if __name__ == "__main__":
    main()
