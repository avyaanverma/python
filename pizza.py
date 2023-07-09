import sys
from tabulate import tabulate


def main():
    while True:
        try:
            if len(sys.argv) > 2:
                sys.exit("Too many command-line arguments")

            elif len(sys.argv) < 2:
                sys.exit("Not enough command-line arguments")

            elif not (sys.argv[1].endswith(".csv")):
                sys.exit("Not a Python file")
            else:
                break
        except FileNotFoundError:
            sys.exit("File does not exist")
    with open(sys.argv[1]) as file:
        menu = csv.reader(file)
        print(tabulate(menu))

if __name__ == "__main__":
    main()