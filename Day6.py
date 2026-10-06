## Day 6: Problems Based on:
# * Functions

#1. Greeting function

# def greet(name):
#     print(f"Hello {name}")

# greet("Ganesh")


#2. Square function
# def square(n):
#     return n * n
# print(square(5))


#3. Cube function
# def cube(n):
#     return n * n * n
# print(cube(5))


#4. Add two numbers
# def add(a, b):
#     return a + b
# print(add(10, 20))


#5. Maximum of two
# def maximum(a, b):
#     if a > b:
#         return a
#     else:
#         return b

# print(maximum(10, 20))


#6. Even or odd
# def odd_even(n):
#     if n % 2 == 0:
#         return f"{n} is Even"
#     else:
#         return f"{n} is Odd"
# print(odd_even(2))


#7. Positive / Negative / Zero
# def check_no(n):
#     if n > 0:
#         return f"{n} is Positive"
#     elif n < 0:
#         return f"{n} is Negative"
#     else:
#         return f"{n} is Zero"
# n = int(input())
# print(check_no(n))


#8. Factorial
# n = int(input())
# def fact(n):
#     total = 1
#     for i in range(1,n+1):
#         total = total * i
#     return total
# print(fact(n))


#9. Sum of digits
# num = int(input()) #1234
# def sum(num):
#     total = 0
#     while num > 0:
#         digit = num % 10 # 4
#         total = total + digit
#         num = num // 10 #123
#     return total
# print(sum(num))


#10. Reverse number
# num = int(input())
# def rev_num(num):
#     rev = 0
#     while num > 0:
#         digit = num % 10
#         num = num // 10
#         rev = rev * 10 + digit
#     return rev
# print(rev_num(num))


#11. Count digits
# n = int(input())
# def count_digit(n):
#     count = 0
#     while n > 0:
#         # digit = n % 10
#         count += 1
#         n = n // 10
#     return count
# print(count_digit(n))


#12. Prime checker ⭐
# n = 7
# def check_prime(n):
#     if n < 2:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# print(check_prime(n))


#13. Fibonacci function ⭐
# n = 7
# def is_fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, b + a
# is_fibonacci(n)


#14. Count vowels
# a = "education"
# def count_vowels(a):
#     vowels = 0
#     consonants = 0
#     for ch in a.lower():
#         if ch in "eaiou":
#             vowels += 1
#         elif ch.isalpha():
#             consonants += 1
#     return vowels
# print(count_vowels(a))


#15. Palindrome checker
# a = "madam"
# def is_palindrom(a):
#     rev = ""
#     for ch in a:
#         rev = ch + rev
#     if rev == a:
#         return True
#     else:
#         return False
# print(is_palindrom(a))


#16. Largest element
# num = [20, 33, 63, 11, 45, 35, 54]
# def larg_num(num):
#     large = 0
#     for i in num:
#         if i > large:
#             large = i
#     return large
# print(larg_num(num))


#17. Smallest element
# num = [20, 33, 63, 11, 45, 35, 54]
# def small_num(num):
#     small = num[1]
#     for i in num:
#         if small > i:
#             small = i
#     return small
# print(small_num(num))


#18. Count even numbers
# num = [20, 33, 63, 11, 45, 35, 54]
# def check_even(num):
#     count = 0
#     for i in num:
#         if i % 2 == 0:
#             count += 1
#     return count
# print(check_even(num))


#19. Remove duplicates
# num = [20, 33, 63, 11, 45, 45, 54, 63]
# def remove_dup(num):
#     orignal = []
#     for i in num:
#         if i not in orignal:
#             orignal.append(i)
#     return orignal
# print(remove_dup(num))


#20. Character frequency ⭐⭐⭐
# word = "banana"
# def freq(word):
#     char = {}
#     for i in word:
#         if i not in char:
#             char[i] = 1
#         else:
#             char[i] += 1
#     return char
# print(freq(word))


#Challenge 1 — Calculator using functions
# num1 = int(input("Enter Number1: "))
# num2 = int(input("Enter Number2: "))
# operator = input("Enter Operator: ")
# def add(num1, num2):
#     return num1 + num2

# def mul(num1, num2):
#     return num1 * num2

# def sub(num1, num2):
#     return num1 - num2

# def div(num1, num2):
#     return num1 / num2

# if operator == "+":
#     print(add(num1, num2))
# elif operator == "-":
#     print(sub(num1, num2))
# elif operator == "*":
#     print(mul(num1, num2))
# elif operator == "/":
#     print(div(num1, num2))
# else:
#     print(f"{operator} operator is invalid!")


#Challenge 2 — Student Result System
# def calculate_total(marks):
#     total = 0
#     for i in marks:
#         total += i
#     return total

# def calculate_average(marks):
#     sub = len(marks)
#     total = 0
#     for i in marks:
#         total += i
#     avg = total / sub
#     return avg

# def find_highest(marks):
#     high = 0
#     for i in marks:
#         if i > high:
#             high = i
#     return high

# def find_lowest(marks):
#     low = marks[0]
#     for i in marks:
#         if i < low:
#             low = i
#     return low

# def calculate_grade(average):
#     if average >= 90:
#         return "Grade A"
#     elif average >= 80:
#         return "Grade B"
#     elif average >= 70:
#         return "Grade C"
#     elif average >= 60:
#         return "Grade D"
#     else:
#         return "Fail"

# marks = [85, 92, 78, 88, 95]
# total = calculate_total(marks)
# average = calculate_average(marks)
# highest = find_highest(marks)
# lowest = find_lowest(marks)
# grade = calculate_grade(average)
# print(f"Total marks:{total} \nAverage marks: {average}\nHighest marks: {highest}\nLowest marks: {lowest}\nGrade :  {grade}")


#Challenge 3 — Number Analyzer
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# def count_digits(n):
#     count = 0
#     while n > 0:
#         count += 1
#         n = n // 10
#     return count

# def sum_digits(n):
#     total = 0
#     while n > 0:
#         digit = n % 10
#         total += digit
#         n = n // 10
#     return total

# def reverse_number(n):
#     rev = 0
#     while n > 0:
#         digit = n % 10
#         n = n // 10
#         rev = rev * 10 + digit
#     return rev

# n = 153
# Even = is_even(n)
# Prime = is_prime(n)
# Digits = count_digits(n)
# Sum = sum_digits(n)
# Reverse = reverse_number(n)

# print(f"Even: {Even}\nPrime: {Prime}\nDigits: {Digits}\nSum: {Sum}\nReverse: {Reverse}")


#Challenge 4 — String Analyzer
# def count_vowels(text):
#     vowels = 0
#     for i in text.lower():
#         if i in "aeiou":
#             vowels += 1
#     return vowels

# def count_consonants(text):
#     consonants = 0
#     for i in text.lower():
#         if i.isalpha() and i not in "aeiou":
#             consonants += 1
#     return consonants

# def reverse_string(text):
#     rev = ""
#     for i in text:
#         rev = i + rev
#     return rev

# def is_palindrome(text):
#     rev = ""
#     for i in text:
#         rev = i + rev
#     if rev == text:
#         return True
#     else:
#         return False

# text = "Madam"
# vowels = count_vowels(text)
# consonants = count_consonants(text)
# reverse = reverse_string(text)
# palindrome = is_palindrome(text)
# print(f"Vowels = {vowels}\nConsonants = {consonants}\nReverse: {reverse}\nPalindrome: {palindrome}")


#Challenge 5 — Mini Student Management System
# def calculate_total(marks):
#     total = 0
#     for i in marks:
#         total += i
#     return total

# def calculate_average(marks):
#     sub = len(marks)
#     total = 0
#     for i in marks:
#         total += i
#     avg = total / sub
#     return avg

# def find_highest(marks):
#     high = 0
#     for i in marks:
#         if i > high:
#             high = i
#     return high

# def find_lowest(marks):
#     low = marks[0]
#     for i in marks:
#         if i < low:
#             low = i
#     return low

# students = {
#     "Ganesh": [85, 92, 78],
#     "Rahul": [72, 88, 91],
#     "Arjun": [90, 85, 95]
# }

# name = input("Enter student name: ")

# if name in students:
#     marks = students[name]

#     total = calculate_total(marks)
#     average = calculate_average(marks)
#     highest = find_highest(marks)
#     lowest = find_lowest(marks)

#     print(f"Name: {name}\n"
#           f"Total: {total}\n"
#           f"Average: {average}\n"
#           f"Highest: {highest}\n"
#           f"Lowest: {lowest}")
# else:
#     print("Student not found")