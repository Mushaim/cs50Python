def main():
    greeting = take_input()
    check_greeting(greeting)

def take_input():
    greeting = input("Greeting: ")
    return greeting

def check_greeting(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        print("$0",end="")
    elif greeting.startswith("h"):
        print("$20",end="")
    else:
        print("$100",end="")

main()