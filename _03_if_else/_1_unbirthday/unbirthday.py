from tkinter import simpledialog, messagebox, Tk

if __name__ == '__main__':
    
    #initializing window
    window = Tk()
    window.withdraw()
    
    #ask user for birthday
    birthday = simpledialog.askstring(title = "Birthday", prompt = "Please enter your birthday. \nUse the format mm/dd")
    
    if birthday == "07/16":
        messagebox.showinfo(title = "Happy birthday!", message = "Happy birthday!")
        
    else:
        messagebox.showinfo(title = "Very merry UNbirthday!", message = "Very merry UNbirthday!")
    
    window.mainloop()