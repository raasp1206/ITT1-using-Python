a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))
if (a+b > c) and (b+c > a) and (a+c > b):
    print("The three sides form a valid triangle.")
else:
    print("The three sides do not form a valid triangle.")
