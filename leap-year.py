# To get year (integer input) from the user
# This is my first explanation
yıl = int(input("Enter a year: "))

if (yıl % 4) == 0:
    if (year % 100) == 0:
        if (yıl % 400) == 0:
            print("{0} is a leap year".format(yıl))
        else:
            print("{0} is not a leap year".format(yıl))
    else:
        print("{0} is a leap year".format(yıl))
else:
    print("{0} is not a leap year".format(yıl))
