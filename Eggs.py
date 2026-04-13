T_str = input("Enter no.of.test cases: ")
T = int(T_str)

for _ in range(T):
    N = int(input("Enter no.of.eggs: "))
    if (N % 6) == 4:
        print("YES")
    else:
        print("NO")
