import json as json


def main():
    print("n=1")
    print(json_str_expansion("Examples/KochCurve.json", 1))
    print("F+F−F−F+F")

    print("n=2")
    print(json_str_expansion("Examples/KochCurve.json", 2))
    print("F+F−F−F+F+F+F−F−F+F−F+F−F−F+F−F+F−F−F+F+F+F−F−F+F") #correct string for n=2


def json_to_dict(json_file_loc: str) -> dict:
    """
    correctly opens and closes the json file and returns the variables
    in a dictionary form
    :param json_file_loc: the location of the json file in string format
    :return: a dictionary containing all the variables of the json file
    """
    open_file = open(json_file_loc, 'r')
    json_dict = json.load(open_file)
    open_file.close()
    return json_dict


def json_str_expansion(json_file_loc: str, iterations: int) -> str:
    """
    takes a json file location and extracts from it the axiom and the ruleset
    then expands the axiom for 'iterations' amount of iterations according to
    the l_system_string_expansion() function
    :param json_file_loc: the location of the json file in string format
    :param iterations: the amount of iterations (n>=0)
    :return: the fully expanded string
    """
    config_dict = json_to_dict(json_file_loc)
    axiom = config_dict["axiom"]
    rules = config_dict["rules"]
    return l_system_string_expansion(axiom, rules, iterations)


def l_system_string_expansion(axiom: str, rules: dict, iterations: int) -> str:
    """
    expands the axiom (starting string) according to the given rules for a given
    amount of iterations
    :param axiom: the starting string/axiom
    :param rules: the rules showing how to expand the string
    :param iterations: the amount of iterations (n>=0)
    :return: the fully expanded string
    """
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
