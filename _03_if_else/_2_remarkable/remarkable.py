from tkinter import simpledialog, messagebox, Tk

if __name__ == '__main__':
    
    window = Tk()
    window.withdraw()
    
    firstname = simpledialog.askstring(title = "Name?", prompt = "Please enter your first name...")
    
    if firstname == "Nathanael":
        messagebox.showinfo(title = "You are remarkable!", message = "You are an interesting person!")
    
    elif firstname == "Daniel":
        messagebox.showinfo(title = "You are remarkable!", message = "You have remarkable Python skills!")
    
    elif firstname == "Ethan":
        messagebox.showinfo(title = "You are remarkable!", message = "You can move my ears separately and at the same time!")

    
    
    window.mainloop()