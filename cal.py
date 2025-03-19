




def display_operations():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")


def get_input():
    choice = input("Enter choice (1/2/3/4): ")
    
  
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return choice, num1, num2
    else:
        print("Invalid input! Please choose a valid operation.")
        return None, None, None  

def perform_operation(choice, num1, num2):
    if choice == '1':  
        return num1 + num2
    elif choice == '2':  
        return num1 - num2
    elif choice == '3': 
        return num1 * num2
    elif choice == '4':
        if num2 == 0:
            return "Error! Cannot divide by zero."
        else:
            return num1 / num2

def main():
   
    while True:
        display_operations()  
        choice, num1, num2 = get_input()  

        if choice:  
            result = perform_operation(choice, num1, num2)  
            print(f"Result: {result}")  

        
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes': 
            print("Thank you!")  
            break  


if __name__ == "__main__":
    main()  

