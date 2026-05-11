def ll1_parser(input_tokens):
    input_tokens.append("$")
    stack = ["$", "E"]
    
    # Hardcoded LL(1) Parsing Table
    table = {
        "E":  {"id": ["T", "E'"], "(": ["T", "E'"]},
        "E'": {"+": ["+", "T", "E'"], ")": ["ε"], "$": ["ε"]},
        "T":  {"id": ["F", "T'"], "(": ["F", "T'"]},
        "T'": {"*": ["*", "F", "T'"], "+": ["ε"], ")": ["ε"], "$": ["ε"]},
        "F":  {"id": ["id"], "(": ["(", "E", ")"]}
    }

    idx = 0
    while stack:
        top = stack.pop()
        curr = input_tokens[idx]

        if top == curr:
            idx += 1
        elif top in table and curr in table[top]:
            prod = table[top][curr]
            if prod != ["ε"]:
                stack.extend(reversed(prod))
        else:
            return "Rejected"

    return "Accepted" if idx == len(input_tokens) else "Rejected"

# Hardcoded logic for execution
if __name__ == "__main__":
    user_input = input("Enter tokens (e.g., id + id): ").strip().split()
    print(ll1_parser(user_input))
    
