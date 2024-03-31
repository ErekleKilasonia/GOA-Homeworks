def copy_join(listn):
    word = ""
    for i in listn:
        word = word +  i + " "
    return word
print(copy_join(["black", "banana", "apple", "pineapple", "orange"]))