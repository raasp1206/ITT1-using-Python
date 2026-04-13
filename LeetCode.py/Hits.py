def get_hint(code, guess):
    hits = 0
    near_hits = 0
    code_map = {}
    guess_map = {}
    for c, g in zip(code, guess):
        if c == g:
            hits += 1
        else:
            code_map[c] = code_map.get(c, 0) + 1
            guess_map[g] = guess_map.get(g, 0) + 1
    for char in guess_map:
        if char in code_map:
            near_hits += min(guess_map[char], code_map[char])
    return f"{hits}H{near_hits}N"
code_input = input("Enter the secret code: ")
guess_input = input("Enter your guess: ")
result = get_hint(code_input, guess_input)
print(f"Output: {result}")
