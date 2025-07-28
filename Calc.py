# Basic Calculator Program
def calculator():
    print("Simple Calculator using Python")
    
    # Get user input
    try:
        num1 = float(input("\nEnter the first Number:"))
        num2 = float(input("Enter the second Number:"))
        operation = input("Enter the operation (+, -, *, /)").strip()
        
        # perform calculation operation
        if operation == "+":
            result = num1 + num2
            print(f"{num1}+ {num2} = {result}")
        elif operation == "-":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif operation == "*":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid operation Please choose one of: +, -, *, /")
        
    except ValueError:
        print("Invalid input Please Enter valid number")

# Run the calculator
calculator()