import re
print("please enter password should be \n1)One capital letter/n2)Special character \n3)One number\n4)length should be 8-18:")
pswd=input(" ENTER PASSWORD:  ")
reg="^(?=.*[a-z])(?=.*[A-Z])(?=.\d)(?=.*[@$!%*#?&])[A-z\d@@$!%*#?&]{8,18}"
matchre = re.compile(reg)
res = re.search(matchre,pswd)
if res:
    print(" VALID PASSWORD")
else:
    print(" INVALID PASSWORD")
