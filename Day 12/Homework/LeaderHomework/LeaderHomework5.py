num = int(input("Enter a number between 1 and 10: "))


if num > 10 or num < 1:
    print("you chose number incorectly")
else:
    print("evey number between 1 and 50 is multipled by your choosen number ")
    for i in range(50):
        print(i * num)
