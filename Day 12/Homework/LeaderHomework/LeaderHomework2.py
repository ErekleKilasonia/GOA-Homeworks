opinion = input("Enter what you want mile to km or km to mile: ")


if opinion == "km to mile":
    num1 = int(input("Enter how many km you want to convert to miles: "))
    print(f"{num1}km to miles is {num1 * 0.6}")

elif opinion == "mile to km":
    num2 = int(input("Enter how many miles you want to convert to km: "))
    print(f"{num2}miles to km is {num2 * 1.6}")
else:
    print("Wrong decision")















