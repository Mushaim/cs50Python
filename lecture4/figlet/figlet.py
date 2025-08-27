from pyfiglet import Figlet
from random import choice
import sys

figlet = Figlet()

fonts = figlet.getFonts()

if len(sys.argv) == 3:
    if sys.argv[1].strip() == "-f" or sys.argv[1].strip() == "--font":
        if sys.argv[2] in fonts:
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Wrong font")
    else:
        sys.exit("Wrong format")
elif len(sys.argv) == 1:
    font = choice(fonts)
    figlet.setFont(font=font)
else:
    sys.exit("Invalid")

words = input("Input: ")
print(figlet.renderText(words))


