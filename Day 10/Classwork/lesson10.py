age = int (input("Enter your age here: ")) #1

if age < 12:
    print("you are a child")
elif age >= 12 and age <18:
    print("You are a teenager")
elif age >= 18 and age < 60:
    print("You are an adult")
else:
    print("You are old")



list = ["Maze Runner", "Prison break", "Kung Fu Panda", "Thor Ragnarok"]  #2
print(list)
print(list[1])