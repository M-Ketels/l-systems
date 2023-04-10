import pytest

import lSystems as ls
import lSystems_turtle

"""
To run all test functions: type "pytest" in the terminal
"""

####################################################
# json parsing tests
####################################################

def test_json_asignment_plant_axiom():
    json_dict = ls.json_to_dict("Examples/AsignmentPlant.json")
    assert json_dict["axiom"] == "A"

def test_json_asignment_plant_rules():
    json_dict = ls.json_to_dict("Examples/AsignmentPlant.json")
    assert json_dict["rules"]["A"] == "AA+[+A-A-A]-[-A+A+A]"

def test_json_asignment_plant_translations():
    json_dict = ls.json_to_dict("Examples/AsignmentPlant.json")
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



def test_example():
    correct_str = "F+F-F-F+F"
    assert ls.json_str_expansion("Examples/KochCurve.json", 1) == correct_str


def test_example2():
    correct_str = "F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F"
    assert ls.json_str_expansion("Examples/KochCurve.json", 2) == correct_str
