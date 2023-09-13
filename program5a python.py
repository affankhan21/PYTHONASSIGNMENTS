class continent:
    def getcoun(self):
        self.cont=input("Enter name of the continent:  ")
        return self.cont
class country(continent):
    def getcou(self):
        self.contr=input("Enter name of the country:  ")       

class  state(country):
    def getst(self):
        self.sta=input("Enter name of the state:     ")
class  place(state):
    
    def getpl(self):
        self.pla=input("Enter name of the place:     ")
    def display(self): 
        print(self.coun)
        print(self.contr)
        print(self.sta)
        print(self.pla)
        
        
        


p=place()
p.getcoun()
p.getcou()
p.getst()
p.getpl()




