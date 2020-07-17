# Write a Python program that asks the user for two numbers. 
# Then display the sum of the two numbers

from tkinter import simpledialog, messagebox, Tk

if __name__ == '__main__':
    
    window = Tk()
    window.withdraw()
    
    num1 = simpledialog.askfloat(title="Number 1", prompt="Please input a number")
    num2 = simpledialog.askfloat(title="Number 2", prompt="Please input a number")
    messagebox.showinfo(title="Sum", message="The sum of your numbers is " + str(num1 + num2))
    
    window.mainloop()