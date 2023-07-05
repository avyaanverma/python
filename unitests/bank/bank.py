def main():
    user = input("Greeting: ")
    print(f"${value(user)}")
def value(greeting):
    greeting = greeting.strip().lower()
    if greeting[0:5] == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()