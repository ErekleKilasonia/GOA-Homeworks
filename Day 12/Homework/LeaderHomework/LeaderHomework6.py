#მომხმარებელს შემოატანინეთ ორი რიცხვი. შემდეგ მათ შორის უმცირესი for ციკლში საწყის, ხოლო უდიდესი საბოლ
#ოო მნიშვნელობად გამოიყენეთ. ციკლში იტერაცია მოახდინეთ ერთით და გამოიტანეთ საიტერაციო ცვლადის მესამე ხარისხი (კუბი).


num1 = int(input("Enter first number here: "))
num2 = int(input("Enter second number here: "))

first_num = min(num1, num2)
second_num = max(num1, num2)

for i in range(first_num, second_num):
    print(i ** 3)
