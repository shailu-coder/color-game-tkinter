### Have A Query Or Want More Project Like This Follow Us At Instagram - www.instagram.com/python_coderz_


from tkinter import *
import random

root = Tk()
root.title('COLOR GAME')
root.geometry('400x400')

timeleft = 30
score = 0
color = ['yellow','red','blue','black', 'green', 'purple', 'orange', 'pink', 'brown']

def startGame(event):
    if timeleft == 30:
        countdown()
    nextcolor()
    
def countdown():
    global timeleft
    if(timeleft > 0):
        timeleft -= 1
        label_timeleft.config(text="Timeleft: "+str(timeleft))
        label_timeleft.after(1000, countdown)
        
def nextcolor():
    global score
    global timeleft
    if(timeleft > 0):
        entry.focus_set()
        if entry.get().lower() == color[1].lower():
            score += 1
        random.shuffle(color)
        entry.delete(0, END)
        label_score.config(text="Score: "+str(score))
        label_color.config(text=str(color[0]), fg=str(color[1]))

label_rule = Label(root, font=("Courier New",12,'bold'), text='''Enter the color name of the color 
of the display color name''')
label_rule.pack(side=TOP)

label_timeleft = Label(root, text="Timeleft: "+str(timeleft), font=("Courier New",15,'bold'))
label_timeleft.place(x=130, y=50)

label_score = Label(root, text="Score: "+str(score), font=("Courier New",15,'bold'))
label_score.place(x=130, y=80)

label_color = Label(root, text=color[0], fg=color[1], font=("Courier New",50,'bold'))
label_color.place(x=80, y=150)

entry = Entry(root, font=("Courier New",15,'bold'), width=25, bd=5, bg='powder blue')
root.bind('<Return>', startGame)
entry.place(x=50, y=250)
entry.focus()

root.mainloop()
