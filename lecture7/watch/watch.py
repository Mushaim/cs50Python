import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'^<iframe.*src="https?://(www\.)?youtube\.com/embed/([0-9a-zA-Z-_]+)"',s)
    if match:
        return f"https://youtu.be/{match.group(2)}"
    return None


if __name__ == "__main__":
    main()
