import datetime

data = input("Enter the date (DD MM YYYY): ").split()
day = int(data[0])
month = int(data[1])
year = int(data[2])

date_obj = datetime.date(year, month, day)
print(date_obj.strftime("%A").upper())
