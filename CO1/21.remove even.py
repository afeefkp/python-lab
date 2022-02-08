l=[0,1,2,3,4,5,-5,-4,-3,-2,-1]
print(l)

for i in l:
    if i%2==0:
        l.remove(i)
print(l)
