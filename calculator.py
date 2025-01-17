# main.py
import calculator

def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice(1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {calculator.add(num1, num2)}")

    elif choice == '2':
        print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")

    elif choice == '3':
        print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")

    elif choice == '4':
        try:
            print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")
        except ValueError as e:
            print(e)
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
