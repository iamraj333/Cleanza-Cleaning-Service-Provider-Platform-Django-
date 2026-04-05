
'''
shell.py: It helps to create a shell for creating, inserting, deleting and updating the model data (from models.py) into database

TO USE SHELL IN THE TERMINAL: we use command 'python manage.py shell'
'''


# FOR STUDENT TABLE
# from RajApp.models import Student
'''
#create data
# Method 1: create()
s1 = Student.objects.create(roll_no=1, name="Alice", course="Mathematics", age=20)
s1.save()
s2 = Student.objects.create(roll_no=2, name="Bob", course="Physics", age=22)
s2.save()
s3 = Student.objects.create(roll_no=3, name="Charlie", course="Chemistry", age=21)
s3.save()
s4 = Student.objects.create(roll_no=4, name="David", course="Biology", age=23)
s4.save()
s5 = Student.objects.create(roll_no=5, name="Eva", course="Computer Science", age=19)
s5.save()

# Method 2: save()
s2 = Student(roll_no=2, name="Bob", course="Physics", age=22)
s2.save()

students = [
    Student(roll_no=6, name="Frank", course="History", age=24),
    Student(roll_no=7, name="Grace", course="Economics", age=20),
    Student(roll_no=8, name="Henry", course="Philosophy", age=22),
    Student(roll_no=9, name="Ivy", course="English", age=21),
    Student(roll_no=10, name="Jack", course="Statistics", age=23),
]
Student.objects.bulk_create(students)


# Get all data
students = Student.objects.all()
print(students)

# Get single student
student = Student.objects.get(roll_no=1)
print(student.name, student.course)


#update data
student = Student.objects.get(roll_no=2)
student.name = "Bobby"
student.age = 23
student.save()

#delete data
student = Student.objects.get(roll_no=1)
student.delete()
'''

#FOR EMPLOYEE TABLE
# from RajApp.models import Employee

# empData=[
# ]

# e1 = Employee.objects.create(EmpId=1, name="Karan", department="Finance", salary=35000, city="Mumbai")
# e1.save()
