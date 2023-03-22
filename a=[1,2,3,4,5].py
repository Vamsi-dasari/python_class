a=[1,2,3,4,5]
min1=a[0]
min2=a[1] 

#  swap min1 with min2 if min1>min2 
if min1>min2:
    min1=min2
    min2=a[0]
for i in range(len(list)):
    if a[i]<min2:
        min2=a[i]
print(min2)