num=int(input("ENTER A THREE DIGIT NUMBER:"))
rev=0
temp=num
rev=rev*10+num%10
num=num//10
rev=rev*10+num%10
num=num//10
rev=rev*10+num%10
num=num//10
print("THREE DIGIT NUMBER IS :",temp)
print("REVERSE OF  THREE DIGIT NUMBER IS :",rev)