sales=[58,39,54,47,41,38,56,64,69,62,42,46,57,60,51,50,35,44,45,65,59,36,55,63,40,48,52,37,61,43]

#distant apart:

max1=max(sales)
print("first max:",max1)
max_pos1=sales.index(max1)
sales.remove(max(sales))
max2=max(sales)
print("second max",max2)
max_pos2=sales.index(max2)

days=abs(max_pos1-max_pos2)
print(days)