import pytest

import lSystems as ls
import lSystems_turtle

"""
To run all test functions: type "pytest" in the terminal
"""
# TODO: add tests for history functionality
# TODO: add tests for incomplete/incorrect config files

# TODO: add continuous integration pipeline that executes these tests in github


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

#TODO history unit-tests