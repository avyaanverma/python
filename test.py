students = []
 
with open("students.csv") as file:
    for line in file:
        name, house= line.rstrip().split(",")
        student = {}
        student["name"] = name
        print(name)
        print(student)
        student["house"] = house
        print(name)
        print(student)
        students.append(student)

print(students)
# for student in students:
#     print(f"{student['name']} is in {student['house']}")