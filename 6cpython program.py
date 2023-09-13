import re
s="https://www.google.com"
ob1=re.findall('(\w+)://',s)
print(ob1)
ob2=re.findall('://www.([\w+\-\.]+)',s)
print(ob2)
