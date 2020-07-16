'''
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got correct
'''

from tkinter import messagebox, simpledialog, Tk

score = 0

'''use function askRiddle with different parameters. Use string splicing and .upper to accept upper and lower responses'''

def askRiddle(riddleNumber, prompt, answer):
    response = simpledialog.askstring(title="Riddle 1", prompt="What gets wetter the more it dries?")
    
    if "towel" in response or "Towel" in response:
        score += 1
        messagebox.showinfo(title="Correct!", message="Your score is " + str(score))
    else:
        score -= 1
        messagebox.showinfo(title="Incorrect...!", message="Your score is " + str(score) + ". \nThe correct answer was " + answer + ".")

if __name__ == '__main__':
    
    window = Tk()
    window.withdraw()
    

    
    
