from tkinter import *
import random, string
import pyperclip

root=Tk() #initialised tkinter, window created
root.geometry("400x400")
root.resizable(0,0)
root.title("User - PASSWORD GENERATOR")

Label(root, text='PASSWORD GENERATOR', font='arial 15 bold').pack() #label()used todisplay one or more line that user cant edit
Label(root, text ='User', font='arial 15 bold').pack() #pack is organised widget in block

#for password length
pass_label=Label(root, text='PASSWORD LENGTH', font='arial 10 bold').pack() 
pass_len=IntVar() #stores legth of the password
length= Spinbox(root, from_=8, to_=32, textvariable=pass_len, width=15).pack()

pass_str=StringVar() #pass_str is a string type variable that stores the generated password
def Generator():
    password='' #empty string

    for x in range (0,4):
        password=random.choice(string.ascii_uppercase)+ random.choice(string.ascii_lowercase)+ random.choice(string.digits)+ random.choice(string.punctuation)

        for y in range(pass_len.get()- 4):
            password = password+ random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
            pass_str.set(password)

Button(root, text='GENERATE PASSWORD', command= Generator).pack(pady=5)
Entry(root, textvariable=pass_str).pack()
#Button() widget used to display button on our window
#command is called when the button is clicked
#Entry() widget used to create an input text field
#textvariable used to retrieve the current text to the entry widget

def Copy_password():
    pyperclip.copy(pass_str.get())

Button(root, text = 'COPY TO CLIPBOARD', command = Copy_password).pack(pady=5)
root.mainloop()




