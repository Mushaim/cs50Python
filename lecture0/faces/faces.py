def convert(input):
    return input.replace(":)","🙂").replace(":(","🙁")

def main():
    word = input()
    print(convert(word))

main()