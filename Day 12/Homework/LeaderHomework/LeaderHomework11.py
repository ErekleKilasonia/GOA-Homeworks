weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metres: "))
BMI = weight / (height ** 2)
print(f"Your BMI is {round(weight / (height ** 2))}" )
if BMI <= 18.4:
    print("You are underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You are normal")
elif BMI >= 25 and BMI <= 39.9:
    print("You are overweight")
elif BMI >= 40:
    print("You are obese")
else:
    print("wrong weight and height")


