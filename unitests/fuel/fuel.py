def main():
    user = input("Fraction: ")
    gfg = convert(user)
    print(gauge(gfg))

def convert(user):
    b,c = user.split("/")

    if int(c) == 0:
        raise ZeroDivisionError
    elif not (b.isdigit()) or int(b)>int(c)  or not (c.isdigit()):
        raise ValueError

    return int(int(b)/int(c) * 100)


def gauge(percentage):


    if 0 <= percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        return f"{int(percentage)}%"
if __name__ == "__main__":
    main()
