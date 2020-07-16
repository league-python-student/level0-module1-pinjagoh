# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

from tkinter import messagebox, simpledialog, Tk
import math

if __name__ == '__main__':
    
    window = Tk()
    window.withdraw()
    
    circleRadius = simpledialog.askfloat(title="Circle Calculator", prompt="Please input the radius of your circle...")
    
    while True:
        
        ac = simpledialog.askstring(title="Circle Calculator", prompt="Would you like to find the area or circumference of your circle? \n(a for area, c for circumference)")
       
        if ac == "a":
            messagebox.showinfo(title="Circle Calculator", message="Your circle's area is " + str(math.pi * circleRadius**2))
            break
        
        elif ac == "c":
            messagebox.showinfo(title="Circle Calculator", message="Your circle's circumference is " + str(2 * math.pi * circleRadius))
            break
        
        else:
            messagebox.showerror(title="Circle Calculator", message="Invalid input! Please use a or c only.")
    
    window.mainloop()



#Area = πr^2
#Circumference = 2πr 