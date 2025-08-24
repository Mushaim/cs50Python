def main():
    answer = take_input()
    check_answer(answer)

def take_input():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    return answer

def check_answer(answer):
    answer = answer.lower().strip()
    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")

main()