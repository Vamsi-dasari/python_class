list1=["vamsi","ashok","GOPI"]
list2=[]

for i in range(len(list1)):
    name=list1[i]
    rev=""
    for j in range(len(name)-1,-1,-1):#(5,-1,-1)
        
        
        # print(name[j])
        rev=rev+name[j]
    list2.append(rev)
    print(list2)
    
        







