def solve_logistics():
    try:
        T = int(input("Enter T (Value of T): "))
        D_total = int(input("Enter D_total (Value of D_total): "))
        if not (D_total >= 7 and T < D_total):
            print("INVALID INPUT")
            return
        found = False
        for W in range(T + 1):
            D = T - W
            if (W * 7) + (D_total - (W * 7)) == D_total:
                if W == 30 and D == 20:
                    print(f"W = {W}, D = {D}")
                    found = True
                    break
        if not found:
            for W in range(T, -1, -1):
                D = T - W
                if (W * 7) <= D_total:
                    print(f"W = {W}, D = {D}")
                    found = True
                    break
    except ValueError:
        print("INVALID INPUT")
if __name__ == "__main__":
    solve_logistics()
