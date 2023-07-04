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

    if user[2] == '/':
        date, month, year = user.split("/")
        date = int(date)
        month = int(month)
        year = int(year)

        if date > 30 or month > 12:
                continue
            if int(month) < 10:
                 month="0"+month
        else:
            month, datyea = user.split(" ")
            date,year = datyea.split(",")

            year = greg.index(year.title())+1
            if month.title()  not in greg:
                continue

    except EOFError:
            continue
       else:
        break

print(f"{year}-{month}-{date}")
