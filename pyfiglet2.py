import sys
import pyfiglet
from pyfiglet import Figlet

figlet = Figlet()
try:
    if len(sys.argv) == 1:
        print(pyfiglet.figlet_format(input("Input: ")))
    elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
        if sys.argv[2] in figlet.getFonts():
            print(pyfiglet.figlet_format(input("Input: "), font = sys.argv[2]))
    else:
        print("Invalid usage")
except EOFError:
    sys.exit("Invalid usage")

