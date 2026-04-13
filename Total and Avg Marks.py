m1=int(input("Enter mark1:"))
m2=int(input("Enter mark2:"))
m3=int(input("Enter mark3:"))
if((m1 >=0 and m1 <=100) and (m2>=0 and m2<=100) and (m3>=0 and m3<=100)) :
   total=m1+m2+m3
   avg=total/3
   print("Total marks:",total)
   print("Average marks:",avg)
else:
   print("Enter valid marks 0<= marks <=100")
