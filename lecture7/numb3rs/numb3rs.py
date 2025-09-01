import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        if "." in ip:
            parts = ip.split(".")
            for part in parts:
                if int(part) > 255 or int(part) < 0 or part == "":
                    return False
                if str(int(part)) != part:
                    return False

            if len(parts) != 4:
                return False
        else:
            return False
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
