def solve_total_hours():
    try:
        T = int(input("Enter T (Total units): "))
        H_total = int(input("Enter H_total (Total hours): "))

        X = 18

        if not (H_total >= 24 and H_total % 2 == 0 and T < H_total):
            print("INVALID INPUT")
            return
        found = False

        for D in range(T + 1):
            H = T - D

            if (D * 24) + (H * X) == H_total:
                print(f"D = {D}, H = {H}")
                found = True
                break

        if not found:
            print("INVALID INPUT")
    except ValueError:
       print("INVALID INPUT")

if __name__ == "__main__":
    solve_total_hours()
