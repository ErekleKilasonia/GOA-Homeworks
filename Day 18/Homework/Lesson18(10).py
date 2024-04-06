listn = []
listn1 = []
for i in range(5):  
    x = input("Enter a word here: ")
    listn.append(x)
operation = input("Enter what you want to join words with: ")
for i in listn:
    if listn.index(i) % 2 == 0:
        listn1.append(i)
    else:
        pass
print(operation.join(listn1))