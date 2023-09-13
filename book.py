cp=float(input("ENTER AMOUNT OF BOOK:"))
if(cp>=1000):
    disc=cp*25/100
    sp=cp-disc
else:
    disc=cp*5/100
    sp=cp-disc 
print("Cost price of book is :",cp,"Rs")
print("Discount  on book is :",disc,"Rs")
print("Selling  price of book is :",sp,"Rs")
