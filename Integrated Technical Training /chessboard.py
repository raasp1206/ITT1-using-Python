t = int(input("Enter number of test cases: "))

for _ in range(t):
    # 2. Ask for the size of the board
    n = int(input("Enter board size (N): "))

    board = []
    # 3. Ask for each row of the board
    for _ in range(n):
        row = list(map(int, input().split()))
        board.append(row)

    is_valid = True
    for r in range(n):
        for c in range(n):
            # Check horizontal neighbor
            if c + 1 < n and board[r][c] == board[r][c+1]:
                is_valid = False
                break
            # Check vertical neighbor
            if r + 1 < n and board[r][c] == board[r+1][c]:
                is_valid = False
                break
        if not is_valid:
            break

    # Final result for the test case
    if is_valid:
        print("Yes")
    else:
        print("No")
