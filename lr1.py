def lr1_parser(input_string):
    # Action Table: sN = shift to state N, rN = reduce by rule N, acc = accept
    # State transitions for: E -> E+T | T, T -> T*F | F, F -> (E) | id
    action = {
        0: {"id": "s5", "(": "s4"},
        1: {"+": "s6", "$": "acc"},
        2: {"+": "r2", "*": "s7", ")": "r2", "$": "r2"},
        3: {"+": "r4", "*": "r4", ")": "r4", "$": "r4"},
        4: {"id": "s5", "(": "s4"},
        5: {"+": "r6", "*": "r6", ")": "r6", "$": "r6"},
        6: {"id": "s5", "(": "s4"},
        7: {"id": "s5", "(": "s4"},
        8: {"+": "s6", ")": "s11"},
        9: {"+": "r1", "*": "s7", ")": "r1", "$": "r1"},
        10: {"+": "r3", "*": "r3", ")": "r3", "$": "r3"},
        11: {"+": "r5", "*": "r5", ")": "r5", "$": "r5"}
    }
    
    # Goto Table: {state: {Non-Terminal: Next State}}
    goto = {
        0: {"E": 1, "T": 2, "F": 3},
        4: {"E": 8, "T": 2, "F": 3},
        6: {"T": 9, "F": 3},
        7: {"F": 10}
    }
    
    # Grammar Rules: (LHS, length of RHS)
    rules = {
        1: ("E", 3), # E -> E + T
        2: ("E", 1), # E -> T
        3: ("T", 3), # T -> T * F
        4: ("T", 1), # T -> F
        5: ("F", 3), # F -> ( E )
        6: ("F", 1)  # F -> id
    }

    stack = [0]
    tokens = input_string.split() + ["$"]
    i = 0

    try:
        while True:
            s = stack[-1]
            t = tokens[i]
            
            if t not in action[s]: return "Rejected"
            act = action[s][t]

            if act == "acc": return "Accepted"
            
            if act.startswith("s"):
                stack.extend([t, int(act[1:])])
                i += 1
            elif act.startswith("r"):
                lhs, length = rules[int(act[1:])]
                for _ in range(2 * length): stack.pop()
                top = stack[-1]
                stack.extend([lhs, goto[top][lhs]])
    except:
        return "Rejected"

# Example usage:
user_input = input("Enter tokens (e.g., id + id * id): ").strip()
print(lr1_parser(user_input))
