sal=float(input("Enter salary:"))
if(sal<=250000):
   print("No tax")
elif(sal>250000 and sal<=500000):
   print("Tax amount:",sal*0.05)
elif(sal>500000 and sal<=1000000):
   print("Tax amount:",sal*0.10)
elif(sal>1000000):
   print("Tax amount:",sal*0.15)
else:
   print("Invalid salary entered")
