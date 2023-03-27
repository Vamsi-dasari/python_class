
str=input("enter string 1")
str2=input("enter string 2")
str_list=[]
str2_list=[]
str_list=list(str)
str2_list=list(str2)
not_matched=[]
count=0
for i in range(len(str)):
    
    for j in range(len(str2)):
        if str2_list[i]=="@":#just to identify what letters did not match
               not_matched.append(str2_list[i])
               
        
        if str_list[i]==str2_list[j]:#main
            print(i,str_list[i],j,str2_list[j])
            count=count+1
            str2_list[j]="@"
        
print(str2_list)  
if str2_list[0:(len(str2_list))]=="@":
       pass
               
                   
else: 
        not_matched.append(str2_list[i])    
if count==len(str):
            
        
            print("true")
else:
            
            print("false",not_matched,"these letters did not match");
