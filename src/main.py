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
layout = [[sg.Text("Tic-Tac-Toe")], [sg.Button(image_filename=emptyPiece, image_size=(100, 100), image_subsample=2,  key='1'),
 sg.Button("2"), sg.Button("3")], [sg.Button("4"),
            sg.Button("5"), sg.Button("6")], [sg.Button("7"), sg.Button("8"), sg.Button("9")], [sg.Button("EXIT")]]

# Creating the window
window = sg.Window("TicTacToe", layout)

# Create an event loop while the window is open
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the Exit button
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break

    if event == "1":
        window.FindElement('1').Update(image_filename=xPiece, image_size=(100, 100))

window.close()
