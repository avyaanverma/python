import random
def main():
    correct = 0
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)

        for __ in range(3):
            value = int(input(f"{x} + {y} = "))
            if value == (x + y):
                correct += 1
                break
            elif __ == 2:
                print(f"{x + y}")
            else:
                print("EEE")
        print(f"Score: {correct}")
def get_level():
    lev = None
    while True:
        try:
            lev = int(input("Level: "))
            if lev not in [1,2,3]:
                continue
        except ValueError:
            continue
        else:
            break
    return lev
def generate_integer(level):
    if level == 1:
        a = random.randint(0, 9)
    elif level == 2:
        a = random.randint(10, 99)
    elif level == 3:
        a = random.randint(100, 999)
    else:
        raise ValueError
    return a
#
#


if __name__ == "__main__":
    main()