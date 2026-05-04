V = int(input("Enter total number of vehicles (V): "))
W = int(input("Enter total number of wheels (W): "))

# Constraint checking
if W < 2 or W % 2 != 0 or V >= W:
    print("INVALID INPUT")
else:
    # Formula derived from:
    # 2*TW + 4*FW = W
    # TW + FW = V
    FW = (W - 2 * V) // 2
    TW = V - FW

    # Ensure physical possibility (no negative vehicles)
    if FW < 0 or TW < 0:
        print("INVALID INPUT")
    else:
        print(f"TW={TW} FW={FW}")
