list_1=[1,2,3,4,5]
list_2=[5,6,7,8,9]
print(list_1)
print(list_2)


if len(list_1)==len(list_2):
    print("list are of same length")
else:
    print("List are not same length")


if sum(list_1)==sum(list_2):
    print("Sum of lists are same")
else:
    print("Sum of lists are not same")


a=[x for x in list_1 if x in list_2]
if len(a)<1:
    print("No common element")
else:
    print("common elements are:",a)
