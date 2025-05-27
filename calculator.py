#!/usr/bin/env python3
"""
Simple Calculator
================
A basic calculator with multiple operations
"""

def add(x, y):
    """Addition function"""
    return x + y

def subtract(x, y):
    """Subtraction function"""
    return x - y

def multiply(x, y):
    """Multiplication function"""
    return x * y

def divide(x, y):
    """Division function"""
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

def power(x, y):
    """Power function"""
    return x ** y

def square_root(x):
    """Square root function"""
    if x < 0:
        return "Error: Cannot calculate square root of negative number!"
    return x ** 0.5

def display_menu():
    """Display calculator menu"""
    print("\n🧮 Simple Calculator")
    print("=" * 20)
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Square Root (√)")
    print("7. Exit")
    print("=" * 20)

def get_number(prompt):
    """Get a valid number from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Please enter a valid number!")

def main():
    """Main calculator function"""
    print("🎉 Welcome to Python Calculator!")
    
    while True:
        display_menu()
        
        try:
            choice = int(input("Choose an operation (1-7): "))
        except ValueError:
            print("❌ Please enter a valid choice!")
            continue
        
        if choice == 7:
            print("👋 Thanks for using the calculator!")
            break
        
        if choice in [1, 2, 3, 4, 5]:
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            if choice == 1:
                result = add(num1, num2)
                print(f"✅ {num1} + {num2} = {result}")
            elif choice == 2:
                result = subtract(num1, num2)
                print(f"✅ {num1} - {num2} = {result}")
            elif choice == 3:
                result = multiply(num1, num2)
                print(f"✅ {num1} × {num2} = {result}")
            elif choice == 4:
                result = divide(num1, num2)
                print(f"✅ {num1} ÷ {num2} = {result}")
            elif choice == 5:
                result = power(num1, num2)
                print(f"✅ {num1} ^ {num2} = {result}")
                
        elif choice == 6:
            num = get_number("Enter a number: ")
            result = square_root(num)
            print(f"✅ √{num} = {result}")
            
        else:
            print("❌ Invalid choice! Please select 1-7.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
