list=[3,2,9,10,43,7,20,3,17,23,37]
print("list=",list)
l=[]
print(" prime numbers of the list are")
for a in list:
    if(a%2==0):
     print("number is not prime")
    else:
      l.append(a)
      print(l)
