import sys
import pyfiglet
import random

font_list = pyfiglet.FigletFont.getFonts()

if len(sys.argv) == 1:
    text = input("Input: ")
    print("Output: ")
    print(pyfiglet.figlet_format(text, random.choice(font_list)))

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"] and sys.argv[2] in font_list:
    text = input("Input: ")
    print("Output: ")
    print(pyfiglet.figlet_format(text, font = sys.argv[-1]))

else:
    sys.exit("Invalid usage")