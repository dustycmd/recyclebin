grammar = {
    "E": ["E+T", "T"]
}

new_grammar = {}

for nt, rules in grammar.items():
    alpha = [] 
    beta = []  
    for prod in rules:
        if prod.startswith(nt):
            alpha.append(prod[len(nt):]) # Strip the NT from start
        else:
            beta.append(prod)

    if alpha:
        new_nt = nt + "'"
        new_grammar[nt] = [b + new_nt for b in beta]
        new_grammar[new_nt] = [a + new_nt for a in alpha] + ["e"]
    else:
        new_grammar[nt] = rules

# Output
print("Grammar after Left Recursion Removal:")
for nt, rules in new_grammar.items():
    print(f"{nt} -> {' | '.join(rules)}")
