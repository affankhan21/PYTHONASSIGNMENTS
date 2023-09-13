amt=int(input("ENTER THE AMOUNT IN RS: "))
n=0
n+=amt//2000
amt=amt%2000
n1=n+amt//500
amt=amt%500
n2=n1+amt//200
amt=amt%200
n3=n2+amt//100
amt=amt%100
n4=n3+amt//50
amt=amt%50
n5=n4+amt//20
amt=amt%20
n6=n5+amt//10
amt=amt%10
n7=n6+amt//5
amt=amt%5
n8=n+n1+n2+n3+n4+n5+n6+n7
print("total notes:",n8)
print("2000 :",n)
print("500 :",n1)
print("200 :",n2)
print("100 :",n3)
print("50 :",n4)
print("20 :",n5)
print("10 :",n6)
print("5 :",n7)