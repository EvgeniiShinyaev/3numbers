from functools import reduce
students = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 88, 92], "subject" :["Math", "PE", "English", "IT"]},
    {"name": "Bob", "age": 22, "grades": [78, 89, 76, 85],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "Charlie", "age": 21, "grades": [92, 95, 88, 94],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "David", "age": 20, "grades": [75, 85, 80, 90],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "Eve", "age": 22, "grades": [88, 92, 78, 85],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "Frank", "age": 21, "grades": [85, 90, 88, 92],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "Grace", "age": 20, "grades": [78, 89, 76, 85],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "Hank", "age": 22, "grades": [92, 95, 88, 94],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "Ivy", "age": 21, "grades": [75, 85, 80, 90],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "Jack", "age": 20, "grades": [88, 92, 78, 85],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "Katie", "age": 22, "grades": [85, 90, 88, 92],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "Liam", "age": 21, "grades": [78, 89, 76, 85],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "Mia", "age": 20, "grades": [92, 95, 88, 94],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "Noah", "age": 22, "grades": [75, 85, 80, 90],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "Olivia", "age": 21, "grades": [88, 92, 78, 85],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "Peter", "age": 20, "grades": [85, 90, 88, 92],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "Quinn", "age": 21, "grades": [78, 89, 76, 85],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "Rachel", "age": 20, "grades": [92, 95, 88, 94],"subject" :["Math", "PE", "English", "IT"]},
    {"name": "Sam", "age": 22, "grades": [75, 85, 80, 90],"subject" :["Math", "PE", "English", "IT"]}
]

# Функция для вычисления среднего балла по списку оценок
def calculate_average(grades):
    return sum(grades) / len(grades)

# Функция для фильтрации студентов по возрасту
def filter_by_age(student, target_age):
    return student["age"] == target_age

# Функция для фильтрации студентов по списку предметов
def filter_by_subjects(student, target_subjects):
    return all(grade >= 80 for grade in student["grades"])

# Функция для нахождения студента с самым высоким средним баллом
def find_highest_average(student1, student2):
    return student1 if calculate_average(student1["grades"]) > calculate_average(student2["grades"]) else student2

# Фильтрация студентов по возрасту (например, возрасту 20)
filtered_students_age = list(filter(lambda student: filter_by_age(student, 20), students))

# Фильтрация студентов по списку предметов (например, оценки 90 и выше во всех предметах)
filtered_students_grades = list(filter(lambda student: filter_by_subjects(student, [80, 80, 80, 80]), students))

# Вычисление среднего балла для каждого студента
average_grades = list(map(lambda student: calculate_average(student["grades"]), students))

# Вычисление общего среднего балла по всем студентам
total_average = reduce(lambda x, y: x + y, average_grades) / len(students)

# Нахождение студента с самым высоким средним баллом
student_with_highest_average = reduce(find_highest_average, students)

print("Фильтрованные студенты по возрасту 20:")
for student in filtered_students_age:
    print(student)

print("Фильтрованные студенты по оценкам 80 и выше во всех предметах:")
for student in filtered_students_grades:
    print(student)

print("Средние баллы студентов:", average_grades)
print("Общий средний балл по всем студентам:", total_average)
print("Студент с самым высоким средним баллом:", student_with_highest_average)