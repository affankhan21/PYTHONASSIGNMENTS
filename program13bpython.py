import pandas as pd
s1=pd.Series([10,11,12])
s2=pd.Series([89.9,76.89,56.7])
s3=pd.Series(['vijay','deenanath','chauhan'])
data={'Roll no':s1,'Marks':s2,'Name':s3}
d=pd.DataFrame(data)
print(d)
import pandas as pdd
s4=pdd.Series([14,15,16])
s5=pdd.Series([34.5,61.6,90,`])
s6=pdd.Series(['bharat','ram','sharma'])
data={'Roll no':s4,'Marks':s5,'Name':s6}
e=pdd.DataFrame(data)
print(e)
