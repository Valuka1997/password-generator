#importing libraries and dependancies
from tkinter import *
import tkinter.font as tkFont
import string
import random
import pyperclip


#Function to generate password using selected options
def pw_gen():
    selection = ''
    if letters.get() == 1:
        selection = selection + string.ascii_letters

    if numbers.get() == 1:
        selection = selection + string.digits

    if special.get() == 1:
        selection = selection + string.punctuation

#converting input string to integer value
    pwdlen = int(float(pw_length.get()))
#generating password
    pwd = "".join([random.choice(selection) for _ in range(pwdlen)])
#Output password to interface
    pswdbox.configure(text=pwd)
#copy the password to clipboard
    pyperclip.copy(pwd)


#Function to eneble and disable generate button in various scenarios
def chckd():
    if len(pw_length.get()) != 0:

        if letters.get() == 1:
            generate_password_button['state'] = 'normal'
            generate_password_button.configure(text='Generate Password!')

        elif numbers.get() == 1:
            generate_password_button['state'] = 'normal'
            generate_password_button.configure(text='Generate Password!')

        elif special.get() == 1:
            generate_password_button['state'] = 'normal'
            generate_password_button.configure(text='Generate Password!')

        else:
            generate_password_button['state'] = 'disabled'
            generate_password_button.configure(
                text='Check at least one option!')

    else:
        generate_password_button['state'] = 'disabled'
        generate_password_button.configure(text='Enter length and options!')


#Initializing the Window
root = Tk()
#Window title
root.title("Strong Password Generator")
width = 450
height = 350
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height,
                            (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

#Topic element
title = Label(root)
ft = tkFont.Font(family='Times', size=22)
title["font"] = ft
title["fg"] = "#333333"
title["justify"] = "center"
title["text"] = "Random Password Generator"
title.place(x=60, y=20, width=341, height=34)

#Lable
num_passwd_title = Label(root)
ft = tkFont.Font(family='Times', size=10)
num_passwd_title["font"] = ft
num_passwd_title["fg"] = "#333333"
num_passwd_title["justify"] = "center"
num_passwd_title["text"] = "Enter the length of the password"
num_passwd_title.place(x=30, y=80, width=213, height=30)

#Iaking the input
pw_length = Entry(root)
pw_length["borderwidth"] = "1px"
ft = tkFont.Font(family='Times', size=10)
pw_length["font"] = ft
pw_length["fg"] = "#333333"
pw_length["justify"] = "center"
pw_length["text"] = ""
pw_length.place(x=280, y=80, width=70, height=25)


#checkboxes for selection options
letters = IntVar()
numbers = IntVar()
special = IntVar()

ckbtn = tkFont.Font(family='Times', size=10)
C1 = Checkbutton(root, text="Letters", variable=letters, onvalue=1,
                 offvalue=0, height=5, width=20, command=chckd, font=ckbtn)
C1.place(x=70, y=140, width=70, height=25)

C2 = Checkbutton(root, text="Numbers", variable=numbers, onvalue=1,
                 offvalue=0, height=5, width=20, command=chckd, font=ckbtn)
C2.place(x=180, y=140, width=70, height=25)

C3 = Checkbutton(root, text="Special Characters", variable=special,
                 onvalue=1, offvalue=0, height=5, width=20, command=chckd, font=ckbtn)
C3.place(x=300, y=140, width=120, height=25)

#Password output box
pswdbox = Label(root)
ft = tkFont.Font(family='Times', size=14)
pswdbox["font"] = ft
pswdbox["fg"] = "#333333"
pswdbox["justify"] = "center"
pswdbox["text"] = ""
pswdbox.place(x=10, y=190, width=427, height=49)

#Button
generate_password_button = Button(root, command=pw_gen)
generate_password_button["bg"] = "#f0f0f0"
ft = tkFont.Font(family='Times', size=10)
generate_password_button["font"] = ft
generate_password_button["fg"] = "#000000"
generate_password_button["justify"] = "center"
generate_password_button["text"] = "Enter length and options!"
generate_password_button['state'] = "disabled"
generate_password_button.place(x=130, y=250, width=172, height=59)

#Mainloop for gui
root.mainloop()
