## Day 2: Problems Based on:
# * If condition
# * If-else condition
# * If-elif condition
# * Nested if condition

#Problem 1 — Positive, Negative, or Zero
# num = int(input("Enter a number: "))

# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")


#Problem 2 — Greater of Two Numbers
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# if num1 > num2:
#     print(f"num1 is greater {num1}")
# elif num1 < num2:
#     print(f"num2 is greater {num2}")
# else:
#     print(f"Both are equal, num1 = {num1} and num2 = {num2}")


#Problem 3 — Greater of Three Numbers
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# num3 = int(input("Enter num3: "))
# if num1 >= num2 and num1 >= num3:
#     print(f"num1 is greater {num1}")
# elif num1 <= num2 and num3 <= num2:
#     print(f"num2 is greater {num2}")
# else:
#     print(f"num3 is greater {num3}")


#Problem 4 — Age Category
# age = int(input("Enter age: "))
# if age < 0:
#     print("Invalid age")
# elif age <= 12:
#     print(f"Child")
# elif 13 <= age <= 19:
#     print(f"Teenager")
# elif 20 <= age <= 59:
#     print(f"Adult")
# else:
#     print(f"Senior Citizen")


#Problem 5 — Divisible by 5
# num = int(input("Enter num: "))
# if num % 5 == 0:
#     print(f"Divisible by 5")
# else:
#     print(f"Not Divisible by 5")


#Problem 6 — Largest of Two
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# if num1 > num2:
#     print(f"num1 is greater {num1}")
# elif num1 < num2:
#     print(f"num2 is greater {num2}")
# else:
#     print(f"Both are equal, num1 = {num1} and num2 = {num2}")


#Problem 7 — Leap Year
# year = int(input("Enter the Year: "))
# if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
#     print("Leap Year")
# else:
#     print("Not Leap Year")


#Problem 8 — Grade Calculator Similar to Problem 4 — Age Category


#Problem 9 — Login System
# c_user = "ganeshk41"
# c_pass = "@123"
# user_name = input("Enter User name: ")
# user_pass = input("Enter Password: ")

# if c_user == user_name and c_pass == user_pass:
#     print(f"Login Successful")
# else:
#     print(f"Invalid User name or Password!")


#Problem 10 — Simple Calculator ⭐
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# operator = input("Enter Operator: ")

# if operator == "+":
#     print(num1 + num2)
# elif operator == "-":
#     print(num1 - num2)
# elif operator == "*":
#     print(num1 * num2)
# elif operator == "/":
#     print(num1 / num2)
# elif operator == "%":
#     print(num1 % num2)
# else:
#     print("invalid operator")


#Problem 11 — Electricity Bill
# units = int(input("Enter the units: "))
# price = None
# if units < 0:
#     print("Invalid units")
# elif units <= 100:
#     price = 2
# elif units <= 200:
#     price = 3
# elif units <= 300:
#     price = 5
# else:
#     price = 7

# bill = price * units
# print(bill)


#Problem 12 — Triangle
# a = int(input("Enter a value: "))
# b = int(input("Enter b value: "))
# c = int(input("Enter c value: "))

# if a > 0 and b > 0 and c > 0 and a + b + c == 180 :
#     print(f"Valid Triangle")
# else:
#     print(f"Invalid Triangle")


#Problem 13 — Triangle Type (I don't no the concept)
# a = int(input("Enter a value: "))
# b = int(input("Enter b value: "))
# c = int(input("Enter c value: "))
# if a == b == c:
#     print("Equilateral")
# elif a == b or b == c or a == c:
#     print("Isosceles")
# else:
#     print("Scalene")


#Problem 14 — Number in Range
# a = int(input("Enter a value: "))

# if 10 <= a <= 50:
#     print("inside range")
# else:
#     print("outside range")


#🔥 Problem 15 — ATM Challenge
# Balance = 10000
# withdraw = int(input("Enter Withdrawal Amount: "))

# if withdraw > 0:
#     if withdraw <= Balance:
#         print(f"Withdrawal Successful")
#         Balance = Balance - withdraw
#     else:
#         print(f"Insufficient Balance")
# else:
#     print(f"Invalid Amount")

# print(f"Remaining Balance = {Balance}")