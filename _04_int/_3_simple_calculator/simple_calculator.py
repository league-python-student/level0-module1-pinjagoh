# Write a Python program that asks the user for two numbers.
# Then ask the user if the would like to add, subtract, multiply, or divide.
# Use if-else statements to provide the desired math operation on the numbers and display the result.

from tkinter import simpledialog, messagebox, Tk

num1 = None
operation = None
num2 = None

def askValues():
    
    global num1
    global num2
    global operation
    
    num1 = simpledialog.askfloat(title="Number 1", prompt="Please input a number")
    
    while True:
        operation = simpledialog.askstring(title="Operation", prompt="Please input an operation \n(Use +, -, *, or /)")
        if operation == "+" or operation == "-" or operation == "*" or operation == "/":
            break
        else:
            messagebox.showerror(title="Invalid Input", message="Please enter only +, -, *, or /")
            
    num2 = simpledialog.askfloat(title="Number 2", prompt="Please input a number")

if __name__ == '__main__':
    
    window = Tk()
    window.withdraw()
    
    askValues()
    
    while True:
        
        if operation == "+":
            messagebox.showinfo(title="Sum", message=str(num1+num2))
            break
        
        if operation == "-":
            messagebox.showinfo(title="Difference", message=str(num1-num2))
            break
        
        if operation == "*":
            messagebox.showinfo(title="Product", message=str(num1*num2))
            break
            
        if operation == "/":
            if num2 == 0:
                messagebox.showerror(title="Error!", message="Don't divide by zero!")
                messagebox.showerror(title="Error!", message="Let's try this again...")
                askValues()
            else:
                messagebox.showinfo(title="Quotient", message=str(num1/num2))
                break
    
    window.mainloop()