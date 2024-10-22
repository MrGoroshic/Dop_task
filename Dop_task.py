students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
student_performance = {}

students_list = list(students)
students_list.sort()

for i in range(0, len(grades)):
    grades_mid = sum(grades[i]) / len(grades[i])
    student_performance.update({students_list[i] : grades_mid})

print(student_performance)
