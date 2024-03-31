# შექმენით ფუნქცია, რომელიც მიიღებს არგუმენტად სიას და დაბეჭდეთ სიის რიცხვების ჯამი, არ გამოიყენოთ sum.
def sum(num):
    sum1 = 0
    for i in num:
        sum1 =sum1 + i
    print("Sum of all numbers in the list is", sum1)


list = [1,2,3,4,5,6,9,76]
sum(list)