import re
regex="^[a-z0-9]+[\.]?[a-z0-9]+[@]\w+[\.]\w{2,3}$"
def check(email):
    if(re.search(regex,email)):
        print("VALID EMAIL ADDRESS")
    else:
        print("NOT A VALID EMAIL ADDRESS")
    
email=input("Enter email: ")
check(email)
