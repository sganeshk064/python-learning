#1. Sum from 1 to N
# n = int(input())
# def sum(n):
#     total = 0
#     for i in range(n):
#         total += i
#     return total
# print(sum(n))


#2. Count numbers divisible by 3
# n = 50
# def count_num(n):
#     count = 0
#     for i in range(1,n):
#         if i % 3 == 0:
#             count += 1
#     return(count)
# print(count_num(n))


#3. Print even numbers
# n = 100
# def even_num(n):
#     for i in range(1, n):
#         if i % 2==0:
#             print(i)
#     return
# print(even_num(n))


#4. Sum of even numbers
# n = 100
# def even_sum(n):
#     total = 0
#     for i in range(1, n):
#         if i % 2==0:
#             total += i
#     return total
# print(even_sum(n))


#5. Count odd numbers
# numbers = [10, 21, 33, 42, 55, 68, 71]
# odd_num = []
# for i in numbers:
#     if i % 2 != 0:
#         odd_num.append(i)
# print(odd_num)


#6. Reverse a number
# n = 1234
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10 
# print(rev)


#7. Sum of digits
# n = 1234
# total = 0
# while n > 0:
#     digit = n % 10
#     total = total + digit
#     n = n // 10 
# print(total)


#8. Count digits
# n = 58372
# count = 0
# while n > 0:
#     count += 1
#     n = n // 10
# print(count)


#9. Product of digits
# n = 234
# total = 1
# while n > 0:
#     digit = n % 10
#     total = total * digit
#     n = n // 10 
# print(total)


#10. Check palindrome number
# n = 121
# orignal = 121
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# if orignal == rev:
#     print("palindrome")
# else:
#     print("Not Palindrome")


#11. Factorial
# n = 5
# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact = fact * i
#     return fact
# print(factorial(n))


#12. Prime number
# n = 7
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# print(is_prime(n))


#13. Print primes
# n = 100
# def is_prime(n):
#     for i in range(2,n):
#         prime = True
#         for j in range(2, i):
#             if i % j == 0:
#                 prime = False
#         if prime:
#             print(i, end=" ")
# is_prime(n)

# num = 100
# def prime(num):
#     for n in range(2,num):
#         if is_prime(n):
#             print(n)
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
# prime(num)


#14. Fibonacci series
# n = 8
# def fibonacci(n):
#     a = 0
#     b = 1
#     for i in range(n):
#         print(a, end=" ")
#         a, b = a+b, a
# fibonacci(n)


#15. Find GCD//////////////////////////




#16. Find largest element
# numbers = [10, 50, 20, 80, 30]
# largest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num
# print(largest)


#17. Find smallest
# numbers = [10, 50, 20, 80, 30]
# smallest = numbers[0]
# for num in numbers:
#     if num < smallest:
#         smallest = num
# print(smallest)


#18. Calculate average
# marks = [80, 90, 75, 85, 95]
# def summ(marks):
#     total = 0
#     for i in marks:
#         total += i
#     return total
# def avg(marks):
#     sub = len(marks)
#     total = summ(marks)
#     average = total // sub
#     return average
# print(avg(marks))


#19. Count even and odd
# numbers = [10, 15, 22, 33, 40, 51, 62]
# even = 0
# odd = 0
# for i in numbers:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(f"Even = {even}\nOdd = {odd}")


#20. Separate positive and negative
# numbers = [10, -5, 8, -2, 0, 7, -9]
# positive = []
# negative = []
# for i in numbers:
#     if i > 0:
#         positive.append(i)
#     elif i < 0:
#         negative.append(i)
# print(f"Positive: {positive}\nNegative: {negative}")


#21. Count vowels
# word = "programming"
# vowels = 0
# for i in word:
#     if i in "eaiou":
#         vowels += 1
# print(vowels)


#22. Count each character
# word = "hello"
# dic = {}
# for i in word:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i] += 1
# print(dic)


#23. Find first non-repeating character
# s = "kswisks"
# freq = {}
# for ch in s:
#     freq[ch] = freq.get(ch, 0) + 1
# for ch in s:
#     if freq[ch] == 1:
#         print(ch)
#         break


#24. Remove duplicate characters
# word = "programming"
# dup = ""
# for ch in word:
#     if ch not in dup:
#         dup += ch
# print(dup)


#25. Check anagram ⭐
# a = "listen"
# b = "silent"
# d1 = {}
# d2 = {}
# for ch in a:
#     if ch not in d1:
#         d1[ch] = 1
#     else:
#         d1[ch] += 1
# for ch in b:
#     if ch not in d2:
#         d2[ch] = 1
#     else:
#         d2[ch] += 1
# if d1 == d2:
#     print("Anagram")
# else:
#     print("Not Anagram")


#🔥 Challenge 1 — Number Analyzer
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

# def is_palindrome(n):
#     if reverse_number(n) == n:
#         return True
#     else:
#         return False

# n = 153
# Even = is_even(n)
# Prime = is_prime(n)
# Digits = count_digits(n)
# Sum = sum_digits(n)
# Reverse = reverse_number(n)
# palindrome = is_palindrome(n)

# print(f"Even: {Even}\nPrime: {Prime}\nDigits: {Digits}\nSum: {Sum}\nReverse: {Reverse}\nPalindrome: {palindrome}")


#🔥 Challenge 2 — Student Result Analyzer
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

# 🔥 Challenge 3 — Word Frequency Analyzer
# sent = "python is easy and python is powerful and python is popular"
# d = {}
# for word in sent.split():
#     if word not in d:
#         d[word] = 1
#     else:
#         d[word] += 1

# most_frequent = max(d, key=d.get)

# print(most_frequent)
# print(d[most_frequent])