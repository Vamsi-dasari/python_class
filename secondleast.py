a = [-1,-20,-3,4,5,6,2,-2]


m1 = a[0] # 3 # least of the list
m2 = a[1] # 1 # second least

if (m1 > m2):
    m1,m2 = m2,m1 # 1 , # 3  # 2

for i in range(2,len(a)): # 2

    if (a[i] < m1): # 2 < m1 (1)
        m2 = m1
        m1 = a[i]
          #  2  < 3
    elif (a[i] < m2): 
        m2 = a[i] # 2

print(m2)
afs-bthm-ppc