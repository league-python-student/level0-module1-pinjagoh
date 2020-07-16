from tkinter import simpledialog, messagebox, Tk

if __name__ == '__main__':
    
    window = Tk()
    window.withdraw()
    
    passKey = "password"
    
    secret = simpledialog.askstring(title="Secret Message", prompt="Please input a secret message!")
    
    passAttempt = simpledialog.askstring(title="Enter Password", prompt="You must enter the password to see the secret message!")
    
    if passAttempt == passKey:
        messagebox.showinfo(title="Message", message="Here is the secret message: \n" + secret)
        
    else:
        messagebox.showerror(title="INTRUDER!", message="You may not view the secret message!")
      
    
    window.mainloop()