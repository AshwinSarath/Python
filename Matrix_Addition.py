a=[[1,4,5],[2,3,4],[10,5,0]]
b=[[3,3,3],[5,6,6],[50,6,1]]
sum=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a)):
        sum=a[i][j]+b[i][j]
        #print(sum,end=' ')
#s=list(zip(a,b))

t=[a[i][j]+b[i][j] for i in range(len(a)) for j in range(len(a))]
print(t)
#print(s)