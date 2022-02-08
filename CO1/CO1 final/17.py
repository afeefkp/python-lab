list=[]
n=int(input('Enter number of elements of list '))
for i in range(0,n):
    element=int(input())
    list.append(element)
print('list=',list)

a=[x for x in list if x<=100]
b=['over' for x in list if x>100 ]
a.append(b)
print(a)













