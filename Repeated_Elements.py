a=[1,2,2,45,6,7,8,11,1,0,34,1,45,45,2342,23434,3,342,2,223,4,5535,334]
c=0
dup=[]
for i in a:
    if i not in dup:
        dup.append(i)
    else:
        c+=1
        print("repeated ",i)
print(dup)
print(c)
