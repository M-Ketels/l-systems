import json as json


def main():
    print("n=1")
    print(json_str_expansion("Examples/KochCurve.json", 1))
    print("F+F−F−F+F")

    print("n=2")
    print(json_str_expansion("Examples/KochCurve.json", 2))
    print("F+F−F−F+F+F+F−F−F+F−F+F−F−F+F−F+F−F−F+F+F+F−F−F+F") #correct string for n=2


def json_to_dict(json_file_loc: str) -> dict:
    open_file = open(json_file_loc, 'r')
    json_dict = json.load(open_file)
    open_file.close()
    return json_dict


def json_str_expansion(json_file_loc: str, iterations: int) -> str:
    config_dict = json_to_dict(json_file_loc)
    axiom = config_dict["axiom"]
    rules = config_dict["rules"]
    return l_system_string_expansion(axiom, rules, iterations)


def l_system_string_expansion(axiom: str, rules: dict, iterations: int) -> str:
    current_string = axiom
    keys = rules.keys()
    for iter in range(iterations):
        new_string = ""
        for symbol in current_string:
            if symbol in keys:
                new_string += rules[symbol]
            else:
                new_string += symbol

        current_string = new_string

    return current_string


if __name__ == "__main__":
    main()
