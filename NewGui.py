import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Strong Password Generator")
        #setting window size
        width=450
        height=350
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        num_passwd_title=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        num_passwd_title["font"] = ft
        num_passwd_title["fg"] = "#333333"
        num_passwd_title["justify"] = "center"
        num_passwd_title["text"] = "Enter the length of the password"
        num_passwd_title.place(x=30,y=80,width=213,height=30)

        generate_password_button=tk.Button(root)
        generate_password_button["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        generate_password_button["font"] = ft
        generate_password_button["fg"] = "#000000"
        generate_password_button["justify"] = "center"
        generate_password_button["text"] = "Genarate"
        generate_password_button.place(x=130,y=250,width=172,height=59)
        # generate_password_button["command"] = self.GButton_474_command

        C1=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        C1["font"] = ft
        C1["fg"] = "#333333"
        C1["justify"] = "center"
        C1["text"] = "Letters"
        C1.place(x=70,y=140,width=70,height=25)
        C1["offvalue"] = "0"
        C1["onvalue"] = "1"
        # C1["command"] = self.GCheckBox_215_command

        C2=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        C2["font"] = ft
        C2["fg"] = "#333333"
        C2["justify"] = "center"
        C2["text"] = "Numbers"
        C2.place(x=180,y=140,width=70,height=25)
        C2["offvalue"] = "0"
        C2["onvalue"] = "1"
        # C2["command"] = self.GCheckBox_45_command

        C3=tk.Checkbutton(root)
        ft = tkFont.Font(family='Times',size=10)
        C3["font"] = ft
        C3["fg"] = "#333333"
        C3["justify"] = "center"
        C3["text"] = "Special Characters"
        C3.place(x=300,y=140,width=120,height=25)
        C3["offvalue"] = "0"
        C3["onvalue"] = "1"
        # C3["command"] = self.GCheckBox_519_command

        pw_length=tk.Entry(root)
        pw_length["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        pw_length["font"] = ft
        pw_length["fg"] = "#333333"
        pw_length["justify"] = "center"
        pw_length["text"] = ""
        pw_length.place(x=280,y=80,width=70,height=25)

        title=tk.Label(root)
        ft = tkFont.Font(family='Times',size=22)
        title["font"] = ft
        title["fg"] = "#333333"
        title["justify"] = "center"
        title["text"] = "Random Password Generator"
        title.place(x=60,y=20,width=341,height=34)

        pswdbox=tk.Entry(root)
        pswdbox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=14)
        pswdbox["font"] = ft
        pswdbox["fg"] = "#333333"
        pswdbox["justify"] = "center"
        pswdbox["text"] = ""
        pswdbox.place(x=10,y=190,width=427,height=49)

    # def GButton_474_command(self):
    #     print("command")


    # def GCheckBox_215_command(self):
    #     print("command")


    # def GCheckBox_45_command(self):
    #     print("command")


    # def GCheckBox_519_command(self):
    #     print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
