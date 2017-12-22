import numpy as np
a=np.asarray([1,2,np.nan,3])
b=np.asarray([4,5,6])
c=np.asarray([9,8,7,44,98])
d=np.asarray([9,0])

a1=a[~np.isnan(a)]

a2=a[np.isnan(a)]

b1=b[~np.isnan(a)]

b2=b[np.isnan(a)]

d2=d[np.isnan(a)]

print(a1)