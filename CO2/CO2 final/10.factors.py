n=int(input('enter a number'))
print(n)
print('factors of entered number are')
for i in range(1,n+1):
    if n%i==0:
        print(i)
