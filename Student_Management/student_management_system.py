#students = []
#for i in range(3):
  #   name = input("Enter student name : ")
  #  students.append(name)
  #  print(students) 

#students = []
#for i in range(3):
 #   name = input("Enter student Name : ")
 #   marks = int(input("Enter student marks : "))
  #  student = {
 #       "Name" : name,
 #       "Marks" : marks
  #  }
 #   students.append(student)
#print(students)
#print(students[0])

students = []
print("/n Welcome to student management system")
print("1. Add student")
print("2. View student")
print("3. Exit")

while(True):
    choice = input("Enter choice : ")

    if choice == '1':
    
        name = input("Enter student name : ")
        marks = int(input("Enter student marks : "))
        student = {
            "name" : name,
            "marks" : marks
        }
        students.append(student)
    
        print("Student added successfully!")

    elif choice == '2':
        print(students)

    elif choice == '3':
        print("Exit....")
        break