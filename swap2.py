a=int(input("ENTER A NUMBER:"))
b=int(input("ENTER A NUMBER:"))
print("-------BEFORE SWAPPING---------------")
print("The value of a is:",a)
print("The value of b is:",b)
a=a+b
b=a-b
a=a-b
print("-------AFTER SWAPPING---------------")
print("The value of a is:",a)
print("The value of b is:",b)