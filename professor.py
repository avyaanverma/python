import random


def main():
    level = get_level()
    # x + y = 10

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(levl)
        value = input(f"{x} + {y} = ")
        for __ in range(3):
            if value == (x + y):
                break
            else:
                print("EEE")
                print(f"{x+y}")





def get_level():
    lev = None
    while True:
        try:
            lev = input("Level: ")
            if lev not in [1,2,3]:
                continue
        except ValueError:
            raise ValueError
        else:
            break
    return lev



def generate_integer(level):
    if level == 1:
        a = random.randint(1, 9)
    elif level == 2:
        a = random.randint(11, 99)
    elif level == 3:
        a = random.randint(100, 999)
    else:
        raise ValueError



if __name__ == "__main__":
    main()