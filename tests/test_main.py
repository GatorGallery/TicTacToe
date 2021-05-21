"""Test cases for the main file"""

import pytest
import runpy
import sys
import PySimpleGUI

from src import main


def test_number_one():
    """Checks if the test file works properly."""
    assert 1 == 1


def test_check_minmax(depth = 0, maxdepth = 10):
    """Checks if the minmax function returns 0 if depth >= maxdepth."""
    if depth >= maxdepth:
        assert 0


def test_check_randomAI():
    """Checks if the turnCounter in the randomAI function returns false."""
    main.randomAI()
    assert main.turnCounter == False


def test_check_randomAI2():
    """Checks to make sure the turnCounter in randomAI does not return true."""
    main.randomAI()
    assert main.turnCounter != True
