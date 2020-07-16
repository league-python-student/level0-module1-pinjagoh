import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    circleRadius = simpledialog.askinteger("Radius", "Please enter a radius in pixels")
    
    # Make a new turtle
    myTurtle = turtle.Turtle()
    myTurtle.speed(0)
    
    # Have your turtle draw a circle with the correct radius
    myTurtle.circle(radius=circleRadius, extent=360, steps=360)

    # Call the turtle .penup() method
    myTurtle.penup()

    # Move your turtle to a new x,y position using .goto()
    myTurtle.goto(100, 100)

    # Calculate the area of your circle and store it in a variable, you can use math.pi
    circleArea = math.pi * circleRadius ** 2
    
    # Write the area of your circle using the turtle .write() method
    myTurtle.write(arg="area = " + str(circleArea), move=True, align='left', font=('Arial',8,'normal'))

    # Hide your turtle
    myTurtle.hideturtle()
    
    # Call turtle.done()
    turtle.done()

    window.mainloop()