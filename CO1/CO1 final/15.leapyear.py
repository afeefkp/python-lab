n = int(input("Enter a year(>2021): "))
if n <= 2021:
        print("invalid year")
for i in range(2021, n):
    if i % 4 ==0 :
            print(i)
    
