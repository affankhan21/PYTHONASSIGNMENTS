num=int(input("enter number:"))
rev=0
temp=num
rev=rev*10+num%10
num=num//10
rev=rev*10+num%10
num=num//10
rev=rev*10+num%10
num=num//10
print("you entered the number:",temp)
print("reverse of 3 digit  is:",rev)
if(rev==temp):
    print(temp,"number is palindrome")
else:
      print(temp,"number is not palindrome")
