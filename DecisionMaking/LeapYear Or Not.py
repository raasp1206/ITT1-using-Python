year=int(input("Enter a year:"))
res="Leap year"if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) else "Not a leap year"
print(res)
