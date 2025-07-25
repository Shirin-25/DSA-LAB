student={}
n=int(input("enter number of students"))
for i in range(n):
    rollno=input("enter roll number")
    name=input("enter name")
    student[rollno]=name
print("student details")
for rollno in student.items():
    print("roll no:",rollno,"name",name)
    