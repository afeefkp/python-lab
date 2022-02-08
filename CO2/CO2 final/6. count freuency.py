s=str(input('Enter the string:'))
d={x:s.count(x) for x in s}
print(d)
