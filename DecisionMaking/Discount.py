amt=int(input("Enter purchase amount:"))
print("Purchase amount:",amt)
if amt>=5000:
   print("Final bill amt:",amt-amt*0.20)
elif amt>=3000 and amt<5000:
   print("Final bill amt:",amt-amt*0.10)
else:
   print("Final bill amt:",amt)
