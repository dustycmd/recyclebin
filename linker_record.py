prog = [
    "PG1 START 0000",
    "EXTDEF A B",
    "EXTREF C D",
    "ADD ABC",
    "A SUB PQR",
    "ADD ABC1",
    "B MUL ABC",
    "END"
]

loc = 0
symtab = {}
drecord = "D^"
rrecord = "R^"
progname = ""  # Initialize progname
start = 0      # Initialize start
extdef = []    # Initialize extdef to an empty list

for line in prog:
    words = line.split()

    if not words: # Skip empty lines
        continue

    # Handle END directive first, as it can be a single word
    if words[0] == "END":
        break

    # Now handle other directives and instructions
    # Check for START directive, which is in words[1] (e.g., "PG1 START 0000")
    # This requires len(words) to be at least 2 for words[1] and 3 for words[2]
    if len(words) >= 2 and words[1] == "START":
        progname = words[0]
        start = int(words[2])
        loc = start
    elif words[0] == "EXTDEF": # e.g., "EXTDEF A B"
        extdef = words[1:]
    elif words[0] == "EXTREF": # e.g., "EXTREF C D"
        for x in words[1:]:
            rrecord += f" {x} ^"
    else: # This block handles instructions
        # If the instruction has a label (3 words: LABEL OPCODE OPERAND)
        if len(words) == 3: # e.g., "A SUB PQR"
            symtab[words[0]] = loc
        # All instructions (1, 2, or 3 words) increment loc by 3.
        loc += 3

# The rest of the code is outside the loop and should work with initialized variables
for sym in extdef:
    drecord += f" {sym}^{symtab[sym]:06}^"

print(drecord)
print(rrecord)

print("\nLocal Symbol Table")
print("Symbol\tValue")

for sym,val in symtab.items():
    print(f"{sym}\t{val:06}")
