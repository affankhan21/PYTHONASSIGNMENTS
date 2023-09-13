print("----------TICKET FARE----------------")
sum1=0
sum2=0
sum3=0
sum4 =0
sum5=0

a1=int(input("Enter age: "))
tamt=int(input("Enter amount : "))
a2=int(input("Enter age: "))
tamt=int(input("Enter amount : "))
a3=int(input("Enter age: "))
tamt=int(input("Enter amount : "))
a4=int(input("Enter age: "))
tamt=int(input("Enter amount : "))
a5=int(input("Enter age: "))
tamt=int(input("Enter amount : "))
if(a1<12):
    famt=tamt*30/100
   
    sum1=famt
elif(a1>59):
    famt=tamt*50/100
    sum1=sum1+famt 
else:
    famt =tamt
    sum1=sum1+ famt 
if(a2<12):
    famt=tamt*30/100
   
    sum2=famt
elif(a2>59):
    famt=tamt*50/100
    sum2=sum2+famt 
else:
    famt =tamt
    sum2=sum2+ famt  
if(a3<12):
    famt=tamt*30/100
    
    sum3=famt
elif(a3>59):
    famt=tamt*50/100
    sum3=sum3+famt 
else:
    famt =tamt
    sum3=sum3+ famt  
if(a4<12):
    famt=tamt*30/100
    
    sum4=famt
elif(a4>59):
    famt=tamt*50/100
    sum4=sum4+famt 
else:
    famt =tamt
    sum4=sum4+ famt 
if(a5<12):
    famt=tamt*30/100

    sum5=famt
elif(a5>59):
    famt=tamt*50/100
    sum5=sum5+famt 
else:
    famt =tamt
    sum5=sum5+ famt  
sumt=sum1+sum2+sum3+sum4+sum5        
print("final amt is:",sumt)