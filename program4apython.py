import math
num=int(input("enter the no: "))
def isprime():
    a=2
    while a<=math.sqrt(num):
        if num%a<1:
            return"number is not prime "
        a=a+1
        return"number is prime"
print(isprime())
