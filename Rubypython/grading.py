#create a program that checks a students performance

marks = int(input("Enter your marks: "))

if 100 >= marks >= 80:
    print("You have an A")
elif 79 >= marks >= 60:
    print("You have a B")
elif 59 >= marks >= 40:
    print("You have a C")
elif 39 >= marks >= 0:
    print("You have failed")
else:
    print("Invalid Marks")


#Create a program that calculates BMI
weight=int(input("Enter your weight: "))
height=float(input("Enter your height in meters: "))
BMI=weight/height**2

if BMI<18.5:
    print("Underweight")
elif 18.5 <= BMI < 25:
    print("Normal")
elif 25 <= BMI < 30:
    print("Overweight")
else: print("Obeise")
