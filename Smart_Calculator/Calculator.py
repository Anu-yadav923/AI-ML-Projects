print("Welcome to smart calculator")
num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))



def op(operation):
    match operation:
        case 1:
           sum = num1 + num2
           print("sum :", sum)
        case 2:
          substraction = num1 - num2  
          print("substraction :", substraction)
        case 3:
          multiplication = num1 * num2
          print("multiplication: ", multiplication)
        case 4:
          division = num1 // num2
          print("division: ",division)
        case _:
          print("Invalid operation")

operation = int(input("Choose 1: sum , 2: substraction, 3: multiplication, 4: Division"))
op(operation)