n=input("enter ")
s=len(n)
for i in range(s):
    if (n[i]!=n[s-1-i]):
        break
else:
    print("palindrome")


    

