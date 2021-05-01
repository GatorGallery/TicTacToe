# Main file for TicTacToe
# Team5Project2 - TicTacToe
# Authors: Tommy Antle, Andre Hance, Bailey Matrascia, Alex Le Floch

# This will hold the GUI, User input, and other main features.

print("Starting...")
import PySimpleGUI as sg

# Creating the layout for the window
layout = [[sg.Text("Tic-Tac-Toe")], [sg.Button("1"), sg.Button("2"), sg.Button("3")], [sg.Button("4"),
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

window.close()
