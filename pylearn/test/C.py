import numpy as np


mp={1: {1: 3.0, 2: 4.0, 3: 3.5, 4: 5.0, 5: 3.0}, 2: {1: 3.0, 2: 4.0, 6: 2.0, 4: 3.0, 3: 2.0, 5: 3.0}, 3: {2: 3.5, 6: 3.0, 3: 2.5, 4: 4.0, 5: 4.5}, 4: {1: 2.5, 2: 3.5, 6: 3.0, 4: 3.5, 5: 3.0, 3: 2.5}, 5: {2: 4.5, 4: 4.0, 3: 1.0}, 6: {1: 3.0, 2: 3.5, 6: 1.5, 4: 5.0, 3: 3.5, 5: 3.0}, 7: {1: 2.5, 2: 3.0, 4: 3.5, 5: 4.0}}

print(mp)

k=list(mp.keys())

bk=np.asanyarray(k,dtype=np.int32)
bk.sort()

ak=np.asanyarray([1,3,4,2,8,6,5],dtype=np.int32)
ak.sort()


l=[1,2,3,5,8,100,3,88]
al=np.asanyarray(l)

al.sort()

print(l)
print(al)