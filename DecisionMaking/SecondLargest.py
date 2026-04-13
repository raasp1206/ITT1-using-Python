num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))
num3=int(input("Enter a number:"))
if(num1 >= num2 and num1 <= num3) or (num1 >= num3 and num1 <= num2):
        print("Second largest:",num1)
elif(num2 >= num1 and num2 <= num3) or (num2 >= num3 and num2 <= num1):
        print("Second largest:",num2)
else:
        print("Second largest:",num3)
