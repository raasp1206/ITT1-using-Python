try:
    user_list = [int(x) for x in input("Enter the list of numbers: ").split()]
    index = int(input("Enter the index: "))
    print(user_list[index])

except IndexError:
    print("Error: Index out of range")

except ValueError:
    print("Error: Invalid input")
