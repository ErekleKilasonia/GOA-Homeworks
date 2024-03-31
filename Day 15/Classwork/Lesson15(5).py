def print_value(numbers):
    min = numbers[0]
    max = numbers[0]
    for i in numbers:
        if i < min: 
            min = i
        elif i > max:
            max = i
    print(f"Max number is :{max} and Min numbers is : {min}")


my = [7,8,54,98,4]

print_value(my)

