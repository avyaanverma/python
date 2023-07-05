def main():
    greg = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            user = input("Date: ")

            if '/' in user:
                date, month, year = user.split("/")
                if int(date) > 30 or int(month) > 12:
                    continue
                if int(month) < 10:
                    month="0"+month
            elif ',' in user:
                month,date, year = user.split(" ")
                date = date[0]
                date = int(date)
                year = int(year)
                if month.title()  not in greg:
                    continue
                month = greg.index(month.title()) + 1
        except EOFError:
            continue
        else:
            print(f"{year}-{month}-{date}")
            break


if __name__=="__main__":
    main()