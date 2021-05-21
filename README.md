# Team5Project2: Tic-Tac-Toe

[![Actions Status](../../workflows/build/badge.svg)](../../actions)     [![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


An implementation of the classic game Tic-Tac-Toe. The program is built with [Python](https://www.python.org/) and [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/).

## Installation (For Windows)

**Note that in order to run this program on Mac OS, skip to the next section to use pipenv**

To install [PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/) run:

```
python -m pip install pysimplegui
```

To run the program first clone the repository:

```
git clone git@github.com:allegheny-computer-science-203-s2021/Team5Project2.git
```

Then enter the folder:

```
cd Team5Project2
```

Then to start the program run:

```
python src/main.py
```

## Alternatively, using pipenv (required for Mac OS & testing)

To install dependancies run:

```
pipenv install --dev
```

To run the program:

```
pipenv run python src/main.py
```

Or use `python3` if need-be:

```
pipenv run python3 src/main.py
```

To run the test suite:

```
pipenv run pytest tests/test_main.py
```

## How to play

Follows traditional rules of Tic-Tac-Toe

To play simply use curser to select a gameboard spot and attempt to get three in a row just like any other Tic-Tac-Toe game

For a challenge play against hard level AI that is designed to be unbeatable
