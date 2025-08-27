def main():
    word = input()
    shorten(word)


def shorten(word):
    res = ""
    vowel = "aeiouAEIOU"
    for w in word:
        if w not in vowel:
            res +=w
    return res


if __name__ == "__main__":
    main()
