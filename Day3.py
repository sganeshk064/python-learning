## Day 3: Problems Based on:
# * For Loops
# * While Loops
# * Nested Loops

#Problem 1 — Print 1 to 10
# for i in range (1,11):
#     print(i)


#Problem 2 — Print 10 to 1
# for i in range(10,0,-1):
#     print(i)


#Problem 3 — Even numbers
# for i in range(2,51,2):
#     print(i)
# Other Solution
# for i in range(1,51):
#     if i % 2 == 0:
#         print(i)


#Problem 4 — Odd numbers
# for i in range(1,51):
#     if i % 2 != 0:
#         print(i)


#Problem 5 — Multiplication table ⭐
# n = 5
# for i in range(1, 11):
#     print("5 * ",i,"=", 5*i)


#Problem 6 — Sum 1 to N
# n = 10
# sum = 0
# for i in range(n+1):
#     sum = sum + i
# print(sum)


#Problem 7 — Sum of even numbers
# n = 10
# sum = 0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         sum = sum + i
# print(sum)


#Problem 8 — Count digits ⭐
# n = 12345
# c = 0
# while n != 0:
#     n = n // 10
#     c += 1
# print(c)


#Problem 9 — Sum of digits ⭐
# n = 583
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum = sum + digit
#     n = n // 10
# print(sum)


#Problem 10 — Reverse a number ⭐⭐
# n = 583
# rev = 0
# while n > 0:
#     digit = n % 10 # 3
#     n = n // 10 # 58
#     rev = rev * 10 + digit
# print(rev)


#Problem 11 — Count even and odd digits
# n = 12345
# even = 0
# odd = 0

# while n > 0:
#     digit = n % 10
#     n = n // 10
#     if digit % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(f"Even = {even} and Odd = {odd}")


#Problem 12 — Factorial ⭐
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(fact)


# #Problem 13 — Check prime number ⭐⭐///////////////////////////
# n = 8
# if n <= 2:
#     print("Not Prime")
# else:  
#     for i in range(2,n):
#         if n % i == 0:
#             print("Not Prime")
        
#     print("Prime")

#Problem 14 — Fibonacci series ⭐⭐ ///////////////////////////////
# n = int(input("Enter the terms: "))
# a = 0
# b = 1
# for i in range(n):
#     print(a, end=" ")
#     a, b = b, a+b


#💀 Problem 15 — Number Guessing Game
# secert = 7
# n = int(input())
# while n != secert:
#     print("Wrong!")
#     n = int(input())
# print("Correct!")


#Armstrong-style thinking
# n = 153
# orig = n
# total = 0
# while n > 0:
#     digit = n % 10
#     total = total + digit**3
#     n = n // 10
# if orig == total:
#     print(f"Amstrong Number")
# else:
#     print(f"Not Amstrong Number")