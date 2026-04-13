bp=int(input("Enter basic salary:"))
if(bp>=5000 and bp<=50000):
        hra=bp*0.20
        da=bp*0.10
        print("Gross salary:",bp+hra+da)
else:
   print("please enter valid salary...")
