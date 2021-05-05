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
 [sg.Button("EXIT")],
 [sg.Button("CLEAR")]]

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

    # Button 1 is clicked
    if event == "1":
        if (turnCounter % 2 == 0):
            window.FindElement('1').Update(image_filename = xPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1
        else:
            window.FindElement('1').Update(image_filename = yPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1

    # Button 2 is clicked
    if event == "2":
        if (turnCounter % 2 == 0):
            window.FindElement('2').Update(image_filename = xPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1
        else:
            window.FindElement('2').Update(image_filename = yPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1

    # Button 3 is clicked
    if event == "3":
        if (turnCounter % 2 == 0):
            window.FindElement('3').Update(image_filename = xPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1
        else:
            window.FindElement('3').Update(image_filename = yPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1

    # Button 4 is clicked
    if event == "4":
        if (turnCounter % 2 == 0):
            window.FindElement('4').Update(image_filename = xPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1
        else:
            window.FindElement('4').Update(image_filename = yPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1

    # Button 5 is clicked
    if event == "5":
        if (turnCounter % 2 == 0):
            window.FindElement('5').Update(image_filename = xPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1
        else:
            window.FindElement('5').Update(image_filename = yPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1

    # Button 6 is clicked
    if event == "6":
        if (turnCounter % 2 == 0):
            window.FindElement('6').Update(image_filename = xPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1
        else:
            window.FindElement('6').Update(image_filename = yPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1

    # Button 7 is clicked
    if event == "7":
        if (turnCounter % 2 == 0):
            window.FindElement('7').Update(image_filename = xPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1
        else:
            window.FindElement('7').Update(image_filename = yPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1

    # Button 8 is clicked
    if event == "8":
        if (turnCounter % 2 == 0):
            window.FindElement('8').Update(image_filename = xPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1
        else:
            window.FindElement('8').Update(image_filename = yPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1

    # Button 9 is clicked
    if event == "9":
        if (turnCounter % 2 == 0):
            window.FindElement('9').Update(image_filename = xPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1
        else:
            window.FindElement('9').Update(image_filename = yPiece, image_size = (100, 100))
            turnCounter = turnCounter + 1
    
    # "CLEAR" is clicked
    if event == "CLEAR":
        window.FindElement('1').Update(image_filename = emptyPiece, image_size = (100, 100))
        window.FindElement('2').Update(image_filename = emptyPiece, image_size = (100, 100))
        window.FindElement('3').Update(image_filename = emptyPiece, image_size = (100, 100))
        window.FindElement('4').Update(image_filename = emptyPiece, image_size = (100, 100))
        window.FindElement('5').Update(image_filename = emptyPiece, image_size = (100, 100))
        window.FindElement('6').Update(image_filename = emptyPiece, image_size = (100, 100))
        window.FindElement('7').Update(image_filename = emptyPiece, image_size = (100, 100))
        window.FindElement('8').Update(image_filename = emptyPiece, image_size = (100, 100))
        window.FindElement('9').Update(image_filename = emptyPiece, image_size = (100, 100))
            
window.close()
