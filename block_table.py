prog = [
    "COPY START 0",
    "USE DATA",
    "A RESW 1",
    "USE CODE",
    "LDA A",
    "END"
]
blocktab = {}
block = "DEFAULT"
loc = 0
for line in prog:
    words = line.split()
    if "USE" in words:
        if len(words) > 1:
            block = words[-1]
        else:
            block = "DEFAULT"
        if block not in blocktab:
            blocktab[block] = loc
    else:
        loc += 3
print("BLOCK TABLE")
print("Block\tAddress")

for name,addr in blocktab.items():
    print(f"{name}\t{addr:04}")
    
