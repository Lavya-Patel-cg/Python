
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

if month < 1 or month > 12:
    print("Invalid date")
elif day < 1 or day >31 :
    print("Invalid date")
else:
    is_leap_year = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    if month in (1, 3, 5, 7, 8, 10, 12):
        max_day = 31
    elif month == 2:
        if is_leap_year:
            max_day = 29
        else:
            max_day = 28
    else:
        max_day = 30

    if day <= max_day:
        print("Valid date")
    else:
        print("Invalid date")