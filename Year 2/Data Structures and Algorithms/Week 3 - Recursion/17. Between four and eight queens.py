def examine(p):
    for i in range(len(p)):  # Check each queen's position
        for j in range(i + 1, len(p)):
            col1 = p[i]  # Queen i's column
            col2 = p[j]  # Queen j's column
            if (col1 == col2) or (abs(i - j) == abs(col1 - col2)):  # Check for attacks
                return "failure"
    if len(p) == 4:
        return "solution"
    else:
        return "incomplete"

def extensions(p):
    """Generate possible extensions of the current state."""
    if len(p) < 4:  # Up to 4 queens for the Four Queens problem
        return [p + [col] for col in range(4) if col not in p]
    return []

solutions = []
initialState = []

def solve(p):
    verdict = examine(p)
    if verdict == "solution":
        solutions.append(p)
    elif verdict == "failure":
        return
    elif verdict == "incomplete":
        for p_i in extensions(p):
            solve(p_i)

# Solve the Four Queens problem
solve(initialState)
print("Four Queens Solutions:", solutions)
