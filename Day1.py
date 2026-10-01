## Day 1: Problems Based on:
# * Variables
# * Data types
# * Input/Output
# * Operations

# Program 1 — Personal information
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# city = input("Enter your city: ")

# print(f"I am {name} i am {age} year old and I live in {city}")


#Program 2 — Add two numbers
# num1 = int(input("Enter num 1: "))
# num2 = int(input("Enter num 2: "))

# sum = num1 + num2
# print(f"Sum = {sum}")


#Program 3 — Basic calculator
# num1 = int(input("Enter num 1: "))
# num2 = int(input("Enter num 2: "))

# print(f"Addition = {num1 + num2}")
# print(f"Subtraction = {num1 - num2}")
# print(f"Multiplication = {num1 * num2}")
# print(f"Division = {num1 / num2}")
# print(f"Modulus = {num1 % num2}")


#Program 4 — Rectangle
# height = int(input("Enter height: "))
# width = int(input("Enter width: "))

# area = height * width
# perimeter = 2 * (height * width)
# print(f"Area = {area}")
# print(f"Perimeter = {perimeter}")


#Program 5 — Average of 3 numbers
# a = int(input("Enter num1: "))
# b = int(input("Enter num2: "))
# c = int(input("Enter num3: "))

# print(f"Sum = {a+b+c}")
# print(f"Average = {(a+b+c)/3}")


#print cube and square
# a = int(input("Enter Num: "))
# square = a**2
# cube = a**3
# print(f"Square = {square}")
# print(f"Cube = {cube}")


#Take the user's age and print the age after 5 years.
# currnt_age = int(input("Enter Current age: "))
# after_age = currnt_age + 5

# print(f"After 5 years age will be {after_age}")


#Problem 6 — Circle
# pi = 3.14159
# radius = int(input("Enter radius: "))
# area = pi * radius * radius
# circum = 2* pi*radius
# print(f"Area = {area}")
# print(f"Circumference = {circum}")


#Simple Intrest
# Principle = int(input("Enter Principle amount: "))
# Rate = int(input("Enter rate: "))
# Time = int(input("Enter Time(Months): "))
# Sip = (Principle * Rate * Time)/ 100
# print(f"Intrest amount = {Sip}")
# print(f"Total amount = {Sip + Principle}")


#Temperature: Celsius as input Convert it to Fahrenheit.
# Cel = int(input("Enter Celsius: "))
# Fa = (Cel * 9/5) + 32
# print(f"Fahrenheit = {Fa}")


#Total and Average Marks
# s1 = int(input("Enter English marks: "))
# s2 = int(input("Enter Maths marks: "))
# s3 = int(input("Enter Science marks: "))
# s4 = int(input("Enter Python marks: "))
# s5 = int(input("Enter DBMS marks: "))
# s6 = int(input("Enter Java marks: "))

# Sum = s1+s2+s3+s4+s5+s6
# Avg = Sum/6
# print(f"Sum = {Sum} and Avg = {Avg}")


#Last Digit
# num = int(input("Enter num: "))
# f = len(str(num))
# print(f"Digits = {f}")
# div = 10 ** (f-1)
# last = num % 10
# first = num // div
# print(f"First Digit = {first}")
# print(f"Last Digit = {last}")
# print(f"Sum of First and Last Digit = {first + last}")


#Even true/false
# num = int(input("Enter num: "))
# even = num % 2 == 0
# print(even)


#Problem 12 — Reverse a 2-digit number
# num = int(input("Enter num: "))
# first = num // 10
# last = num % 10
# print(f"First Digit = {first}")
# print(f"Last Digit = {last}")
# print(f"Reverse Digit = {last *10 + first}")


#Problem 13 — Swap Two Numbers
# a = 10
# b = 20
# print(f"Before Swap a = {a} and b = {b}")
# a,b = b,a
# print(f"After Swap a = {a} and b = {b}")


#Problem 14 — Seconds Converter
# seconds = int(input("Enter Seconds: "))
# hour = seconds // 3600
# remain = seconds % 3600
# Mins = remain // 60
# second = remain % 60

# print(f"Hour = {hour}")
# print(f"Minutes = {Mins}")
# print(f"Seconds = {second}")


#Bill Calculator
# Price = int(input("Enter Food Price: "))
# Tax = Price * 5 / 100
# Tip = Price * 10 / 100
# Total_bill = Price + Tax + Tip
# print(f"Food Price: {Price}")
# print(f"Tax: {Tax}")
# print(f"Tip: {Tip}")
# print(f"Total Bill = {Total_bill}")