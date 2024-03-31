def listn(nums):
    num = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            num = num + nums[i]
    return num
print(listn([1,2,3,4,5]))