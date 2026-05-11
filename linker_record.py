def generate_records(asm_input):
    lines = [line.strip() for line in asm_input.strip().split('\n')]
    
    symbol_table = {}
    extdef_symbols = []
    extref_symbols = []
    lc = 0
    
    for line in lines:
        parts = line.replace(',', ' ').split()
        if not parts: continue
        
        if "START" in parts:
            lc = int(parts[parts.index("START") + 1], 16)
            continue
            
        if "EXTDEF" in parts:
            extdef_symbols = parts[1:]
            continue
            
        if "EXTREF" in parts:
            extref_symbols = parts[1:]
            continue

        if "END" in parts:
            break

        instructions = ["ADD", "SUB", "MUL", "DIV", "LDA", "STA"]
        
        if parts[0] not in instructions:
            # It's a label
            label = parts[0]
            symbol_table[label] = f"{lc:06X}"
            lc += 3
        else:
            lc += 3

    d_parts = ["D"]
    for sym in extdef_symbols:
        if sym in symbol_table:
            d_parts.append(f"{sym}^{symbol_table[sym]}")
    d_record = "^ ".join(d_parts)

    r_record = "R^ " + " ^ ".join(extref_symbols) + " ^"

    print("Sample output:")
    print(d_record)
    print(r_record)
    print("\nLocal Symbol table")
    print(f"{'Symbol NAME':<12} {'value'}")
    for sym, val in symbol_table.items():
        print(f"{sym:<12} {val}")

asm_code = """
PROG2 START 1000
EXTDEF MAX, MIN
EXTREF VAL1, VAL2
LDA ALPHA
MAX STA BETA
ADD GAMMA
MIN SUB DELTA
STA VAL1
END
"""

generate_records(asm_code)
