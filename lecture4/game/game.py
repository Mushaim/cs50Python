import random

def main():
    while True:
        try:
            range = int(input("Level: "))
            if range > 0:
                guess_number(range)
                break
            else:
                continue
        except ValueError:
            continue


def guess_number(r):
    random_int = random.randint(0,r)
    while True:
        guess = input("Guess: ")
        if not guess.isdecimal() or int(guess) <= 0:
            continue
        elif int(guess) == random_int:
            print("Just right!")
            break
        elif int(guess) > random_int:
            print(" Too large!")
        else:
            print("Too small!")

main()
