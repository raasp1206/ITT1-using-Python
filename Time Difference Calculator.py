import datetime

time_str1 = input("Enter first timestamp (DD-MM-YYYY HH:MM:SS): ")
time_str2 = input("Enter second timestamp (DD-MM-YYYY HH:MM:SS): ")

time_format = "%d-%m-%Y %H:%M:%S"

time1 = datetime.datetime.strptime(time_str1, time_format)
time2 = datetime.datetime.strptime(time_str2, time_format)

diff = time2 - time1
result = abs(int(diff.total_seconds()))

print(result)
