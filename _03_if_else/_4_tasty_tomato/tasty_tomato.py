from tkinter import Canvas, simpledialog, messagebox, Tk
import tkinter as tk

windowWidth = 600
windowHeight = 600

root = tk.Tk()

canvas = tk.Canvas(root, width=windowWidth, height=windowHeight, bg="#DDDDDD")
canvas.grid()


def drawTomato(colorInput):
    canvas.create_oval(75, 200, 400, 450, fill=colorInput, outline="")
    canvas.create_oval(200, 200, 525, 450, fill=colorInput, outline="")
                
    canvas.create_rectangle(275, 100, 325, 230, fill="green", outline="")

#1. Ask the user what color tomato they would like and save their response   
#   You can give them up to three choices

while True:
    
    tomatoColor = simpledialog.askstring(title="Tomato Color", prompt="Would you like a red, blue, or yellow tomato?")
    
    if tomatoColor == "red" or tomatoColor == "blue" or tomatoColor == "yellow":
        drawTomato(tomatoColor)
        break
    
    else:
        messagebox.showerror(title="Invalid Response", message="Please select red, blue, or yellow (case senstive!).")

#2. use if-else statements to draw the tomato in the color that they chose
#   you can modify the code below or draw your own tomato


root.mainloop()