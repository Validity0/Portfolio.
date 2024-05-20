weight = input("What is your Weight in LB?")
while weight.isdecimal() == False: 
    print("Please write a number")
    weight = input("What is your Weight in LB?")

height = input("What is your Height in feet?")
while height.isdecimal() == False:
    print("Please write a number")
    height = input("What is your Height in feet?")

weight = float(weight)
height = float(height)

bmi = round(float((weight / (height * 12) ** 2) * 703), 1)
print("Your bmi is", bmi)

def averageBmi(bmi):
    match bmi:
        case bmi if bmi<18.5:
            print("You are Under Weight")
        case bmi if bmi>=18.5 and bmi<25:
            print("You are Normal Weight")
        case bmi if bmi>=25 and bmi<30:
            print("You are Over Weight")
        case bmi if bmi>=30 and bmi<35:
            print("You are Obese")
        case bmi if bmi>=35:
            print("You are Extremley Obese")

averageBmi(bmi)