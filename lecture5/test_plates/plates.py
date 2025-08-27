def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # length should be in range of 2-6
    if 2 > len(s) or len(s) > 6:
        return False

    #first 2 digit should be alphabet
    if s[0:2].isdecimal():
        return False

    #no punctuation
    if not s.isalnum():
        return False

    #digit should not be in center
    for i in range(len(s)):
        c = s[i]
        if c.isdigit():
            if c == "0":
                return False
            elif s[i:].isdigit():
                return True
    return True

if __name__ == "__main__":
    main()
