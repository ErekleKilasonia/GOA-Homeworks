num1 = int(input("Enter first number here: "))
num2 = int(input("Enter second number here: "))
sum = 0
if num1 % 2 == 0:
    for i in range(num1,num2 + 1,2):
        sum = sum + i
else:
    for i in range(num1 + 1,num2 + 1,2):
        sum = sum + i
print(sum)