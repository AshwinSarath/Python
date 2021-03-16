file_obj=open(r"D:\summary31aug.txt")
file_reader=file_obj.read()
print(file_reader)

ret=''
skipper=0
throw=[]

for tester in file_reader:
    if tester=="(":
        skipper+=1
        throw.append(tester)
        continue    
    elif tester==")":
        skipper-=1
        throw.append(tester)
        continue   
    elif skipper==0:
        ret+=tester

print(ret)
print(len(throw))
file_obj.close()
#program to remove to parenthesis

