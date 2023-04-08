import pytest

import lSystems as ls
import lSystems_turtle

"""
To run all test functions: type "pytest" in the terminal
"""


def test_example():
    correct_str = "F+F-F-F+F"
    assert ls.json_str_expansion("Examples/KochCurve.json", 1) == correct_str


def test_example2():
    correct_str = "F+F-F-F+F+F+F-F-F+F-F+F-F-F+F-F+F-F-F+F+F+F-F-F+F"
    assert ls.json_str_expansion("Examples/KochCurve.json", 2) == correct_str
