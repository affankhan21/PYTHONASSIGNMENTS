num=int(input("ENTER A THREE DIGIT NUMBER:"))
sum=0
temp=num
sum=sum+num%10
num=num//10
sum=sum+num%10
num=num//10
sum=sum+num%10
num=num//10
print("THREE DIGIT NUMBER IS :",temp)
print("SUM OF THREE DIGIT NUMBER IS :",sum)