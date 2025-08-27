def main():
    try: 
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("The maximum number is:", max(num1, num2))
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()

