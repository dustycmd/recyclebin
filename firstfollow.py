grammar = {
    "E": ["TA"],
    "A": ["+TA", "e"],
    "T": ["FB"],
    "B": ["*FB", "e"],
    "F": ["(E)", "i"]
}

firsts = {}
follows = {}

def get_first(nt):
    if nt in firsts: return firsts[nt]
    res = set()
    for prod in grammar[nt]:
        if prod == 'e': res.add('e')
        elif not prod[0].isupper(): res.add(prod[0]) # Terminal
        else:
            for char in prod:
                f = get_first(char)
                res |= (f - {'e'})
                if 'e' not in f: break
            else: res.add('e')
    firsts[nt] = res
    return res

def get_follow(nt):
    if nt in follows: return follows[nt]
    res = set()
    if nt == "E": res.add('$') # Start symbol rule
    
    for head, prods in grammar.items():
        for prod in prods:
            if nt in prod:
                idx = prod.index(nt)
                # If there's something after the NT
                if idx + 1 < len(prod):
                    next_char = prod[idx+1]
                    if not next_char.isupper(): res.add(next_char)
                    else:
                        f_next = get_first(next_char)
                        res |= (f_next - {'e'})
                        if 'e' in f_next: res |= get_follow(head)
                # If NT is at the end
                else:
                    if head != nt: res |= get_follow(head)
    follows[nt] = res
    return res

# Execution
for nt in grammar: get_first(nt)
for nt in grammar: get_follow(nt)

# Output
print("NT\tFirst\t\tFollow")
for nt in grammar:
    print(f"{nt}\t{firsts[nt]}\t{follows[nt]}")
