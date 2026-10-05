## Day 5: Problems Based on:
# * List
# * Tuple
# * Sets
# * Dictionary

#1. Create a List
# marks = [91,68,92,86,80,94]
# print(f"First Element: {marks[0]}")
# print(f"Last Element: {marks[-1]}")
# print(f"Length of marks: {len(marks)}")


#2. Update a List
# marks = [91,68,92,86,80,94]
# marks[2] = 95
# print(f"{marks}")


#3. Add Elements
# marks = [91,68,92,86,80,94]
# marks.append(54)
# print(marks)


#4. Remove Elements
# marks = [91,68,92,86,80,94]
# marks.remove(68)
# print(marks)


#5. Find Sum
# marks = [91,68,92,86,80,94]
# print(sum(marks))


#6. Find Largest
# marks = [91,68,92,86,80,94]
##we can also do large = marks[0]//
# largest = 0
# for i in marks:
#     if i > largest:
#         largest = i
# print(largest)


#7. Find Smallest
# marks = [91,68,92,86,80,94]
# small = marks[0]
# for i in marks:
#     if i < small:
#         small = i
# print(small)


#8. Count Even Numbers
# marks = [91,68,92,86,80,94]
# even = 0
# for i in marks:
#     if i % 2 == 0:
#         even += 1
# print(even)


#9. Count Positive and Negative
# num = [10, -5, 8, -2, 0, 7, -9]
# pve = 0
# nve = 0
# zero = 0
# for i in num:
#     if i > 0:
#         pve += 1
#     elif i < 0:
#         nve += 1
#     else:
#         zero += 1
# print(f"Positive: {pve}, Negative: {nve}, Zero: {zero}")


#10. Reverse a List
# marks = [91,68,92,86,80,94]
# # marks[::-1] //
# # marks.reverse()//
# rev = []
# for i in marks[::-1]:
#     rev.append(i)
# print(rev)

#11. Remove Duplicates
# marks = [91,68,94,91,92,86,80,94]
# dup = []
# for i in marks:
#     if i not in dup:
#         dup.append(i)
# print(dup)


#12. Second Largest ⭐
# marks = [91,68,92,86,80,94]
# large = 0
# seclar = 0
# for i in marks:
#     if i > large:
#         large = i
# for j in marks:
#     if j < large and j > seclar:
#         seclar = j
# print(seclar , large)


#13. Frequency of Elements ⭐⭐
# marks = [91,68,92,86,80,94]
# freq = {}
# for i in marks:
#     if i in freq:
#         freq[i] += 1
#     else:
#         freq[i] = 1
# print(freq)


#14. Student Dictionary
# student = {
#     "name": "Ganesh",
#     "age": 21,
#     "branch": "Data Science",
#     "college": "Malla Reddy University"
# }
# for key, value in student.items():
#     print(key, value)


#15. Update Student
# student = {
#     "name": "Ganesh",
#     "age": 21,
#     "branch": "Data Science",
#     "college": "Malla Reddy University"
# }
# student["age"] = 22
# student["cgpa"] = 7.03
# student["city"] = "Hyderabad"
# student.pop("branch")
# print(student)


#16. Find Common Elements
# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6, 7, 8]
# common = []
# # print(set(a) & set(b))
# for i in a:
#     if i in b:
#         common.append(i)
# print(common)


#17. Unique Words
# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6, 7, 8]
# common = []
# for i in a:
#     if i not in b:
#         common.append(i)
# for j in b:
#     if j not in a and j not in common:
#         common.append(j)
# print(common)


#18. Student Marks Dictionary/////////////////////////////////////////////////
# student = {
#     "name": "Ganesh",
#     "age": 21,
#     "college": "Malla Reddy University",
#     "branch": "Data Science",
#     "marks": [85, 92, 78, 88]
# }

#19. Character Frequency ⭐////////////////////////////////////////////////////


#20. Remove Duplicate Characters ⭐


#21. Student Management Program ////////////////////////////////////////////
# Name
# Age
# College
# Branch
# Total marks
# Average marks
# Highest mark
# Lowest mark
# student = {
#     "name": "Ganesh",
#     "age": 21,
#     "college": "Malla Reddy University",
#     "branch": "Data Science",
#     "marks": [85, 92, 78, 88]
# }