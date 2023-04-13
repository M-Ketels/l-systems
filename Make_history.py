import lSystems as ls
from datetime import datetime


def get_variables(json_file_loc: str) -> list:
    config_dict = ls.json_to_dict(json_file_loc)
    variables = []
    constants = config_dict["rules"].keys()
    translations = config_dict["translations"]

    for char in translations.keys():
        if char not in constants:
            variables.append(char)

    return variables


def make_history_file(json_file_loc: str, iterations: int) -> None:
    """
    adds a timestamp, the variables, the constants, the axiom, the rules and
    the resulting string as a new line to the history file
    :param json_file_loc: location of the config file
    :param iterations: amount of iterations
    :return: void
    """
    history = open("History/history_lsystems.txt", "a")
    time = datetime.now()
    config_dict = ls.json_to_dict(json_file_loc)
    current_time = time.strftime("%H:%M:%S")
    axiom = config_dict["axiom"]
    rules = config_dict["rules"]
    translations = config_dict["translations"]
    constants = rules.keys()
    variables = get_variables(json_file_loc)

    resulting_string = ls.json_str_expansion(json_file_loc, iterations)
    history.write(f"<{current_time}>\t")
    history.write(f"<{variables}>\t")
    history.write(f"<{constants}>\t")
    history.write(f"<{axiom}>\t")
    history.write(f"<{rules}>\t")
    history.write(f"<{translations}>\t")
    history.write(f"<{iterations}>\t")
    history.write(f"<{resulting_string}>\n") #needs to be newline instead of tab
    history.close()

