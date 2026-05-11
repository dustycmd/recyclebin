def generate(expr, is_prefix):
    # Process right-to-left for prefix, else left-to-right
    items = list(expr[::-1] if is_prefix else expr)
    stack = []
    t = 1
    
    print("\nQuadruples:")
    print("Op\tArg1\tArg2\tRes")
    
    quads = []
    for c in items:
        if c.isalnum():
            stack.append(c)
        else:
            # Order of popping matters for subtraction/division
            op2, op1 = stack.pop(), stack.pop()
            if is_prefix: op1, op2 = op2, op1 # Swap for prefix logic
            
            res = f"t{t}"
            print(f"{c}\t{op1}\t{op2}\t{res}")
            quads.append([c, op1, op2]) # Store for triples
            stack.append(res)
            t += 1

    print("\nTriples:")
    print("ID\tOp\tArg1\tArg2")
    for i, q in enumerate(quads):
        # In Triples, we refer to previous results by their (index)
        print(f"({i})\t{q[0]}\t{q[1]}\t{q[2]}")

# --- Hardcoded Input ---
print("--- POSTFIX INPUT ---")
generate("AB+CD-*", is_prefix=False)

print("\n--- PREFIX INPUT ---")
generate("*+AB-CD", is_prefix=True)
