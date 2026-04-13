try:
    user_data = input("Enter two numbers (e.g., 10 2): ").split()

    if len(user_data) != 2:
        raise ValueError

    a = int(user_data[0])
    b = int(user_data[1])
    result = a / b
    print(result)

except ZeroDivisionError:
    print("Error: Division by zero")

except ValueError:
    print("Error: Invalid input")
