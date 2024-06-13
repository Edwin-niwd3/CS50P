months = [
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
        date = input("Date: ")
        if date.find('/') != -1:
            month, day, year = date.split('/')
        else:
            if date.find(',') == -1:
                raise Exception
            month, day, year = date.split()
            day = day.replace(",", "")
            month = month.capitalize()
            month = months.index(month) + 1
        month = int(month)
        day = int(day)
        year = int(year)
        if day > 31 or month > 12:
            raise Exception
        print(year, "-", f"{month:02}", "-",f"{day:02}", sep = "")
        break
    except Exception:
        pass
