def solve_palindrome(n):
    for step in range(1, 6):
        # Reverse the number using string slicing
        reverse_n = int(str(n)[::-1])
        total = n + reverse_n

        print(f"Step {step}: {n} + {reverse_n} = {total}")

        # Check if total is a palindrome
        if str(total) == str(total)[::-1]:
            print(f"Output: {total} is a palindrome.")
            return

        # Update n for the next iteration
        n = total

    print("Output: Palindrome not obtained in 5 steps.")

# Get input from user
num = int(input("Enter a 2-digit or 3-digit number: "))
solve_palindrome(num)
