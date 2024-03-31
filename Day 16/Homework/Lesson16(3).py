def listn(nums):
    num = 0
    num1 = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            num = num + nums[i]
        elif i % 2 != 0:
            num1 = num1 + nums[i]
    return num,num1

list1 =  [1,2,3,4,5]
print(listn(list1))