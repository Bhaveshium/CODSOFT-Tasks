#Task 2: Simple Calculator
#

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

#Menu for interaction
def calculator():
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("\nEnter choice: ")

    num1 = float(input("\nEnter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        try:
            result = divide(num1, num2)
        except ValueError as e:
            print(e)
            return

    print("Result:", result)

if __name__ == "__main__":
    calculator()
