import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    shapeTurtle = turtle.Turtle()
    
    while True:
        # Ask the user what shape they want to draw and store it in a variable
        shapeSides = simpledialog.askinteger(title="Polygons!", prompt="Please input the number of sides you'd like your polygon to have!")
   
        # Draw the shape requested by the user using if-elif-else statements
        if shapeSides > 2:
            shapeTurtle.circle(radius=100, extent=360, steps=shapeSides)
            break
        
        else:
            messagebox.showerror(title="Error!", message="You can't have that many sides on a polygon :<")
            
        
        # Call the turtle .done() method
    turtle.done()
    
    window.mainloop()