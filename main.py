from tkinter import *
import string
import random

def pw_gen():
    print("abcabc")
    selection=''
    # if letters.get() == 1 | numbers.get() == 1 | special.get() == 1:
    #     selection = string.ascii_letters + string.digits + string.punctuation
    #
    # elif letters.get() == 1 | numbers.get() == 0 | special.get() == 1:
    #     selection = string.ascii_letters + string.punctuation
    #
    # elif letters.get() == 1 | numbers.get() == 1 | special.get() == 0:
    #     selection = string.ascii_letters + string.digits
    #
    # elif letters.get() == 1 | numbers.get() == 0 | special.get() == 0:
    #     selection = string.ascii_letters
    #
    # elif letters.get() == 0 | numbers.get() == 1 | special.get() == 1:
    #     selection =  string.digits + string.punctuation
    #
    # elif letters.get() == 0 | numbers.get() == 1 | special.get() == 0:
    #     selection =  string.digits
    #
    # elif letters.get() == 0 | numbers.get() == 0 | special.get() == 1:
    #     selection =  string.punctuation
    #
    if letters.get() == 1 :
        selection = selection + string.ascii_letters

    if numbers.get() == 1:
        selection = selection + string.digits

    if special.get() == 1:
        selection = selection + string.punctuation

    pswdbox.delete(0, END)
    pwdlen = int(float(pw_length.get()))
    pwd = "".join([random.choice(selection) for _ in range(pwdlen)])
    pswdbox.insert(0, pwd)

def chckd():
    if letters.get() == 1 :
        generate_password_button['state'] = NORMAL
        generate_password_button.configure(text='Generate Password!')

    elif numbers.get() == 1:
        generate_password_button['state'] = NORMAL
        generate_password_button.configure(text='Generate Password!')

    elif special.get() == 1 :
        generate_password_button['state'] = NORMAL
        generate_password_button.configure(text='Generate Password!')

    else:
        generate_password_button['state'] = DISABLED
        generate_password_button.configure(text='Check at least one option!')

#user inerface

ui = Tk()
ui.title("Strong Password Generator")
ui.config(bg="#ffffff")

title = Label(text="Random Password Generator")
bg = "#00ff00"
fg = "#ff0000"
#title.grid(row=0, column=0, columnspan=3)
title.pack()

num_passwd_title = Label(text="Enter the length of the password")
bg = "#00ff00"
fg = "#ff0000"
#num_passwd_title.grid(row=1, column=0,)
num_passwd_title.pack()

pw_length = Entry(ui, bg="#0000ff")
#pw_length.grid(row=1, column=1)
pw_length.pack()

letters = IntVar()
numbers = IntVar()
special = IntVar()
C1 = Checkbutton(ui, text = "Letters", variable = letters, onvalue = 1, offvalue = 0, height=5, width = 20, command=chckd)
C2 = Checkbutton(ui, text = "Numbers", variable = numbers, onvalue = 1, offvalue = 0, height=5, width = 20, command=chckd)
C3 = Checkbutton(ui, text = "Special Characters", variable = special, onvalue = 1, offvalue = 0, height=5, width = 20, command=chckd)
#C1.grid(row=1, column=2)
#C2.grid(row=2,column=2)
#C3.grid(row=3, column=2)
C1.pack()
C2.pack()
C3.pack()

generate_password_button = Button(ui, text="Check at least one option!",state=DISABLED, bg="#fb743e", height=4, width=55, command=pw_gen)
#generate_password_button.grid(row=4, column=0, columnspan=3)
generate_password_button.pack()

pswdbox = Entry(bg="#383e56",font=("Arial", 15, "bold"), width=40)
#pswdbox.grid(row=3, column=0, columnspan=3)
pswdbox.pack()

ui.mainloop()