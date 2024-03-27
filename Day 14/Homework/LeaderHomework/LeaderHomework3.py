sent = input("Enter a sentence here: ")
sui = sent.split(" ")
list = []
for i in sui:
    new = i[::-1]
    list.append(new)
new = ' '.join(list)
print(new)

