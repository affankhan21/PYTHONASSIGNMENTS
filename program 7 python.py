import re
def tetrm(text):
   pattern='\Bz\B'
   if re.search(pattern,text):
      print("MATCH FOUND")
   else:
        print("MATCH NOT FOUND")

    
tetrm("we saw a  chimpanzee in the jungle")
tetrm("we saw a  tigers in the jungle")
tetrm("we saw a  beza sin the jungle")

