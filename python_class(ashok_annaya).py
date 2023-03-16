'''
j=0
a = 0 
b = 1

for i in range(20):
    c = a+b
    a,b = b,c
    
    j=j+1
    if j==10:
        print(c)
'''        
# git clone https://github.com/Vamsi-dasari/python_class.git
# git add .
# git commit -m "message/name"
# git push


cur_str = 'ashok sai ram'
rev = '' # ashok ias ram

for i in range(6,-5 , -1):
    print(i)
    rev = rev + cur_str[i]

print(rev)