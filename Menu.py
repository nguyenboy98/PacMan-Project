import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
# import main as main


def play():
    import main as main
    main.play()

def displayHighScore():
    file = open("score.txt")
    data = file.read()
    file.close()
    data = data +'\n'
    txt.insert(0.0,data)
    # Results = Label(window, text=data)
    # Results.grid(row=1, column=1)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

load = Image.open('pacman.jpg')
load = load.resize((300,200), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)
img = Label(root, image = render)
img.pack(side=TOP)

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
play = tk.Button(frame,
                   text="PLay",
                   command= play
                   )
play.pack(side=tk.LEFT)

score = tk.Button(frame,
                  text = "High Score",
                  command =displayHighScore)

score.pack(side = tk.LEFT)

txt = Text(root, width=25, height =10, wrap =WORD)
txt.pack(side = tk.BOTTOM)
root.mainloop()
