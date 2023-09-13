i=int(input("enter emp no  "))
while i>10:

 print("employee should be between 1 to 10")
 break
else:
 working_hours=int(input("working hours   "))
 if(working_hours>40):
  overtime=working_hours-40
                   
  overpay=overtime*12
  print( "employee no", i, "overtime"  ,"is","RS",overpay)
 else: 
     print(" you have to work for 40 hours to get o vertime ")
