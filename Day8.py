#

#1. List comprehension
# numbers = [ x for x in range(1,6)]
# print(numbers)


#2. Squares
# numbers = [1, 2, 3, 4, 5]
# squares = [x*x for x in numbers]
# print(squares)


#3. Even numbers
# numbers = [10, 13, 25, 40, 52, 61, 70]
# even = [x for x in numbers if x % 2 == 0]
# print(even)


#4. Even squares
# numbers = [1, 2, 3, 4, 5, 6]
# even_sq = [x*x for x in numbers if x % 2 == 0]
# print(even_sq)


#5. Uppercase
# names = ["ganesh", "rahul", "arjun"]
# names_upper = [x.upper() for x in names]
# print(names_upper)


#6. enumerate()
# names = ["Ganesh", "Rahul", "Arjun", "Kiran"]
# for index, name in enumerate(names, start=1):
#     print(index, name)


#7. zip()
# names = ["Ganesh", "Rahul", "Arjun"]
# marks = [85, 90, 78]
# for name,mark in zip(names,marks):
#     print(f"{name} -> {mark}")


#8. Dictionary using zip
# names = ["Ganesh", "Rahul", "Arjun"]
# marks = [85, 90, 78]
# student = dict(zip(names,marks))
# print(student)


#9. Sort numbers
# numbers = [50, 10, 40, 20, 30]
# result = sorted(numbers, reverse=True)
# print(result)


#10.Create a lambda function that returns the cube of a number.
# cube = lambda x: x*x*x
# print(cube(2))


#11. map()
# numbers = [1, 2, 3, 4, 5]
# result = list(map(lambda x:x+x ,numbers))
# print(result)


#12. map()— squares
# numbers = [1, 2, 3, 4, 5]
# sq = list(map(lambda x:x*x ,numbers))
# print(sq)


#13. filter() — even numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# even = list(filter(lambda x:x%2==0,numbers))
# print(even)


#14. filter() — positive numbers
# numbers = [-5, 10, -2, 8, -1, 7]
# even = list(filter(lambda x:x>0,numbers))
# print(even)


#15. any()
# numbers = [10, 20, 30, -5, 40]
# result = any(x < 0 for x in numbers)
# print(result)


#16. all()
# numbers = [10, 20, 30, 40]
# result = all(x > 0 for x in numbers)
# print(result)


#17. Dictionary comprehension
# numbers = [1, 2, 3, 4, 5]
# sq = {num: num * num for num in numbers}
# print(sq)


#18. Filter dictionary
# marks = {
#     "Ganesh": 85,
#     "Rahul": 65,
#     "Arjun": 92,
#     "Kiran": 55
# }
# student ={}
# for name,mark in marks.items():
#     if mark >=70:
#         student[name] = mark
# print(student)


#19. Sort students by marks ⭐
# students = {
#     "Ganesh": 85,
#     "Rahul": 65,
#     "Arjun": 92,
#     "Kiran": 78
# }
# result = sorted(students.items(), key=lambda x: x[1], reverse=True)
# print(result)


#⭐ 20. Sort words by length
# words = ["python", "is", "very", "powerful"]
# result = sorted(words, key=lambda x: len(x))
# print(result)

