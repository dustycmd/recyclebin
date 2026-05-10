n = int(input("Enter Number of TAC Statements: "))

tac = []

print("Enter TAC Statements:")

for _ in range(n):
    tac.append(input())

leaders = [0]

# Find Leaders
for i in range(len(tac)):

    stmt = tac[i]

    if "goto" in stmt:

        target = int(stmt.split()[-1]) - 1

        if target < len(tac) and target not in leaders:
            leaders.append(target)

        if i + 1 < len(tac) and i + 1 not in leaders:
            leaders.append(i + 1)

leaders.sort()

# Print Basic Blocks
print("\nBasic Blocks:\n")

for i in range(len(leaders)):

    start = leaders[i]

    if i + 1 < len(leaders):
        end = leaders[i + 1]
    else:
        end = len(tac)

    print(f"Block {i+1}")

    for j in range(start, end):
        print(f"{j+1} : {tac[j]}")

    print()

print("Total Basic Blocks =", len(leaders))
