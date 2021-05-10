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
layout1 = [[sg.Text("Tic-Tac-Toe Main Menu")],
        [sg.Button("2 Player")],
        [sg.Button("VS Computer (easy)")],
        [sg.Button("VS Computer (hard)")]]

layout2 = [[sg.Text("Tic-Tac-Toe", key = 'title')],
        [sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '1'),
        sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '2'),
        sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '3')],
        [sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '4'),
        sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '5'),
        sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '6')],
        [sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '7'),
        sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '8'),
        sg.Button(image_filename = emptyPiece, image_size = (100, 100), key = '9')],
        [sg.Button("CLEAR"), sg.Button("Main Menu")],
        [sg.Text(text='GAME OVER',font=("Times New Roman",12), visible=False, key='0')]]

layout = [[sg.Column(layout1, key='-COL1-'), sg.Column(layout2, visible=False, key='-COL2-')],
        [sg.Button("EXIT")]]
# Creating the window
window = sg.Window("TicTacToe", layout)

# counter variable to determine which player is taking their turn.
turnCounter = 0

#A dictionary to contain the board state for the program to assess
theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

# Create an event loop while the window is open
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the Exit button
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break

    if event == '2 Player':
        window[f'-COL1-'].update(visible=False)
        window[f'-COL2-'].update(visible=True)

    # Button 1 is clicked
    if event in ['1','2','3','4','5','6','7','8','9']:
        if (turnCounter % 2 == 0):
            window.FindElement(event).Update(image_filename = xPiece, image_size = (100, 100), disabled = True)
            theBoard[event] = 'X'
            turnCounter = turnCounter + 1

        else:
            window.FindElement(event).Update(image_filename = yPiece, image_size = (100, 100), disabled = True)
            theBoard[event] = 'O'
            turnCounter = turnCounter + 1
    
    # Now we will check if player X or O has won,for every move after 5 moves.
    if turnCounter >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                window.FindElement('title').Update("Game Over")
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                window.FindElement('title').Update("Game Over")
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                window.FindElement('title').Update("Game Over")
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                window.FindElement('title').Update("Game Over")
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                window.FindElement('title').Update("Game Over")
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                window.FindElement('title').Update("Game Over")
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                window.FindElement('title').Update("Game Over")
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                window.FindElement('title').Update("Game Over")

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
    if turnCounter == 9:
        window.FindElement('title').Update("Tie Game!")
        window.FindElement('0').Update(visible=True)

    # "CLEAR" is clicked
    if event == "CLEAR":
        for i in range(1,10):
            s = str(i)
            window.FindElement(s).Update(image_filename = emptyPiece, image_size = (100, 100))

    if event == "Main Menu":
        window[f'-COL2-'].update(visible=False)
        window[f'-COL1-'].update(visible=True)


window.close()
