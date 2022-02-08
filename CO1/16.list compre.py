
l=[1,2,3,4,-1,-2,-3,-4]
positive=[x for x in l if x>0]
print('Positive numbers in the list ',positive)

n=int(input("Enter the limit: "))
square=[x*x for x in range(n+1)]
print('square of numbers ',square)


word=input("Enter a word: ")
vowels=["A","E","I","O","U","a","e","i","o","u"]
list_vowels=[x for x in word if x in vowels]
print('vowels in the entered word are ',list_vowels)


word=input("Enter a word: ")
list_ordinal=[ord(x) for x in word]
print(list_ordinal)
