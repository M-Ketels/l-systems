def main():
    axiom = "A"
    rules = {
        "A": "AA+[+A-A-A]-[-A+A+A]"
    }
    print(l_system_string_expansion(axiom, rules, 5))


def l_system_string_expansion(axiom: str, rules: dict, iterations: int) -> str:
    current_string = axiom
    keys = rules.keys()
    for iter in range(iterations):
        new_string = ""
        for symbol in current_string:
            if symbol in keys:
                new_string += rules[symbol]

        current_string = new_string

    return current_string


if __name__ == "__main__":
    main()