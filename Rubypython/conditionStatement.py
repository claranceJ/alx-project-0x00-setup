#Checking if a number is even or odd

# Numb = int(input("Enter your number: "))
#
# if Numb % 2 == 0:
#     print(f"{Numb} is an even Number")
# else:
#     print(f"{Numb} is an odd Number")

#A program that prints the largest of three numbers
num1=int(input("Enter the first Number: "))
num2=int(input("Enter the second Number: "))
num3=int(input("Enter the Third Number: "))

if num1>num2 and num1>num3:
    print(f"{num1} is the greatest")
elif num2>num1 and num2>num3:
    print(f"{num2} is the greatest")
elif num3>num1 and num3>num2:
    print(f"{num3} is the greatest")
else:
    print("They are all equal")

