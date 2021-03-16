sample_space=["HHHH","HHHT","HHTH","HHTT","HTHH","HTHT","HTTH","HTTT","THHH","THHT","THTH","THTT","TTHH","TTHT","TTTH","TTTT"]
hcount=[]
for i in sample_space:
    count=i.count('H')
    hcount.append(count)
for i in range(5):
    print("p(x=",i,")",hcount.count(i))