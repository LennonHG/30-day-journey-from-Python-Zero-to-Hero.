# Calculator Project -- Guided
# Week 1 - 30 Days Project 

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    #Error handling for division by Zero
    if n2 == 0:
        return "Error: Cannot divide by 0"
    return n1 / n2 

# Main Logic Loop
def calculator():
    print("Select Operations:")
    print("1. Add(+)")
    print("2. Substract")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    #Keep calculator running
    
    while True:
        choice = input("\nEnter choice (1/2/3/4) or 'q' to quit\n")

        if choice.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        if choice in ('1', '2', '3', '4'):
        # Error handling for input
            try:
                #To convert the input numbers into floats
                num1 = float(input("Enter first number: ")) 
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only")
                continue #Go back to start of while loop
            if choice == '1':
                result = add(num1, num2)
                op_symbol = '+'
            elif choice == '2':
                result = subtract(num1, num2)
                op_symbol = '-'
            elif choice == '3':
                result = multiply(num1, num2)
                op_symbol = '*'
            elif choice == '4':
                result = division(num1, num2)
                op_symbol = '/'

            print(f"{num1} {op_symbol} {num2} = {result}")
            
        else:   
            print("Invalid Input. Please choose '1', '2', '3', '4' or 'q' ")
            
calculator()


    
    