from tkinter import *
from tkinter import ttk
import random


# Main Window Stuff
mainWindow = Tk()
mainWindow.title("Simple Rock Paper Scissors Game")
mainWindow.configure(bg="black")
mainWindow.iconbitmap("blackBox.ico")


# Main Functions:

def computer_plays():
    picks = ['ROCK!', 'SCISSORS!', 'PAPER!']
    computer_picks = random.choice(picks)
    r_picker2_label.config(text=computer_picks)
    return computer_picks


def rockBttn():
    """Function that returns values if user picks rock option"""
    picker2_label.config(text="ROCK!")
    computer_choice = computer_plays()
    if computer_choice == 'ROCK!':
        r_end_picker.config(text="It's a TIE!!!", foreground='cyan')
        l_end_picker.config(text="It's a TIE!!!", foreground='cyan')
    elif computer_choice == "SCISSORS!":
        r_end_picker.config(text="I Lost!", foreground='red')
        l_end_picker.config(text="You Win!", foreground='green')
    elif computer_choice == "PAPER!":
        r_end_picker.config(text="I Win!", foreground='green')
        l_end_picker.config(text='You Lost!', foreground='red')


def paperBttn():
    """Function that returns values if user picks paper option"""
    picker2_label.config(text="PAPER!")
    computer_choice = computer_plays()
    if computer_choice == 'PAPER!':
        r_end_picker.config(text="It's a TIE!!!", foreground='cyan')
        l_end_picker.config(text="It's a TIE!!!", foreground='cyan')
    elif computer_choice == "SCISSORS!":
        r_end_picker.config(text="I Won!", foreground='green')
        l_end_picker.config(text="You Lost!", foreground='red')
    elif computer_choice == "ROCK!":
        r_end_picker.config(text="I Lost!", foreground='red')
        l_end_picker.config(text='You Won!', foreground='green')


def scissorBttn():
    """Function that returns values if user picks scissors option"""
    picker2_label.config(text="SCISSORS!")
    computer_choice = computer_plays()
    if computer_choice == 'SCISSORS!':
        r_end_picker.config(text="It's a TIE!!!", foreground='cyan')
        l_end_picker.config(text="It's a TIE!!!", foreground='cyan')
    elif computer_choice == "PAPER!":
        r_end_picker.config(text="I Lost!", foreground='red')
        l_end_picker.config(text="You Won!", foreground='green')
    elif computer_choice == "ROCK!":
        r_end_picker.config(text="I Won!", foreground='green')
        l_end_picker.config(text='You Lost!', foreground='red')


# Frames
leftFrame = Frame(mainWindow, bg="black")
leftFrame.grid(row=0, column=0, padx=30)

rightFrame = Frame(mainWindow, bg='black')
rightFrame.grid(row=0, column=1, padx=30)

# Left Frame Stuff / Human Side
l_top_label = ttk.Label(leftFrame, text='Player 1:', background='black', foreground='white', font='Arial, 50')
l_top_label.grid(row=0, column=0)

# Left Rock Button
l_rock_button = Button(leftFrame, text='ROCK!', background='black', foreground='white', font='Arial, 10',
                       command=rockBttn, activeforeground='cyan')
l_rock_button.grid(row=1, column=0, pady=8)

# Left Paper Button
l_paper_button = Button(leftFrame, text='PAPER!', background='black', foreground='white', font='Arial, 10',
                        command=paperBttn, activeforeground='cyan')
l_paper_button.grid(row=2, column=0, pady=8)


# Left Scissors Button
l_scissors_button = Button(leftFrame, text='SCISSORS!', background='black', foreground='white', font='Arial, 10',
                           command=scissorBttn, activeforeground='cyan')
l_scissors_button.grid(row=3, column=0, pady=8)


# Left Frame User Picked
picker1_label = Label(leftFrame, text='You Picked: ', background='black', foreground='white', font='Arial, 20')
picker1_label.grid(row=4, column=0)
# *********************************************
picker2_label = Label(leftFrame, background='black', foreground='white', font='Arial, 20')
picker2_label.grid(row=5, column=0)
# *********************************************
l_end_picker = Label(leftFrame, background='black', foreground='cyan', font='Arial, 20')
l_end_picker.grid(row=6, column=0)


# ***********************************************************************************************************


# Right Frame Stuff / Computer Side
r_top_label = ttk.Label(rightFrame, text='Player 2:', background='black', foreground='white', font='Arial, 50')
r_top_label.grid(row=0, column=0)


# Right Rock Button
r_rock_button = Button(rightFrame, text='ROCK!', background='black', foreground='white', font='Arial, 10',
                       command=rockBttn, state='disabled')
r_rock_button.grid(row=1, column=0, pady=8)

# Right Paper Button
r_paper_button = Button(rightFrame, text='PAPER!', background='black', foreground='white', font='Arial, 10',
                        command=paperBttn, state='disabled')
r_paper_button.grid(row=2, column=0, pady=8)


# Right Scissors Button
r_scissors_button = Button(rightFrame, text='SCISSORS!', background='black', foreground='white', font='Arial, 10',
                           command=scissorBttn, state='disabled')
r_scissors_button.grid(row=3, column=0, pady=8)


# Right Frame User Picked
r_picker1_label = Label(rightFrame, text='I Picked: ', background='black', foreground='white', font='Arial, 20')
r_picker1_label.grid(row=4, column=0)
# *****************************************
r_picker2_label = Label(rightFrame, background='black', foreground='white', font='Arial, 20')
r_picker2_label.grid(row=5, column=0)
# ******************************************
r_end_picker = Label(rightFrame, background='black', foreground='cyan', font='Arial, 20')
r_end_picker.grid(row=6, column=0)


mainWindow.mainloop()
