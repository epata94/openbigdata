student_tuples = [
     ('john', 'A', 15),
     ('jane', 'C', 10),
     ('dave', 'B', 12),
]

print(sorted(student_tuples, key=lambda student: student[1]))
print(sorted(student_tuples, key=lambda student: student[2]))
