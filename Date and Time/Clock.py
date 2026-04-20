def solve_clock_problem():
    try:
        T = int(input("Enter T (Value of T): "))
        M_total = int(input("Enter M_total (Value of M_total): "))

        if not (M_total >= 60 and M_total % 10 == 0 and T < M_total):
            print("INVALID INPUT")
            return
        found = False

        for H in range(T + 1):
            M = T - H
            if (H * 60) + (M * 10 / 3) == M_total:
                print(f"H = {H}, M = {M}")
                found = True
                break

        if not found:
            print("INVALID INPUT")
    except ValueError:
        print("INVALID INPUT")

if __name__ == "__main__":
    solve_clock_problem()
