lis=[]
length=[]
for x in range(0,4):
    word=input("enter the word=")
    lis.append(word)
    length.append(len(word))
print(lis)
print("length of longest word=",max(length))
