n = int(input("Enter Number of Lines: "))

prog = []
symtab = {}

loc = 0
start = 0
progname = ""

for _ in range(n):

    line = input().split()
    prog.append(line)

# PASS 1
for line in prog:

    if line[1] == "START":

        progname = line[0]
        start = int(line[2])
        loc = start

    else:

        label = line[0]

        if label != "-":
            symtab[label] = loc

        loc += 3

length = loc - start

# H RECORD
print("\nH Record")
print(f"H^{progname}^{start:06}^{length:06}")

# SYMBOL TABLE
print("\nSymbol Table")
print("Symbol\tValue")

for sym,val in symtab.items():
    print(f"{sym}\t{val:06}")

# E RECORD
print("\nE Record")
print(f"E^{start:06}")
