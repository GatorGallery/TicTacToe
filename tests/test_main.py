"""Test cases for the main file"""

import pytest
import runpy
import sys
import PySimpleGUI

from src import main


def test_number_one():
    """Checks."""
    assert 1 == 1
