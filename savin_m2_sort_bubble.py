# Module 2. Algorithms
# bubble methods
from random import randint

# ---  random list -------
n=100
a_unsort=[]
for i in range(n):
    a_unsort.append(randint(1,100))
print(a_unsort)
print("----------------------------\n")

# ------ Bubble sort var 1 ------
k=0             # number of operations
c=0             # number of cycles
a_sort=[]
a_sort.extend(a_unsort)

for i in range(n-1):
    for j in range(n-1):
        if a_sort[j]>a_sort[j+1]:
            a_sort[j],a_sort[j+1]=a_sort[j+1],a_sort[j]
            k+=1    # increase counters
        c+=1
print(a_sort)
print("Var 1. Number of operations: ",k," number of cycles: ",c)
print("----------------------------\n")

# ------ Bubble sort var 2 ------
k=0             # number of operations
c=0             # number of cycles
a_sort=[]
a_sort.extend(a_unsort)

for i in range(n-1):
    for j in range(n-1-i):        # update!
        if a_sort[j]>a_sort[j+1]:
            a_sort[j],a_sort[j+1]=a_sort[j+1],a_sort[j]
            k+=1    # increase counters
        c+=1 
print(a_sort)
print("Var 2. Number of operations: ",k," number of cycles: ",c)
print("----------------------------\n")
# ------ Bubble sort var 3 -----
k=0             # number of operations
c=0             # number of cycles
a_sort=[]
a_sort.extend(a_unsort)

for i in range(n-1):
    upd=0                           # update 2
    for j in range(n-1-i):          # update 1
        if a_sort[j]>a_sort[j+1]:
            a_sort[j],a_sort[j+1]=a_sort[j+1],a_sort[j]
            k+=1    # increase counters
            upd+=1
        c+=1
    if upd==0:      # if no changes
        break
print(a_sort)
print("Var 3. Number of operations: ",k," number of cycles: ",c)
