import pytest

import lSystems as ls
import lSystems_turtle as lst
import make_history as hist
import time
from datetime import datetime
import os

"""
To run all test functions: type "pytest" in the terminal
"""


####################################################
# json parsing tests
####################################################

def test_json_asignment_plant_axiom():
    json_dict = ls.json_to_dict("Examples/AssignmentPlant.json")
    assert json_dict["axiom"] == "A"


def test_json_asignment_plant_rules():
    json_dict = ls.json_to_dict("Examples/AssignmentPlant.json")
    assert json_dict["rules"]["A"] == "AA+[+A-A-A]-[-A+A+A]"


def test_json_asignment_plant_translations():
    json_dict = ls.json_to_dict("Examples/AssignmentPlant.json")
    assert json_dict["translations"]["A"] == ["draw", 5]
    assert json_dict["translations"]["+"] == ["angle", 22.5]
    assert json_dict["translations"]["-"] == ["angle", -22.5]
    assert json_dict["translations"]["["] == ["push"]
    assert json_dict["translations"]["]"] == ["pop"]


def test_json_fractal_plant_axiom():
    json_dict = ls.json_to_dict("Examples/fractalplant.json")
    assert json_dict["axiom"] == "X"


def test_json_fractal_plant_rules():
    json_dict = ls.json_to_dict("Examples/fractalplant.json")
    assert json_dict["rules"]["X"] == "F+[[X]-X]-F[-FX]+X"
    assert json_dict["rules"]["F"] == "FF"


def test_json_fractal_plant_translations():
    json_dict = ls.json_to_dict("Examples/fractalplant.json")
    assert json_dict["translations"]["F"] == ["draw", 5]
    assert json_dict["translations"]["X"] == ["nop"]
    assert json_dict["translations"]["+"] == ["angle", 25]
    assert json_dict["translations"]["-"] == ["angle", -25]
    assert json_dict["translations"]["["] == ["push"]
    assert json_dict["translations"]["]"] == ["pop"]


####################################################
# str expansion tests
####################################################

def test_str_expansion_asignment_plant0():
    correct_str = "A"
    assert ls.json_str_expansion("Examples/AssignmentPlant.json", 0) == correct_str


def test_str_expansion_asignment_plant1():
    correct_str = "AA+[+A-A-A]-[-A+A+A]"
    assert ls.json_str_expansion("Examples/AssignmentPlant.json", 1) == correct_str


def test_str_expansion_asignment_plant2():
    correct_str = "AA+[+A-A-A]-[-A+A+A]AA+[+A-A-A]-[-A+A+A]+[+AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]-AA+[+A-A-A]-[-A+A+A]]-[-AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]+AA+[+A-A-A]-[-A+A+A]]"
    assert ls.json_str_expansion("Examples/AssignmentPlant.json", 2) == correct_str


def test_str_expansion_fractal_plant0():
    correct_str = "X"
    assert ls.json_str_expansion("Examples/fractalplant.json", 0) == correct_str


def test_str_expansion_fractal_plant1():
    correct_str = "F+[[X]-X]-F[-FX]+X"
    assert ls.json_str_expansion("Examples/fractalplant.json", 1) == correct_str


def test_str_expansion_fractal_plant2():
    correct_str = "FF+[[F+[[X]-X]-F[-FX]+X]-F+[[X]-X]-F[-FX]+X]-FF[-FFF+[[X]-X]-F[-FX]+X]+F+[[X]-X]-F[-FX]+X"
    assert ls.json_str_expansion("Examples/fractalplant.json", 2) == correct_str


def test_make_history_single_test():
    file_location = "Examples/fractalplant.json"
    amount_of_iters = 3
    timer = datetime.now()
    test_time = timer.strftime("%H:%M:%S")
    correct_history = f"<{test_time}>	<['+', '-', '[', ']']>	<['X', 'F']>	<X>	<{{'X': " \
                      "'F+[[X]-X]-F[-FX]+X', 'F': 'FF'}>	<{'F': ['draw', 5], 'X': " \
                      "['nop'], '+': ['angle', 25], '-': ['angle', -25], '[': ['push'], ']':" \
                      " ['pop']}>	<3>	<FFFF+[[FF+[[F+[[X]-X]-F[-FX]+X]-F+[[X]-X]-F[-FX]+X]-FF" \
                      "[-FFF+[[X]-X]-F[-FX]+X]+F+[[X]-X]-F[-FX]+X]-FF+[[F+[[X]-X]-F[-FX]+X]-F+[[X]-X]" \
                      "-F[-FX]+X]-FF[-FFF+[[X]-X]-F[-FX]+X]+F+[[X]-X]-F[-FX]+X]-FFFF[-FFFFFF+[[F+[" \
                      "[X]-X]-F[-FX]+X]-F+[[X]-X]-F[-FX]+X]-FF[-FFF+[[X]-X]-F[-FX]+X]+F+" \
                      "[[X]-X]-F[-FX]+X]+FF+[[F+[[X]-X]-F[-FX]+X]-F+[[X]-X]-" \
                      "F[-FX]+X]-FF[-FFF+[[X]-X]-F[-FX]+X]+F+[[X]-X]-F[-FX]+X>\n"
    hist.make_history_file(file_location, amount_of_iters)

    history = open("History/history_lsystems.txt", "r")
    last_hist_line = history.readlines()[-1]
    assert last_hist_line == correct_history
    history.close()


def test_back_up():
    file_location = "Examples/fractalplant.json"
    amount_of_iters = 3

    hist.make_history_file(file_location, amount_of_iters)

    hist.history_backup("History/history_lsystems.txt")
    backup_loc = f"""{os.getenv("HOME")}/.l-systems/backup""" + datetime.now().strftime("%d-%m-%Y_%H:%M:%S")

    check_backup = open(backup_loc, "r")
    check_hist = open("History/history_lsystems.txt", "r")

    assert check_backup.read() == check_hist.read()

    check_hist.close()
    check_backup.close()
