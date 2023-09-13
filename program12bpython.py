import numpy as np
a=np.array([1,2,3,6,7,8,9,4,5,4,4])
b=np.where(a==4)
print(b)
c=np.searchsorted(a,8.8)
print(c)
