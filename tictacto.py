from tkinter import *
import random


def next_turn(ro, col):
    global player

    if buttons[ro][col]['text'] == "" and check_winner() is False:

        if player == players[0]:
            buttons[ro][col]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + "'s Turn"))

            elif check_winner() is True:
                label.config(text=(players[0] + " Wins"))

            elif check_winner() == "TIE!":
                label.config(text="TIE!")

        else:
            buttons[ro][col]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + "'s Turn"))

            elif check_winner() is True:
                label.config(text=(players[1] + " Wins"))

            elif check_winner() == "TIE!":
                label.config(text="TIE!")


def check_winner():
    for ro in range(3):
        if buttons[ro][0]['text'] == buttons[ro][1]['text'] == buttons[ro][2]['text'] != "":
            buttons[ro][0].config(bg="light blue")
            buttons[ro][1].config(bg="light blue")
            buttons[ro][2].config(bg="light blue")
            return True

    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            buttons[0][col].config(bg="light blue")
            buttons[1][col].config(bg="light blue")
            buttons[2][col].config(bg="light blue")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="light blue")
        buttons[1][1].config(bg="light blue")
        buttons[2][2].config(bg="light blue")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="light blue")
        buttons[1][1].config(bg="light blue")
        buttons[2][0].config(bg="light blue")
        return True

    elif empty_space() is False:
        for ro in range(3):
            for col in range(3):
                buttons[ro][col].config(bg="light green")
        return "TIE!"
    else:
        return False


def empty_space():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player

    player = random.choice(players)
    label.config(text=(player + "'s Turn"))

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")


window = Tk()
window.title("Tic-Tac-Toe")

players = ["X", "O"]
player = random.choice(players)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

label = Label(window, text=(player + "'s turn"), font=("", 20), bg="light blue")
label.pack(side=TOP)

reset_button = Button(window, text="Restart", font=("", 15), command=new_game)
reset_button.pack(side=TOP)

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=("", 20), width=5, height=3,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
