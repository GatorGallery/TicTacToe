# Main file for TicTacToe
# Team5Project2 - TicTacToe
# Authors: Tommy Antle, Andre Hance, Bailey Matrascia, Alex Le Floch

# This will hold the GUI, User input, and other main features.

print("testing 123")
import PySimpleGUI as sg

# Creating the layout for the window
layout = [[sg.Text("Tic-Tac-Toe")], [sg.Button("EXIT")]]

# Creating the window
window = sg.Window("TicTacToe", layout)

# Create an event loop while the window is open
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the Exit button
    if event == "EXIT" or event == sg.WIN_CLOSED:
        break

window.close()
