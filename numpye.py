import numpy as np
import time

#edureka
a=np.array([1,2,3])#always array performance has to  be np.array
b=np.array([3,4,5])
res=a+b
print(res)
print(a[1])

print("***************************")

q=np.array([(1,2,3,4),(5,6,7,3),(3,4,5,9)])
print(q)
print(q.max())
print(q[0:,3])
print(q[0:1,2])
print("********************")

w=np.array([(1,2,3),(9,6,3)])
r=np.array([(2,3,4),(5,6,7)])
print(w.sum(axis=0)) #adding coloum elements
print(w.sum(axis=1))#adding row elements
print(np.sqrt(w))
print(np.hstack(r))
print(np.vstack(r))
print(w.ravel())#concatenating n dimmensional as single dim array
print("****************************")
#simpliearn numpy part 2
g=np.arange(10).reshape(5,2)
print(g)
print("FLATTERN METHODS",g.flatten())
#print(g.flattern(order="F"))  #alsp "C" 
#print(g.flattern(order="C"))
print("*********************")
re=np.arange(8).reshape(2,4)
print(re)
fi=re.reshape(2,2,2)
print("RESHAPE",fi)
print("TRANSPOSE",fi.transpose())
print("ROLLAXIS",np.rollaxis(fi,2))
for x in np.nditer(fi):
 print(x)
 print(np.split(re,2))
 print("SHAPED",re.shape)

