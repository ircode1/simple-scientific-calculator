import math

# Basic math functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    # Check division by zero
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def power(x, y):
    return x ** y

def mod(x, y):
    return x % y

# Trigonometric functions (input in degrees)
def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

# Logarithm base 10 function
def log(x):
    if x <= 0:
        return "Log undefined for zero or negative numbers"
    return math.log10(x)

def main():
    print("\nSimple Scientific Calculator")
    print("""
Operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Power (^)
6. Modulo (%)
7. Sine (sin)
8. Cosine (cos)
9. Tangent (tan)
10. Logarithm (log base 10)
""")

    choice = input("Choose operation (1-10): ")

    try:
        # For operations needing two numbers
        if choice in ['1','2','3','4','5','6']:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        # For operations needing one number
        elif choice in ['7','8','9','10']:
            x = float(input("Enter the number: "))
            y = None
        else:
            print("Invalid choice")
            return

        # Calculate based on choice
        if choice == '1':
            result = add(x, y)
        elif choice == '2':
            result = subtract(x, y)
        elif choice == '3':
            result = multiply(x, y)
        elif choice == '4':
            result = divide(x, y)
        elif choice == '5':
            result = power(x, y)
        elif choice == '6':
            result = mod(x, y)
        elif choice == '7':
            result = sin(x)
        elif choice == '8':
            result = cos(x)
        elif choice == '9':
            result = tan(x)
        elif choice == '10':
            result = log(x)

        print("Result:", result)

    except ValueError:
        print("Please enter valid numbers!")

if __name__ == "__main__":
    while True:
        main()
        again = input("\nDo you want to try another operation? (yes/no): ").lower()
        if again != "yes":
            print("Thanks for using the calculator!")
            break




