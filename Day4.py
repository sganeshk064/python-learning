## Day 4: Problems Based on:
# * Strings

#1. Print each character
# name = "Ganesh"
# for ch in name:
#     print(ch)


#2. First and last character
# name = "Ganesh"
# print(f"First = {name[0]}")
# print(f"Last = {name[-1]}")


#3. Count characters
# name = "Ganesh"
# print(len(name))


#4. Convert case
# name = "Python programming"
# print(name.lower())
# print(name.upper())
# print(name.capitalize())


#5. Reverse a string
# # name = "Ganesh"
# rev = ""
# # print(name[::-1])

# for ch in name:
#     rev = ch + rev
# print(rev)


#6. Count vowels
# name = "education"
# count = 0
# for ch in name:
#     if ch in "aeiou":
#         count += 1
# print(count)


#7. Count vowels and consonants
# name = "hello"
# vowels = 0
# consonants = 0
# for ch in name:
#     if ch in "aeiou":
#         vowels += 1
#     else:
#         consonants += 1
# print(vowels)
# print(consonants)


#8. Count a particular character
# name = "banana"
# print(name.count("a"))

# name = "banana"
# count = 0
# for ch in name:
#     if ch == "a":
#         count += 1
# print(count)


#9. Check palindrome
# name = "madam"
# rev = ""
# for ch in name:
#     rev = ch + rev
# if rev == name:
#     print(f"Palindrome")
# else:
#     print(f"Not Palindrome")

# name = "madam"
# rev = ""
# for ch in name.lower():
#     rev = ch + rev
# if rev == name:
#     print(f"Palindrome")
# else:
#     print(f"Not Palindrome")


#10. Count words
# name = "I love Python"
# words = name.count(" ")
# words += 1
# print(words)

# name = "I love Python"
# words = name.split()
# print(len(words))

# name = "I love Python"
# words = name.split()
# count = 0
# for ch in words:
#     count += 1
# print(count)


#11. Remove spaces
# name = "I love Python"
# word = ""
# for ch in name:
#     if ch not in " ":
#         word = word + ch
# print(word)        


#12. Find the largest character
# name = "python"
# large = ""
# for ch in name:
#     if ch > large:
#         large = ch
# print(f"Largest = {large}")


#13. Count uppercase and lowercase
# word = "PyTHon"
# lower = 0
# upper = 0
# for ch in word:
#     if ch.isupper():
#         upper += 1
#     else:
#         lower += 1
# print(f"UpperCase = {upper}")
# print(f"LowerCase = {lower}")


#14. Remove duplicate characters ⭐⭐
# name = "programming"
# word = ""
# for i in name:
#     if i not in word:
#         word = word + i
# print(f"{word}")


#15. ⭐ Character frequency
# name = "programming"
# word = ""
# for i in name:
#     if i not in word:
#         word = word + i
#         print(f"{i} -> {name.count(i)}")



#Challenge 1 — Anagram
# a = "listen"
# b = "silewt"

# if len(a) != len(b):
#     print("Not Anagram")
# else:
#     for ch in a:
#         if a.count(ch) != b.count(ch):
#             print("Not Anagram")
#             break
#     else:
#         print("Anagram")


#Challenge 2 — Reverse each word
# word = "I love Python"
# x = word.split()
# rev = ""
# for i in x:
#     rev = rev + i[::-1] + " "
# print(rev)


#Challenge 3 — Longest word
# word = "I Love Python Program"
# longest = ""
# for ch in word.split():
#     if len(ch) > len(longest):
#         longest = ch
# print(longest)


#Challenge 4 — Remove vowels
# name = "programming"
# word = ""
# for ch in name:
#     if ch not in "aeiou":
#         word = word + ch
# print(word)


#Challenge 5 — Palindrome ignoring spaces
# word = "nurses run"
# word = word.replace(" ","")
# org = ""
# for ch in word:
#     org = ch + org
# if org == word:
#     print("Palindrome")