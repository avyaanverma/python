def main():
    user = list(input("Input: "))
    print(shorten(user))


def shorten(word):
    newstr = ""
    for letter in word:
        if letter.lower() not in ['a','e','i','o','u']:
            newstr += letter

    return newstr

if __name__== "__main__":
    main()
