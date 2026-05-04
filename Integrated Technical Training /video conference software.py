def solve_video_conference():
    # Dictionary to count occurrences of exact full names
    name_counts = {}
    # Set to store every prefix of every name that has joined
    all_seen_prefixes = set()

    # Get the number of people joining
    try:
        n = int(input("Enter number of people: "))
    except ValueError:
        return

    for _ in range(n):
        name = input().strip()

        # CASE 1: Full name has appeared before
        if name in name_counts:
            name_counts[name] += 1
            print(f"{name} {name_counts[name]}")

        # CASE 2: New full name
        else:
            name_counts[name] = 1
            shortest_prefix = ""
            found_unique = False

            # Check prefixes one by one (e.g., 'a', 'al', 'ali'...)
            for i in range(1, len(name) + 1):
                prefix = name[:i]

                if not found_unique and prefix not in all_seen_prefixes:
                    shortest_prefix = prefix
                    found_unique = True

                # Add this prefix to the global set for future name checks
            if not found_unique:
                shortest_prefix = name

            print(shortest_prefix)

            # Update the global prefix set with ALL prefixes of this name
            for i in range(1, len(name) + 1):
                all_seen_prefixes.add(name[:i])

# Execute
solve_video_conference()
