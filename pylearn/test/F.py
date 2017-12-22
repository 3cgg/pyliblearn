
a=[1,2]
b=[4,5,6]
c=[9,8,7,44,98]
zipped=zip(a,b)

print(zipped)
for item in zipped :
    print(item)

zipped=zip(a,b,c)

print(zipped)
l=[]
for item in zipped :
    print(item)
    l.append(item)

print(l)

i1=[2,3,4]
i2=[1,2,3,4,5]

import numpy as np

inter=np.intersect1d(i1,i2)

print(inter)

