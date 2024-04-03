def all(functions):

    item = functions.upper()
    item2 = functions.lower()
    item3 = functions.find("l")
    item4 = functions.capitalize()

    return str(item) + " " + str(item2)  + " " + str(item3)  + " " + str(item4)



sentence = "hello"
print(all(sentence))