a=[7,3,9,0,4,8,2,5,1,6]
o=[0,1,2,3,4,5,6,7,8,9]
m=[]
n=[]
for i in range(len(a)-1):
    gap= a.index(i)-a.index(i+1)  #returns the index of the element in [i]
    m.append(gap)
    print(i,i+1,abs(gap)-1)
l=max(m)
print(l)
