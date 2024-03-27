def list(numbers):
    num = 0
    listn = []
    for i in numbers:
        if i >= 0:
            num += i
        else:
            listn.append(i)
    print(f"Lenght of negative numbers is {len(listn)}")

    print(f"Positive numbers sum is: {num} ")

    
    
    
    
mylist = [5,6,-3,8,-9]
list(mylist)