word = input("Enter a word: ")
find = input("Enter a letter to find: ")
listn = []
for i in word:
    listn.append(i)
if find in listn:
    print(word.index(find))
else:
    print(-1)

    