n1=int(input("ENTER MARKS :"))
n2=int(input("ENTER MARKS :"))
n3=int(input("ENTER MARKS :"))
n4=int(input("ENTER MARKS :"))
n5=int(input("ENTER MARKS :"))
sum1=n1+n2+n3+n4+n5
perc=sum1/5
print("-------------------------------------------")
print("TOTAL MARKS IS :",500)
print("YOUR  MARKS IS: ",sum1)
print("YOUR PERCENTAGE IS: ",perc)
if(perc>=75):
    print("FIRST CLASS WITH DISTINCTION")
elif(perc>=65):
    print("FIRST CLASS")  
elif(perc>=55):
    print("SECOND  CLASS ")  
elif(perc>=40):
    print("PASS")
elif(perc<40):
    print("FAIL")
else:
    print("INVALID NUMBER")     
print("-------------------------------------------")         
