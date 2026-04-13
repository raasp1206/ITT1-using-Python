bal=10000
amt=float(input("Enter amount to withdraw:"))
if((amt<=bal and amt>0) and amt%100==0):
   print("Withdrawl is possible")
else:
   print("Withdrawl is not possible")
