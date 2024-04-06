str1 = input("Enter a word: ")
listn= []
lstn = []
for i in str1:
    listn.append(i)
    if listn.index(i) % 2 == 0:
        lstn.append(i.upper())
    elif listn.index(i) % 2 != 0:
        lstn.append(i.lower())
# if len(lstn) % 2 == 0:
#     lstn[-1] = lstn[-1].lower()
# else:
#     pass
print("".join(lstn))