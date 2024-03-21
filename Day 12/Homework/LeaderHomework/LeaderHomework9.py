num1 =  float(input("Enter a first number here: "))
num2 =  float(input("Enter a seconf number here: "))
dec1 = input("what operation would you like + - / or *: ")

if dec1 == "+":
    print(num1 + num2)
elif dec1 == "-":
    print(num1 - num2)
elif dec1 == "*":
    print(num1 * num2)
elif dec1 == "/":
    print(num1 / num2)
else:
    print("You chose wrong operation")
