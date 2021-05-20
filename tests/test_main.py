"""Test cases for the main file"""

import pytest
import runpy
import sys
import PySimpleGUI

from src import main


def test_number_one():
    """Checks."""
    assert 1 == 1


def test_check_minmax(depth = 0, maxdepth = 10):
    """Checks."""
    if depth >= maxdepth:
        assert 0
