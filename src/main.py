# Main file for TicTacToe
# Team5Project2 - TicTacToe
# Authors: Tommy Antle, Andre Hance, Bailey Matrascia, Alex Le Floch

# This will hold the GUI, User input, and other main features.

# Just for looks
print("Starting...")

# GUI will be built using PySimpleGUI
import PySimpleGUI as sg

# Setting Theme
sg.theme('BrightColors')

# piece image variables, to be assigned to buttons
xPiece = './images/xPiece.png'
yPiece = './images/yPiece.png'
emptyPiece = './images/emptyPiece.png'

# Creating the layout for the window
layout = [[sg.Text("Tic-Tac-Toe")],
 [sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '1'),
 sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '2'),
 sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '3')],
 [sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '4'),
 sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '5'),
 sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '6')],
 [sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '7'),
 sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '8'),
 sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '9')],
 [sg.Button("EXIT")]]

# Creating the window
window = sg.Window("TicTacToe", layout)

# counter variable to determine which player is taking their turn.
turnCounter = 2

# Create an event loop while the window is open
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the Exit button
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break

    if event == "1":
        if (turnCounter % 2 == 0):
            window.FindElement('1').Update(image_filename = xPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1
        else:
            window.FindElement('1').Update(image_filename = yPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1

window.close()
