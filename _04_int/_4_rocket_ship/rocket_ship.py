from tkinter import *

windowWidth = 800
windowHeight = 800
root = Tk()

canvas = Canvas(root, width=windowWidth, height=windowHeight, borderwidth=0, highlightthickness=0, bg="#000050")
canvas.grid()

# this code runs whenever the mouse is clicked on the window
def mouse_pressed(event):
    # draws a dark blue background
    canvas.create_rectangle(0, 0, windowWidth, windowHeight, fill="#000050")
    
    # this defines the x and y coordinated of all three points
    # of a triangle
    points = [event.x, event.y, event.x - 55, event.y + 65, event.x + 55, event.y + 65]
    canvas.create_polygon(points, fill='gray', width=2) #draws triangle

    for i in range(4):
        canvas.create_oval(event.x - 45, event.y + 65 + i*40, event.x + 45, event.y + 110 + i*40, fill='red', width = 2)
        canvas.create_oval(event.x - 35, event.y + 75 + i*40, event.x + 35, event.y + 110 + i*40, fill='yellow', width = 2)
        canvas.create_oval(event.x - 25, event.y + 85 + i*40, event.x + 25, event.y + 110 + i*40, fill='orange', width = 2)
            
    #1. Add details to your rocket to make it look better. You can look at rocket.png for inspiration.
    
    #2. Modify the locations of the shapes above so the rocket will be drawn where the mouse is clicked
    

canvas.bind("<Button-1>", mouse_pressed)

root.mainloop()