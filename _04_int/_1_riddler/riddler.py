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
riddleNumber = 1


def askRiddle(riddle, answer):
    
    global riddleNumber
    global score
    
    response = simpledialog.askstring(title="Riddle " + str(riddleNumber), prompt=riddle)
    
    if answer in response or answer.capitalize() in response:
        score += 1
        messagebox.showinfo(title="Correct!", message="Your score is " + str(score))
    else:
        messagebox.showinfo(title="Incorrect...!", message="Your score is " + str(score) + ". \nThe correct answer was " + answer + ".")
    
    riddleNumber += 1
    
if __name__ == '__main__':
    
    window = Tk()
    window.withdraw()
    
    askRiddle(riddle="What gets wetter the more it dries?", answer="towel")    
    askRiddle(riddle="The more of me you take, the more of me you leave behind... What am I?", answer="footstep")
    askRiddle(riddle="What has a head and a tail, is brown, and has no legs?", answer="penny")
    
    if score >= 2:
        messagebox.showinfo(title="Congrats!", message="You answered " + str(score) +"/3 questions correctly! You win!")
    else:
        messagebox.showinfo(title="Better luck next time...", message="You answered " + str(score) +"/3 questions correctly! Try again!")
    
    window.mainloop()
