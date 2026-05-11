prog = [
    ["COPY", "START", "1000"],
    ["-",    "LDA",   "ALPHA"],
    ["ALPHA", "ADD",   "BETA"],
    ["BETA",  "STA",   "GAMMA"],
    ["-",    "RSUB",  "-"],
    ["GAMMA", "RESW",  "1"]
]

symtab = {}
loc = 0
start = 0
name = ""

for line in prog:
    label, instr, oper = line[0], line[1], line[2]

    if instr == "START":
        name = label
        start = int(oper)
        loc = start
    else:
        if label != "-":
            symtab[label] = loc
        loc += 3

length = loc - start

print(f"H^{name}^{start:06X}^{length:06X}")

print("\nSymbol Table")
for sym, val in symtab.items():
    print(f"{sym}\t{val:06X}")

print(f"\nT^{start:06X}^{length:02X}")
print(f"E^{start:06X}")
