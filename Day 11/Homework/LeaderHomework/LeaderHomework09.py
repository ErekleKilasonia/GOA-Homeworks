num =  int(input("Enter a number: "))

if num % 2 == 0 and num % 3 == 0:
    print("Your number can be diveded by 2 and 3")
elif num % 2 == 0 and num % 3 != 0:
    print("Your number can only be divided by 2")
elif num % 3 == 0 and num % 2 != 0:
    print("Your number can only be divided by 3")
else:
    print("Your number can not be divided by 2 and 3")