
# calculator

def calculator():
    """Simple calculator program with basic arithmetic operations."""

    while True:
        print("\n🧮 Simple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter choice (1/2/3/4/5): ")

        if choice == '5':
            print("👋 Thank you for using the calculator!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("❌ Invalid choice entered ⚠️")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("❌ Invalid input! Please enter valid numbers.")
            continue

        if choice == '1':
            result = num1 + num2
            print(f"📊 Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"📊 Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"📊 Result: {num1} × {num2} = {result}")
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                print(f"📊 Result: {num1} ÷ {num2} = {result}")
            else:
                print("⚠️ Error! Division by zero")

if __name__ == "__main__":

    calculator()
