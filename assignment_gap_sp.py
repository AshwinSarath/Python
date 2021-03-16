a=[7,3,9,0,4,8,2,5,1,6]
contain=[]
pos=[]
count=0
for i in range(len(a)-1):
   gap=a.index(i)-a.index(i+1)
   contain.append(gap)
   count+=1
   pos.append(count)
for index in contain:
    max_num=max(contain)
for count_num in  pos:
    element=(contain.index(max_num))
print("the gap",element,"and",element+1,"is",max_num)
print("Maximum gap of ",max_num,"occurs between",element,"and",element+1)





