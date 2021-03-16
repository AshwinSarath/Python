#for  user input
A=[]

n=int(input("Enter number of elemts  "))#size of array

for x in range(0,n-1):
    entered=int(input())
    #enter values
    A.append(entered)#ENTERED BEING ADDED
    print(A)

print("typed array  ",A)
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[i] > A[j]:
                     
            t=A[i] 
            A[i]=A[j]
            A[j]=t

print("sorted  ",A)    

