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

import ast
students = []
print("\n Welcome to student management system")
print("1. Add student")
print("2. View student")
print("3. Search Student")
print("4. Delete Student")
print("5. Update Marks")
print("6. Exit")

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
       # print(students)
       file = open("student.txt", "r")
       read = file.read()
       data = ast.literal_eval(read)  #previously we read data as string which are store in student.txt file BUT we want to read the real data , so we import a module "ast" and here we use a function called litral_eval which converts string data into REAL PYTHON DATA.
       print(data)
       print(type(data))
       file.close()

    elif choice == '3':
       search_student = input("Enter student name to search : ")
       flag = False
       for student in students :
           if search_student == student["name"] : 
                print("student found successfully!")
                print("name : ", student["name"])
                print("marks : ", student["marks"])
                flag = True
                break
    
       if flag == False :
            print("student not found")

    elif choice == '4':
        delete_student = input("Enter student to delete : ")
        flag = False
        for student in students :
            if delete_student == student["name"] :
                students.remove(student)
                print("student deleted successfully!")
                flag = True
                break

        if flag == False:
            print("Student not found")        

    elif choice == '5':
        updated_name = input("Enter name whose marks to be updated : ")
        found = False
        for student in students :
            if student["name"] == updated_name :
                new_marks = int(input("Enter Marks to be updated : "))
                student["marks"] = new_marks
                print(f'{student["name"]} Marks updated successfully')
                found = True
                break

        if found == False:
            print("student not found")
    elif choice == '6':
        print("Exit....")
        break

file = open("student.txt", "w")
file.write(str(students))
file.close()