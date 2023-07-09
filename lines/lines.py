import sys

def main():
    while True:
        try:
            if len(sys.argv) > 2:
                sys.exit("Too many command-line arguments")
                break
            elif len(sys.argv) < 2:
                sys.exit("Not enough command-line arguments")
                break
            elif not (sys.argv[1].endswith(".py")):
                sys.exit("Not a Python file")
            else:
                break
        except FileNotFoundError:
            sys.exit("File does not exist")
            continue

    filepath = sys.argv[1]
    print(count_lines(filepath))


def count_lines(filepath):
    with open(filepath) as file:
        lines = file.readlines()
    counter = 0
    for line in lines:
        if line =='\n' or line[0] == '#' or line:
            continue
        counter += 1
    return counter

if __name__ == "__main__":
    main()
