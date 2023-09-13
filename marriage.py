gender=input("ENTER YOUR GENDER(male/female): ")
age=int(input("enter age :"))
if(gender=="MALE")or(gender=="male"):
    if(age>=21):
        print("you can marry")
    else:
        print("you cannot marry")    
elif(gender=="FEMALE")or(gender=="female"):
    if(age>=18):
        print("you can marry")
    else:
        print("you cannot marry")
else:
    print("INVALID SELECTION")            

