from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
figfonts = figlet.getFonts()week

if len(sys.argv) != 3 and len(sys.argv) != 1:
    sys.exit("Arguments error")
elif len(sys.argv) == 1:
    #use a random font
    sentence = input("Input: ")
    random.seed()
    figlet.setFont(font = random.choice(figfonts))
    print(figlet.renderText(sentence))
elif len(sys.argv) == 3:
    if sys.argv[1] == "-f" and sys.argv[2] in figfonts or sys.argv[1] == "--font" and sys.argv[2] in figfonts:
        sentence = input("Input: ")
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(sentence))
    else:
        sys.exit("Arguments incorrect")
