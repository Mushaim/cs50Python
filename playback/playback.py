def replace_space(input):
    return input.replace(" ","...")

def main():
    word = input()
    print(replace_space(word))

main()