class InvalidPassword(Exception):
    pass
def verifypassword(pswd):
    if str(pswd)!="abc":
        raise InvalidPassword
    else:
        print('Valid Password:'+str(pswd))
verifypassword("abc")
verifypassword("xyz")
verifypassword("pqr")
    
