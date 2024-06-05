from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import os
import logging
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from dotenv import load_dotenv
from tkinter import ttk
from PIL import Image, ImageTk
import logging
from PIL import ImageTk, Image
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv
import requests
import threading
from pathlib import Path
import PySimpleGUI as sg
import pandas as pd
os.system("cls")
os.getcwd()
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import tkinter as tk
import os
import logging
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from dotenv import load_dotenv
from tkinter import ttk
from PIL import Image, ImageTk
import logging
from PIL import ImageTk, Image
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv
import requests
import threading
from pathlib import Path
import PySimpleGUI as sg
import pandas as pd
os.system("cls")
os.getcwd()
import csv
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,messagebox
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


# Memuat variabel lingkungan dari file .env
load_dotenv()

# Mendapatkan token dari variabel lingkungan
token = os.getenv('BOT_TOKEN')
bot_to_forward = os.getenv('ai')



# class App:
#     # Memuat variabel lingkungan dari file .env
# load_dotenv()

# # Mendapatkan token dari variabel lingkungan
# token = os.getenv('BOT_TOKEN')
# bot_to_forward = os.getenv('ai')

class OnlineShop:
    def __init__(self):
        self.window = Tk()
        self.window.title("Online Shop Login")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")
        self.awal()
        self.register()
        self.login()
    

    def register(self):
        canvas = Canvas(self.window, bg="#FFFFFF", height=832, width=1280, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)
        canvas.create_text(750.0, 152.0,anchor="nw",text="REGISTER MEMBER\n",fill="#9E6F21",font=("Inter Black", 45 * -1, "bold"))
        canvas.create_text(803.0, 420.0, anchor="nw", text="PASSWORD", fill="#9E6F21", font=("Inter Black", 24 * -1, "bold"))
        canvas.create_text(803.0, 302.0, anchor="nw", text="USERNAME",fill="#9E6F21",font=("Inter Black", 24 * -1, "bold"))
        canvas.create_text(800.0, 500.0, anchor="nw", text="*Add Maximum 6 Character", fill="#9E6F21", font=("Inter Black", 13 * -1))     
        
        global username
        global password
        global username_entry
        global password_entry
        
        username = StringVar()
        password = StringVar()

        def register_user():
            username_info = username.get().strip()
            password_info = password.get().strip()

            if not username_info:
                messagebox.showwarning(message="Anda belum memasukkan username")
                return

            if not password_info:
                messagebox.showwarning(message="Anda belum memasukkan password")
                return

            if len(username_info) > 6 or len(password_info) > 6:
                messagebox.showwarning(message="Panjang username dan password maksimal adalah 6 karakter")
                return

            if not username_info.isalnum() or not password_info.isalnum():
                messagebox.showwarning(message="Username dan password hanya boleh berisi huruf dan angka")
                return

            with open('userdata.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username_info, password_info])

            messagebox.showinfo(message="Registration Success")
            clear_entries()
            self.awal()

        def clear_entries():
            username.set("")
            password.set("")
            username_entry.focus_set()
        def Hide_password():
            if password_entry.cget('show') == '*':
                password_entry.config(show='')
            else:
                password_entry.config(show='*')

        check_button = Checkbutton(text="Hide password", command=Hide_password)
        check_button.place(x=1030,y=500)

        entry_image_1 = PhotoImage(file="entry_2.png")
        entry_bg_1 = canvas.create_image(968.0,350.5,image=entry_image_1)
        username_entry = Entry(self.window, textvariable=username,bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        username_entry.place(x=803.0,y=333.0,width=330.0,height=33.0)
        
        entry_image_2 = PhotoImage(file="entry_2.png")
        entry_bg_2 = canvas.create_image(968.0, 468.0, image=entry_image_2)
        password_entry = Entry(self.window, textvariable=password, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        password_entry.place(x=803.0, y=450.5, width=330.0, height=33.0)

        image_image_2 = PhotoImage(file="image_1.png")
        image_1 = canvas.create_image(320.0,416.0,image=image_image_2)
        
        button_image_3 = PhotoImage(file="button_regis.png")
        btn = Button(self.window,image=button_image_3,text="Register",width=10,height=1,font=('Microsoft YaHei UI Light', 12),command=register_user)
        btn.place(x=828.0, y=574.0, width=280.0, height=53.0)
        button_image_1 = PhotoImage(file="back.png")
        data = Button(self.window,image=button_image_1,width=10,fg='yellow',bg='brown',text="< Back",font=('Microsoft YaHei UI Light', 12),command=self.awal)
        data.place(x=0.0, y=0.0, width=35.0, height=30.0) 
        
        self.window.resizable(True, True)
        self.window.mainloop()

    def login(self):
        canvas = Canvas(self.window, bg="#FFFFFF", height=832, width=1280, bd=0, highlightthickness=0, relief="ridge")
        canvas.place(x=0, y=0)
        canvas.create_text(803.0, 420.0, anchor="nw", text="PASSWORD", fill="#9E6F21", font=("Inter Black", 24 * -1, "bold"))
        canvas.create_text(803.0, 302.0, anchor="nw", text="USERNAME", fill="#9E6F21", font=("Inter Black", 24 * -1, "bold"))
        canvas.create_text(800.0, 152.0, anchor="nw", text="LOGIN MEMBER\n", fill="#9E6F21", font=("Inter Black", 45 * -1, "bold"))
        canvas.create_text(800.0, 500.0, anchor="nw", text="*Login With Register Account", fill="#9E6F21", font=("Inter Black", 13 * -1))

        global username_verify
        global password_verify
        
        username_verify = StringVar()
        password_verify = StringVar()

        global username_entry1
        global password_entry1

        def login_verify():
            username_info = username_verify.get()
            password_info = password_verify.get()

            if not username_info:
                messagebox.showwarning(message="Anda belum memasukkan username")
                return

            if not password_info:
                messagebox.showwarning(message="Anda belum memasukkan password")
                return

            registered_users = []
            with open('userdata.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    registered_users.append(row[0])
                    if row[0] == username_info and row[1] == password_info:
                        messagebox.showinfo(message="Login Success")
                        self.login1()
                        return

            if username_info in registered_users:
                messagebox.showwarning(message="Password anda salah!")
            else:
                messagebox.showwarning(message="User mungkin belum Register!")

            clear_entries()

        def clear_entries():
            username.set("")
            password.set("")
            username_entry.focus_set()
            
        def Hide_password():
            if password_entry1.cget('show') == '*':
                password_entry1.config(show='*')
            else:
                password_entry1.config(show='*')

        check_button = Checkbutton(text="Hide password", command=Hide_password)
        check_button.place(x=1030,y=500)

        entry_image_1 = PhotoImage(file="entry_2.png")
        entry_bg_1 = canvas.create_image(968.0,350.5,image=entry_image_1)
        username_entry1  = Entry(self.window,textvariable=username_verify ,bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        username_entry1.place(x=803.0,y=333.0,width=330.0,height=33.0)
        
        entry_image_2 = PhotoImage(file="entry_2.png")
        entry_bg_2 = canvas.create_image(968.0, 468.0, image=entry_image_2)
        password_entry1 = Entry(self.window, textvariable=password_verify, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        password_entry1.place(x=803.0, y=450.5, width=330.0, height=33.0)

        image_image_1 = PhotoImage(file="image_1.png")
        image_1 = canvas.create_image(320.0,416.0,image=image_image_1)
        
        button_image_2 = PhotoImage(file="button_log.png")
        kop = Button(self.window,text="Login",image=button_image_2,width=10,height=1,command=login_verify,font=('Microsoft YaHei UI Light', 12))
        kop.place(x=851.0000610351562,y=564.0,width=175.0,height=60.0)
        button_image_1 = PhotoImage(file="back.png")
        data = Button(self.window,image=button_image_1,width=10,fg='yellow',bg='brown',text="< Back",font=('Microsoft YaHei UI Light', 12),command=self.awal)
        data.place(x=0.0, y=0.0, width=35.0, height=30.0) 
           
        self.window.resizable(True, True)
        self.window.mainloop()

    def awal(self):
        canvas = Canvas(self.window,bg="#FFFFFF",height=832,width=1280,bd=0,highlightthickness=0,relief="ridge")
        canvas.place(x=0, y=0)
        canvas.create_text(803.0,420.0,anchor="nw",text="LOG IN",fill="#9E6F21",font=("Inter Black", 24 * -1, "bold"))
        canvas.create_text(803.0,302.0,anchor="nw",text="REGISTER",fill="#9E6F21",font=("Inter Black", 24 * -1, "bold"))
        canvas.create_text(700.0,152.0,anchor="nw",text="AFANAH MARKETPLACE\n",fill="#9E6F21",font=("Inter Black", 45 * -1, "bold"))
        canvas.create_text(750.0,195.0,anchor="nw",text="TOKO ELEKTRONIK AMANAH TERPERCAYA\n",fill="#9E6F21",font=("Inter Black", 45 * 0))

        button_image_1 = PhotoImage(file="button_regis.png")
        button_1 = Button(self.window,image=button_image_1,borderwidth=0,highlightthickness=0,relief="flat",command=self.register)
        button_1.place(x=803.0,y=333.0,width=285.0, height=53.0)

        button_image_2 = PhotoImage(file="button_log.png")
        button_2 = Button(self.window,image=button_image_2,borderwidth=0,highlightthickness=0,relief="flat",command=self.login,anchor="center")
        button_2.place(x=803.0, y=450.5,width=200.0,height=55.0)

        image_image_1 = PhotoImage(file="image_1.png")
        image_1 = canvas.create_image(320.0, 416.0, image=image_image_1)

        self.window.resizable(True, True)
        self.window.mainloop()
        
    def login1(self):
        self.window.destroy()
        Newarrival()
    def run(self):
        self.awal()
    # def __init__(self):
        
    #     self.window = Tk()
    #     self.window.title("Online Shop Login")
    #     self.window.geometry("1280x832")
    #     self.window.configure(bg="#FFFFFF")

    #     self.canvas = Canvas(self.window, bg="#FFFFFF", height=832, width=1280, bd=0, highlightthickness=0, relief="ridge")
    #     self.canvas.place(x=0, y=0)
    #     self.canvas.create_text(803.0, 420.0, anchor="nw", text="PASSWORD", fill="#9E6F21", font=("Inter Black", 24 * -1, "bold"))
    #     self.canvas.create_text(803.0,302.0, anchor="nw", text="EMAIL",fill="#9E6F21",font=("Inter Black", 24 * -1, "bold"))
    #     self.canvas.create_text(800.0,152.0,anchor="nw",text="LOGIN MEMBER\n",fill="#9E6F21",font=("Inter Black", 45 * -1, "bold"))

    #     button_image_1 = PhotoImage(file=("button_1.png"))
    #     self.button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=self.login1,relief="flat")
    #     self.button_1.place(x=851.0000610351562,y=564.0,width=219.0,height=89.0)

    #     entry_image_1 = PhotoImage(file=("entry_1.png"))
    #     entry_bg_1 = self.canvas.create_image(968.0,350.5,image=entry_image_1)
    #     self.entry_1 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
    #     self.entry_1.place(x=803.0,y=333.0,width=330.0,height=33.0)

    #     entry_image_2 = PhotoImage(file=("entry_2.png"))
    #     entry_bg_2 = self.canvas.create_image(968.0,468.0,image=entry_image_2)
    #     self.entry_2 = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
    #     self.entry_2.place(x=803.0,y=450.5,width=330.0,height=33.0)

    #     image_image_1 = PhotoImage(file=("image_1.png"))
    #     self.image_1 = self.canvas.create_image(320.0,416.0,image=image_image_1)

    #     self.window.resizable(True, True)
    #     self.window.mainloop()

    # def login1(self):
    #     self.window.destroy()
    #     Newarrival()
        

#=====================================================================================================================================#
#=====================================================================================================================================#

class Newarrival:
    def __init__(self):
        self.window = Tk()
        self.window.title("New Arrivals")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")


        self.canvas = Canvas(self.window, bg = "#FFFFFF", height = 832, width = 1280, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(0.0, 0.0, 264.0, 832.0, fill="#F1EBC9", outline="")

        entry_image_1 = PhotoImage(file=("New Arrivals1/entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(731.5,40.5, image=entry_image_1)
        self.entry_1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0 )
        self.entry_1.place(
        x=523.0,
        y=17.0,
        width=417.0,
        height=45.0)

        button_image_1 = PhotoImage(file=("New Arrivals1/button_1.png"))
        self.button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=self.search, relief="flat")
        self.button_1.place(x=952.0, y=17.0, width=47.0, height=47.0)

        self.canvas.create_text(87.0, 102.0, anchor="nw", text="XIAOMI", fill="#000000", font=("Lato Black", 24 * -1, "bold"))

        button_image_2 = PhotoImage(file=("New Arrivals1/button_2.png"))
        self.button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=self.loginpoin, relief="flat")
        self.button_2.place(x=0.0, y=148.0, width=264.0, height=44.0)

        button_image_3 = PhotoImage(file=("New Arrivals1/button_3.png"))
        self.button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0,  command=self.loginpoin1,relief="flat")
        self.button_3.place(x=0.0, y=202.0, width=264.0, height=44.0)

        button_image_4 = PhotoImage(file=("New Arrivals1/button_4.png"))
        self.button_4 = Button(image=button_image_4, borderwidth=0, highlightthickness=0, command=self.loginpoin2, relief="flat")
        self.button_4.place(x=0.0, y=256.0, width=264.0, height=44.0)

        button_image_5 = PhotoImage(file=("New Arrivals1/button_5.png"))
        self.button_5 = Button(image=button_image_5, borderwidth=0, highlightthickness=0, command=self.sorting, relief="flat")
        self.button_5.place(x=0.0, y=310.0, width=264.0,height=44.0)

        self.canvas.create_text(
            582.0,
            97.0,
            anchor="nw",
            text="NEW ARRIVALS",
            fill="#000000",
            font=("Lato Bold", 48 * -1,"bold")
        )

        image_image_1 = PhotoImage(
            file=("New Arrivals1/image_1.png"))
        self.image_1 = self.canvas.create_image(
            757.0,
            306.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("New Arrivals1/image_2.png"))
        self.image_2 = self.canvas.create_image(
            757.0,
            608.0,
            image=image_image_2
        )
        self.window.resizable(True, True)
        self.window.mainloop()


    def loginpoin(self):
        self.window.destroy()
        Newarrival_smartphone()

    def loginpoin1(self):
        self.window.destroy()
        Newarrival_smarthome()
    
    def loginpoin2(self):
        self.window.destroy()
        Newarrival_lifestyle()
    
    
    def search(self):
        self.window.destroy()
        run()
        # Product()
        # sc.run()

    def sorting(self):
        self.window.destroy()
        lari()
        # SortingProduct()

#=====================================================================================================================================#
class Newarrival_smartphone:
    def __init__(self):
        self.window = Tk()
        self.window.title("New Arrivals")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            264.0,
            832.0,
            fill="#F1EBC9",
            outline="")

        entry_image_1 = PhotoImage(
            file=("Newarrival_smartphone/entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            731.5,
            40.5,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=523.0,
            y=17.0,
            width=417.0,
            height=45.0
        )

        button_image_1 = PhotoImage(
            file=("Newarrival_smartphone/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_1 clicked"),
            relief="flat"
        )
        self.button_1.place(
            x=952.0,
            y=17.0,
            width=47.0,
            height=47.0
        )

        self.canvas.create_text(
            87.0,
            102.0,
            anchor="nw",
            text="XIAOMI",
            fill="#000000",
            font=("Lato Black", 24 * -1,"bold")
        )

        button_image_2 = PhotoImage(
            file=("Newarrival_smartphone/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin,
            relief="flat"
        )
        self.button_2.place(
            x=0.0,
            y=148.0,
            width=264.0,
            height=44.0
        )

        button_image_3 = PhotoImage(
            file=("Newarrival_smartphone/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin3,
            relief="flat"
        )
        self.button_3.place(
            x=0.0,
            y=192.0,
            width=264.0,
            height=44.0
        )

        button_image_4 = PhotoImage(
            file=("Newarrival_smartphone/button_4.png"))
        self.button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin4,
            relief="flat"
        )
        self.button_4.place(
            x=0.0,
            y=236.0,
            width=264.0,
            height=44.0
        )

        button_image_5 = PhotoImage(
            file=("Newarrival_smartphone/button_5.png"))
        self.button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
           command=self.loginpoin5,
            relief="flat"
        )
        self.button_5.place(
            x=0.0,
            y=280.0,
            width=264.0,
            height=44.0
        )

        button_image_6 = PhotoImage(
            file=("Newarrival_smartphone/button_6.png"))
        self.button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin1,
            relief="flat"
        )
        self.button_6.place(
            x=0.0,
            y=334.0,
            width=264.0,
            height=44.0
        )

        button_image_7 = PhotoImage(
            file=("Newarrival_smartphone/button_7.png"))
        self.button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin2,
            relief="flat"
        )
        self.button_7.place(
            x=0.0,
            y=388.0,
            width=264.0,
            height=44.0
        )


        image_image_1 = PhotoImage(
            file=("Newarrival_smartphone/image_1.png"))
        self.image_1 = self.canvas.create_image(
            758.0,
            320.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Newarrival_smartphone/image_2.png"))
        self.image_2 = self.canvas.create_image(
            758.0,
            622.0,
            image=image_image_2
        )
        button_image_1 = PhotoImage(
            file=("xiaomi11tpro/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def loginpoin(self):
        self.window.destroy()
        Newarrival()

    def loginpoin1(self):
        self.window.destroy()
        Newarrival_smarthome()

    def loginpoin2(self):
        self.window.destroy()
        Newarrival_lifestyle()

    def loginpoin3(self):
        self.window.destroy()
        Smartphone_xiaomi()

    def loginpoin4(self):
        self.window.destroy()
        Smartphone_poco()
    
    def loginpoin5(self):
        self.window.destroy()
        Smartphone_redmi()

    def back(self):
        self.window.destroy()
        Newarrival()

#=====================================================================================================================================#
class Newarrival_smarthome:
    def __init__(self):
        self.window = Tk()
        self.window.title("New Arrivals")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            264.0,
            832.0,
            fill="#F1EBC9",
            outline="")

        button_image_1 = PhotoImage(
            file=("Newarrival_smarthome/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin3,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=246.0,
            width=264.0,
            height=44.0
        )

        button_image_2 = PhotoImage(
            file=("Newarrival_smarthome/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin4,
            relief="flat"
        )
        self.button_2.place(
            x=0.0,
            y=290.0,
            width=264.0,
            height=44.0
        )

        button_image_3 = PhotoImage(
            file=("Newarrival_smarthome/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin5,
            relief="flat"
        )
        self.button_3.place(
            x=0.0,
            y=334.0,
            width=264.0,
            height=44.0
        )

        entry_image_1 = PhotoImage(
            file=("Newarrival_smarthome/entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            731.5,
            40.5,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=523.0,
            y=17.0,
            width=417.0,
            height=45.0
        )

        button_image_4 = PhotoImage(
            file=("Newarrival_smarthome/button_4.png"))
        self.button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=952.0,
            y=17.0,
            width=47.0,
            height=47.0
        )

        self.canvas.create_text(
            87.0,
            102.0,
            anchor="nw",
            text="XIAOMI",
            fill="#000000",
            font=("Lato Black", 24 * -1,"bold")
        )

        button_image_5 = PhotoImage(
            file=("Newarrival_smarthome/button_5.png"))
        self.button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin1,
            relief="flat"
        )
        self.button_5.place(
            x=0.0,
            y=148.0,
            width=264.0,
            height=44.0
        )

        button_image_6 = PhotoImage(
            file=("Newarrival_smarthome/button_6.png"))
        self.button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin,
            relief="flat"
        )
        self.button_6.place(
            x=0.0,
            y=202.0,
            width=264.0,
            height=44.0
        )

        button_image_7 = PhotoImage(
            file=("Newarrival_smarthome/button_7.png"))
        self.button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin2,
            relief="flat"
        )
        self.button_7.place(
            x=0.0,
            y=388.0,
            width=264.0,
            height=44.0
        )

        button_image_8 = PhotoImage(
            file=("xiaomi11tpro/button_1.png"))
        self.button_1 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        image_image_1 = PhotoImage(
            file=("Newarrival_smarthome/image_1.png"))
        self.image_1 = self.canvas.create_image(
            732.0,
            310.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Newarrival_smarthome/image_2.png"))
        self.image_2 = self.canvas.create_image(
            732.0,
            612.0,
            image=image_image_2
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def loginpoin(self):
        self.window.destroy()
        Newarrival()

    def loginpoin1(self):
        self.window.destroy()
        Newarrival_smartphone()

    def loginpoin2(self):
        self.window.destroy()
        Newarrival_lifestyle()

    def loginpoin3(self):
        self.window.destroy()
        Smarthome_TVmedia()

    def loginpoin4(self):
        self.window.destroy()
        Semarthome_Peralatan_rumah_tangga()

    def loginpoin5(self):
        self.window.destroy()
        Semarthome_Perangkat_pintar()

    def back(self):
        self.window.destroy()
        Newarrival()


#=====================================================================================================================================#

class Newarrival_lifestyle:
    def __init__(self):
        self.window = Tk()
        self.window.title("Livestyle")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            264.0,
            832.0,
            fill="#F1EBC9",
            outline="")

        button_image_1 = PhotoImage(
            file=("Newarrival_livestyle/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin3,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=300.0,
            width=264.0,
            height=44.0
        )

        button_image_2 = PhotoImage(
            file=("Newarrival_livestyle/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin4,
            relief="flat"
        )
        self.button_2.place(
            x=0.0,
            y=344.0,
            width=264.0,
            height=44.0
        )

        button_image_3 = PhotoImage(
            file=("Newarrival_livestyle/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin5,
            relief="flat"
        )
        self.button_3.place(
            x=0.0,
            y=388.0,
            width=264.0,
            height=44.0
        )

        entry_image_1 = PhotoImage(
            file=("Newarrival_livestyle/entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            731.5,
            40.5,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=523.0,
            y=17.0,
            width=417.0,
            height=45.0
        )

        button_image_4 = PhotoImage(
            file=("Newarrival_livestyle/button_4.png"))
        self.button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_4 clicked"),
            relief="flat"
        )
        self.button_4.place(
            x=952.0,
            y=17.0,
            width=47.0,
            height=47.0
        )

        self.canvas.create_text(
            87.0,
            102.0,
            anchor="nw",
            text="XIAOMI",
            fill="#000000",
            font=("Lato Black", 24 * -1,"bold")
        )

        button_image_5 = PhotoImage(
            file=("Newarrival_livestyle/button_5.png"))
        self.button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin1,
            relief="flat"
        )
        self.button_5.place(
            x=0.0,
            y=148.0,
            width=264.0,
            height=44.0
        )

        button_image_6 = PhotoImage(
            file=("Newarrival_livestyle/button_6.png"))
        self.button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin2,
            relief="flat"
        )
        self.button_6.place(
            x=0.0,
            y=202.0,
            width=264.0,
            height=44.0
        )

        button_image_7 = PhotoImage(
            file=("Newarrival_livestyle/button_7.png"))
        self.button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin,
            relief="flat"
        )
        self.button_7.place(
            x=0.0,
            y=256.0,
            width=264.0,
            height=44.0
        )

        button_image_8 = PhotoImage(
            file=("xiaomi11tpro/button_1.png"))
        self.button_1 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        image_image_1 = PhotoImage(
            file=("Newarrival_livestyle/image_1.png"))
        self.image_1 = self.canvas.create_image(
            732.0,
            320.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Newarrival_livestyle/image_2.png"))
        self.image_2 = self.canvas.create_image(
            732.0,
            622.0,
            image=image_image_2
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def loginpoin(self):
        self.window.destroy()
        Newarrival()

    def loginpoin1(self):
        self.window.destroy()
        Newarrival_smartphone()

    def loginpoin2(self):
        self.window.destroy()
        Newarrival_smarthome()

    def loginpoin3(self):
        self.window.destroy()
        Lifestyle_Wearable()

    def loginpoin4(self):
        self.window.destroy()
        Lifestyle_Kantor()

    def loginpoin5(self):
        self.window.destroy()
        Lifestyle_Aksesoris()

    def back(self):
        self.window.destroy()
        Newarrival()

#=====================================================================================================================================#
class Smartphone_xiaomi:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        button_image_1 = PhotoImage(
            file=("smartphone_xiaomi/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.xiaomi12,
            relief="flat"
        )
        self.button_1.place(
            x=318.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        button_image_2 = PhotoImage(
            file=("smartphone_xiaomi/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.xiaomi12pro,
            relief="flat"
        )
        self.button_2.place(
            x=629.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        button_image_3 = PhotoImage(
            file=("smartphone_xiaomi/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
             command=self.xiaomi11t,
            relief="flat"
        )
        self.button_3.place(
            x=318.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_4 = PhotoImage(
            file=("smartphone_xiaomi/button_4.png"))
        self.button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.xiaomi11tpro,
            relief="flat"
        )
        self.button_4.place(
            x=629.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_5 = PhotoImage(
            file=("smartphone_xiaomi/button_5.png"))
        self.button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.xiaomi10t,
            relief="flat"
        )
        self.button_5.place(
            x=940.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_6 = PhotoImage(
            file=("smartphone_xiaomi/button_6.png"))
        self.button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.xiaomi12lite5g,
            relief="flat"
        )
        self.button_6.place(
            x=940.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            264.0,
            832.0,
            fill="#F1EBC9",
            outline="")

        entry_image_1 = PhotoImage(
            file=("smartphone_xiaomi/entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            731.5,
            40.5,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=523.0,
            y=17.0,
            width=417.0,
            height=45.0
        )

        button_image_7 = PhotoImage(
            file=("smartphone_xiaomi/button_7.png"))
        self.button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self.button_7.place(
            x=952.0,
            y=17.0,
            width=47.0,
            height=47.0
        )

        self.canvas.create_text(
            87.0,
            102.0,
            anchor="nw",
            text="XIAOMI",
            fill="#000000",
            font=("Lato Black", 24 * -1,"bold")
        )

        button_image_8 = PhotoImage(
            file=("smartphone_xiaomi/button_8.png"))
        self.button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        self.button_8.place(
            x=0.0,
            y=148.0,
            width=264.0,
            height=44.0
        )

        button_image_9 = PhotoImage(
            file=("smartphone_xiaomi/button_9.png"))
        self.button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        self.button_9.place(
            x=0.0,
            y=192.0,
            width=264.0,
            height=44.0
        )

        button_image_10 = PhotoImage(
            file=("smartphone_xiaomi/button_10.png"))
        self.button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin,
            relief="flat"
        )
        self.button_10.place(
            x=0.0,
            y=236.0,
            width=264.0,
            height=44.0
        )

        button_image_11 = PhotoImage(
            file=("smartphone_xiaomi/button_11.png"))
        self.button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin1,
            relief="flat"
        )
        self.button_11.place(
            x=0.0,
            y=280.0,
            width=264.0,
            height=44.0
        )

        button_image_12 = PhotoImage(
            file=("smartphone_xiaomi/button_12.png"))
        self.button_12 = Button(
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin2,
            relief="flat"
        )
        self.button_12.place(
            x=0.0,
            y=334.0,
            width=264.0,
            height=44.0
        )

        button_image_13 = PhotoImage(
            file=("smartphone_xiaomi/button_13.png"))
        self.button_13 = Button(
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin3,
            relief="flat"
        )
        self.button_13.place(
            x=0.0,
            y=388.0,
            width=264.0,
            height=44.0
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    def loginpoin(self):
        self.window.destroy()
        Smartphone_poco()

    def loginpoin1(self):
        self.window.destroy()
        Smartphone_redmi()

    def loginpoin2(self):
        self.window.destroy()
        Newarrival_smarthome()

    def loginpoin3(self):
        self.window.destroy()
        Newarrival_lifestyle()
    
    def xiaomi12lite5g(self):
        self.window.destroy()
        Xiaomi12Lite5G()

    def xiaomi12pro(self):
        self.window.destroy()
        Xiaomi12pro()

    def xiaomi12(self):
        self.window.destroy()
        Xiaomi12()

    def xiaomi10t(self):
        self.window.destroy()
        Xiaomi10t()

    def xiaomi11tpro(self):
        self.window.destroy()
        Xiaomi11tpro()

    def xiaomi11t(self):
        self.window.destroy()
        Xiaomi11t()
#=====================================================================================================================================#
#=====================================================================================================================================#
class Smartphone_poco:
    def __init__(self):
        self.window = Tk()
        self.window.title("Poco")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(
            318.0,
            351.0,
            591.0,
            403.0,
            fill="#F1EBC9",
            outline="")

        self.canvas.create_rectangle(
            318.0,
            709.0,
            591.0,
            761.0,
            fill="#F1EBC9",
            outline="")

        self.canvas.create_text(
            403.0,
            723.0,
            anchor="nw",
            text="Poco M5S",
            fill="#000000",
            font=("Lato Black", 20 * -1,"bold")
        )

        self.canvas.create_rectangle(
            629.0,
            709.0,
            902.0,
            761.0,
            fill="#F1EBC9",
            outline="")

        self.canvas.create_text(
            719.0,
            723.0,
            anchor="nw",
            text="Poco M5",
            fill="#000000",
            font=("Lato Black", 20 * -1,"bold")
        )

        self.canvas.create_rectangle(
            940.0,
            709.0,
            1213.0,
            761.0,
            fill="#F1EBC9",
            outline="")

        self.canvas.create_rectangle(
            629.0,
            351.0,
            902.0,
            403.0,
            fill="#F1EBC9",
            outline="")

        self.canvas.create_text(
            723.0,
            366.0,
            anchor="nw",
            text="Poco F4",
            fill="#000000",
            font=("Lato Black", 20 * -1,"bold")
        )

        self.canvas.create_rectangle(
            940.0,
            351.0,
            1213.0,
            403.0,
            fill="#F1EBC9",
            outline="")

        button_image_1 = PhotoImage(
            file=
            ("smartphone_poco/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.pocox55g,
            relief="flat"
        )
        self.button_1.place(
            x=318.0,
            y=94.0,
            width=273.0,
            height=257.0
        )

        button_image_2 = PhotoImage(
            file=
            ("smartphone_poco/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.pocof4,
            relief="flat"
        )
        self.button_2.place(
            x=629.0,
            y=94.0,
            width=273.0,
            height=257.0
        )

        button_image_3 = PhotoImage(
            file=
            ("smartphone_poco/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.pocom5s,
            relief="flat"
        )
        self.button_3.place(
            x=318.0,
            y=452.0,
            width=273.0,
            height=257.0
        )

        button_image_4 = PhotoImage(
            file=
            ("smartphone_poco/button_4.png"))
        self.button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.pocom5,
            relief="flat"
        )
        self.button_4.place(
            x=629.0,
            y=452.0,
            width=273.0,
            height=257.0
        )

        button_image_5 = PhotoImage(
            file=
            ("smartphone_poco/button_5.png"))
        self.button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.pocof4gt,
            relief="flat"
        )
        self.button_5.place(
            x=940.0,
            y=452.0,
            width=273.0,
            height=257.0
        )

        button_image_6 = PhotoImage(
            file=
            ("smartphone_poco/button_6.png"))
        self.button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.pocom4pro,
            relief="flat"
        )
        self.button_6.place(
            x=940.0,
            y=94.0,
            width=273.0,
            height=257.0
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            264.0,
            832.0,
            fill="#F1EBC9",
            outline="")

        entry_image_1 = PhotoImage(
            file=
            ("smartphone_poco/entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            731.5,
            40.5,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=523.0,
            y=17.0,
            width=417.0,
            height=45.0
        )

        button_image_7 = PhotoImage(
            file=
            ("smartphone_poco/button_7.png"))
        self.button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("self. clicked"),
            relief="flat"
        )
        self.button_7.place(
            x=952.0,
            y=17.0,
            width=47.0,
            height=47.0
        )

        self.canvas.create_text(
            87.0,
            102.0,
            anchor="nw",
            text="XIAOMI",
            fill="#000000",
            font=("Lato Black", 24 * -1, "bold")
        )

        button_image_8 = PhotoImage(
            file=
            ("smartphone_poco/button_8.png"))
        self.button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        self.button_8.place(
            x=0.0,
            y=148.0,
            width=264.0,
            height=44.0
        )

        button_image_9 = PhotoImage(
            file=
            ("smartphone_poco/button_9.png"))
        self.button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin,
            relief="flat"
        )
        self.button_9.place(
            x=0.0,
            y=192.0,
            width=264.0,
            height=44.0
        )

        button_image_10 = PhotoImage(
            file=
            ("smartphone_poco/button_10.png"))
        self.button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        self.button_10.place(
            x=0.0,
            y=236.0,
            width=264.0,
            height=44.0
        )

        button_image_11 = PhotoImage(
            file=
            ("smartphone_poco/button_11.png"))
        self.button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin1,
            relief="flat"
        )
        self.button_11.place(
            x=0.0,
            y=280.0,
            width=264.0,
            height=44.0
        )

        button_image_12 = PhotoImage(
            file=
            ("smartphone_poco/button_12.png"))
        self.button_12 = Button(
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin2,
            relief="flat"
        )
        self.button_12.place(
            x=0.0,
            y=334.0,
            width=264.0,
            height=44.0
        )

        button_image_13 = PhotoImage(
            file=
            ("smartphone_poco/button_13.png"))
        self.button_13 = Button(
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin3,
            relief="flat"
        )
        self.button_13.place(
            x=0.0,
            y=388.0,
            width=264.0,
            height=44.0
        )

        self.canvas.create_text(
            395.0,
            365.0,
            anchor="nw",
            text="Poco X5 5G",
            fill="#000000",
            font=("Lato Black", 20 * -1, "bold")
        )

        self.canvas.create_text(
            1012.0,
            365.0,
            anchor="nw",
            text="Poco M4 Pro",
            fill="#000000",
            font=("Lato Black", 20 * -1,"bold")
        )

        self.canvas.create_text(
            1018.0,
            723.0,
            anchor="nw",
            text="Poco F4 Gt",
            fill="#000000",
            font=("Lato Black", 20 * -1,"bold")
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def loginpoin(self):
        self.window.destroy()
        Smartphone_xiaomi()

    def loginpoin1(self):
        self.window.destroy()
        Smartphone_redmi()

    def loginpoin2(self):
        self.window.destroy()
        Newarrival_smarthome()

    def loginpoin3(self):
        self.window.destroy()
        Newarrival_lifestyle()

    def pocox55g(self):
        self.window.destroy()
        PocoX55G()

    def pocof4(self):
        self.window.destroy()
        Pocof4()

    def pocom4pro(self):
        self.window.destroy()
        Pocof4()

    def pocom5s(self):
        self.window.destroy()
        pocoM5s()

    def pocom5(self):
        self.window.destroy()
        pocoM5()

    def pocof4gt(self):
        self.window.destroy()
        pocof4gt()
#=====================================================================================================================================#

class Smartphone_redmi:
    def __init__(self):
        self.window = Tk()
        self.window.title("Redmi")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        button_image_1 = PhotoImage(
            file=("Smartphone_redmi/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.redminote12pro5g,
            relief="flat"
        )
        self.button_1.place(
            x=318.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        button_image_2 = PhotoImage(
            file=("Smartphone_redmi/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.redminote12,
            relief="flat"
        )
        self.button_2.place(
            x=629.0,
            y=94.0,
            width=271.0,
            height=309.0
        )

        button_image_3 = PhotoImage(
            file=("Smartphone_redmi/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.redminote11pro5g,
            relief="flat"
        )
        self.button_3.place(
            x=318.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_4 = PhotoImage(
            file=("Smartphone_redmi/button_4.png"))
        self.button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.redminote11pro,
            relief="flat"
        )
        self.button_4.place(
            x=629.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_5 = PhotoImage(
            file=("Smartphone_redmi/button_5.png"))
        self.button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.redminote11,
            relief="flat"
        )
        self.button_5.place(
            x=940.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_6 = PhotoImage(
            file=("Smartphone_redmi/button_6.png"))
        self.button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.redmi102022,
            relief="flat"
        )
        self.button_6.place(
            x=940.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            264.0,
            832.0,
            fill="#F1EBC9",
            outline="")

        entry_image_1 = PhotoImage(
            file=("Smartphone_redmi/entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            731.5,
            40.5,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=523.0,
            y=17.0,
            width=417.0,
            height=45.0
        )

        button_image_7 = PhotoImage(
            file=("Smartphone_redmi/button_7.png"))
        self.button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self.button_7.place(
            x=952.0,
            y=17.0,
            width=47.0,
            height=47.0
        )

        self.canvas.create_text(
            87.0,
            102.0,
            anchor="nw",
            text="XIAOMI",
            fill="#000000",
            font=("Lato Black", 24 * -1,"bold")
        )

        button_image_8 = PhotoImage(
            file=("Smartphone_redmi/button_8.png"))
        self.button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        self.button_8.place(
            x=0.0,
            y=148.0,
            width=264.0,
            height=44.0
        )

        button_image_9 = PhotoImage(
            file=("Smartphone_redmi/button_9.png"))
        self.button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin,
            relief="flat"
        )
        self.button_9.place(
            x=0.0,
            y=192.0,
            width=264.0,
            height=44.0
        )

        button_image_10 = PhotoImage(
            file=("Smartphone_redmi/button_10.png"))
        self.button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin1,
            relief="flat"
        )
        self.button_10.place(
            x=0.0,
            y=236.0,
            width=264.0,
            height=44.0
        )

        button_image_11 = PhotoImage(
            file=("Smartphone_redmi/button_11.png"))
        self.button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_11 clicked"),
            relief="flat"
        )
        self.button_11.place(
            x=0.0,
            y=280.0,
            width=264.0,
            height=44.0
        )

        button_image_12 = PhotoImage(
            file=("Smartphone_redmi/button_12.png"))
        self.button_12 = Button(
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin2,
            relief="flat"
        )
        self.button_12.place(
            x=0.0,
            y=334.0,
            width=264.0,
            height=44.0
        )

        button_image_13 = PhotoImage(
            file=("Smartphone_redmi/button_13.png"))
        self.button_13 = Button(
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin3,
            relief="flat"
        )
        self.button_13.place(
            x=0.0,
            y=388.0,
            width=264.0,
            height=44.0
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    def loginpoin(self):
        self.window.destroy()
        Smartphone_xiaomi()

    def loginpoin1(self):
        self.window.destroy()
        Smartphone_poco()
    
    def loginpoin2(self):
        self.window.destroy()
        Newarrival_smarthome()

    def loginpoin3(self):
        self.window.destroy()
        Newarrival_lifestyle()

    def redminote12pro5g(self):
        self.window.destroy()
        redminote12pro5g()

    def redminote12(self):
        self.window.destroy()
        redminote12()

    def redmi102022(self):
        self.window.destroy()
        redmi102022()

    def redminote11pro5g(self):
        self.window.destroy()
        redminote11pro5g()

    def redminote11pro(self):
        self.window.destroy()
        redminote11pro()

    def redminote11(self):
        self.window.destroy()
        redminote11()
#=====================================================================================================================================#
class Smarthome_TVmedia:
    def __init__(self):
        self.window = Tk()
        self.window.title("TV&Media")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        button_image_1 = PhotoImage(
            file=("Smarthome_tv&media/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.XiaomiTvA255,
            relief="flat"
        )
        self.button_1.place(
            x=318.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        button_image_2 = PhotoImage(
            file=("Smarthome_tv&media/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.XiaomiTvP1E65,
            relief="flat"
        )
        self.button_2.place(
            x=629.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        button_image_3 = PhotoImage(
            file=("Smarthome_tv&media/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.MiTv443bezelless,
            relief="flat"
        )
        self.button_3.place(
            x=318.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_4 = PhotoImage(
            file=("Smarthome_tv&media/button_4.png"))
        self.button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.MiTvStick,
            relief="flat"
        )
        self.button_4.place(
            x=629.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_5 = PhotoImage(
            file=("Smarthome_tv&media/button_5.png"))
        self.button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.XiaomiTvStick4K,
            relief="flat"
        )
        self.button_5.place(
            x=940.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_6 = PhotoImage(
            file=("Smarthome_tv&media/button_6.png"))
        self.button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.MiTv455,
            relief="flat"
        )
        self.button_6.place(
            x=940.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            264.0,
            832.0,
            fill="#F1EBC9",
            outline="")

        button_image_7 = PhotoImage(
            file=("Smarthome_tv&media/button_7.png"))
        self.button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self.button_7.place(
            x=0.0,
            y=246.0,
            width=264.0,
            height=44.0
        )

        button_image_8 = PhotoImage(
            file=("Smarthome_tv&media/button_8.png"))
        self.button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin,
            relief="flat"
        )
        self.button_8.place(
            x=0.0,
            y=290.0,
            width=264.0,
            height=44.0
        )

        button_image_9 = PhotoImage(
            file=("Smarthome_tv&media/button_9.png"))
        self.button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin1,
            relief="flat"
        )
        self.button_9.place(
            x=0.0,
            y=334.0,
            width=264.0,
            height=44.0
        )

        entry_image_1 = PhotoImage(
            file=("Smarthome_tv&media/entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            731.5,
            40.5,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=523.0,
            y=17.0,
            width=417.0,
            height=45.0
        )

        button_image_10 = PhotoImage(
            file=("Smarthome_tv&media/button_10.png"))
        self.button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        self.button_10.place(
            x=952.0,
            y=17.0,
            width=47.0,
            height=47.0
        )

        self.canvas.create_text(
            87.0,
            102.0,
            anchor="nw",
            text="XIAOMI",
            fill="#000000",
            font=("Lato Black", 24 * -1, "bold")
        )

        button_image_11 = PhotoImage(
            file=("Smarthome_tv&media/button_11.png"))
        self.button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin2,
            relief="flat"
        )
        self.button_11.place(
            x=0.0,
            y=148.0,
            width=264.0,
            height=44.0
        )

        button_image_12 = PhotoImage(
            file=("Smarthome_tv&media/button_12.png"))
        self.button_12 = Button(
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_12 clicked"),
            relief="flat"
        )
        self.button_12.place(
            x=0.0,
            y=202.0,
            width=264.0,
            height=44.0
        )

        button_image_13 = PhotoImage(
            file=("Smarthome_tv&media/button_13.png"))
        self.button_13 = Button(
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin3,
            relief="flat"
        )
        self.button_13.place(
            x=0.0,
            y=388.0,
            width=264.0,
            height=44.0
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    def loginpoin(self):
        self.window.destroy()
        Semarthome_Peralatan_rumah_tangga()

    def loginpoin1(self):
        self.window.destroy()
        Semarthome_Perangkat_pintar()

        
    def loginpoin2(self):
        self.window.destroy()
        Newarrival_smartphone()

    def loginpoin3(self):
        self.window.destroy()
        Newarrival_lifestyle()

    def XiaomiTvA255(self):
        self.window.destroy()
        XiaomiTvA255()

    def XiaomiTvP1E65(self):
        self.window.destroy()
        XiaomiTvP1E65()

    def MiTv455(self):
        self.window.destroy()
        MiTv455()

    def MiTv443bezelless(self):
        self.window.destroy()
        MiTv443bezelless()

    def MiTvStick(self):
        self.window.destroy()
        MiTvStick()

    def XiaomiTvStick4K(self):
        self.window.destroy()
        XiaomiTVStick4K()
#=====================================================================================================================================#
class Semarthome_Peralatan_rumah_tangga:
    def __init__(self):
        self.window = Tk()
        self.window.title("peralatan Rumah Tangga")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        button_image_1 = PhotoImage(
            file=("Smarthome_peralatan rumah tangga/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.XiaomiRobotVacuumE10,
            relief="flat"
        )
        self.button_1.place(
            x=318.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        button_image_2 = PhotoImage(
            file=("Smarthome_peralatan rumah tangga/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.MiVacuumCleanerLight,
            relief="flat"
        )
        self.button_2.place(
            x=629.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        button_image_3 = PhotoImage(
            file=("Smarthome_peralatan rumah tangga/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.MiVacuumCleanerMini,
            relief="flat"
        )
        self.button_3.place(
            x=318.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_4 = PhotoImage(
            file=("Smarthome_peralatan rumah tangga/button_4.png"))
        self.button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.XiaomiAirPurifier4Pro,
            relief="flat"
        )
        self.button_4.place(
            x=629.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_5 = PhotoImage(
            file=("Smarthome_peralatan rumah tangga/button_5.png"))
        self.button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.XiaomiSmartAirPurifier4Lite,
            relief="flat"
        )
        self.button_5.place(
            x=940.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_6 = PhotoImage(
            file=("Smarthome_peralatan rumah tangga/button_6.png"))
        self.button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.MiRobotVacuumMop2Lite,
            relief="flat"
        )
        self.button_6.place(
            x=940.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            264.0,
            832.0,
            fill="#F1EBC9",
            outline="")

        button_image_7 = PhotoImage(
            file=("Smarthome_peralatan rumah tangga/button_7.png"))
        self.button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin,
            relief="flat"
        )
        self.button_7.place(
            x=0.0,
            y=246.0,
            width=264.0,
            height=44.0
        )

        button_image_8 = PhotoImage(
            file=("Smarthome_peralatan rumah tangga/button_8.png"))
        self.button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        self.button_8.place(
            x=0.0,
            y=290.0,
            width=264.0,
            height=44.0
        )

        button_image_9 = PhotoImage(
            file=("Smarthome_peralatan rumah tangga/button_9.png"))
        self.button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin1,
            relief="flat"
        )
        self.button_9.place(
            x=0.0,
            y=334.0,
            width=264.0,
            height=44.0
        )

        entry_image_1 = PhotoImage(
            file=("Smarthome_peralatan rumah tangga/entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            731.5,
            40.5,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=523.0,
            y=17.0,
            width=417.0,
            height=45.0
        )

        button_image_10 = PhotoImage(
            file=("Smarthome_peralatan rumah tangga/button_10.png"))
        self.button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        self.button_10.place(
            x=952.0,
            y=17.0,
            width=47.0,
            height=47.0
        )

        self.canvas.create_text(
            87.0,
            102.0,
            anchor="nw",
            text="XIAOMI",
            fill="#000000",
            font=("Lato Black", 24 * -1,"bold")
        )

        button_image_11 = PhotoImage(
            file=("Smarthome_peralatan rumah tangga/button_11.png"))
        self.button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin2,
            relief="flat"
        )
        self.button_11.place(
            x=0.0,
            y=148.0,
            width=264.0,
            height=44.0
        )

        button_image_12 = PhotoImage(
            file=("Smarthome_peralatan rumah tangga/button_12.png"))
        self.button_12 = Button(
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_12 clicked"),
            relief="flat"
        )
        self.button_12.place(
            x=0.0,
            y=202.0,
            width=264.0,
            height=44.0
        )

        button_image_13 = PhotoImage(
            file=("Smarthome_peralatan rumah tangga/button_13.png"))
        self.button_13 = Button(
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin3,
            relief="flat"
        )
        self.button_13.place(
            x=0.0,
            y=388.0,
            width=264.0,
            height=44.0
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    def loginpoin(self):
        self.window.destroy()
        Smarthome_TVmedia()

    def loginpoin1(self):
        self.window.destroy()
        Semarthome_Perangkat_pintar()
     
    def loginpoin2(self):
        self.window.destroy()
        Newarrival_smartphone()

    
    def loginpoin3(self):
        self.window.destroy()
        Newarrival_lifestyle()

    def XiaomiRobotVacuumE10(self):
        self.window.destroy()
        XiaomiRobotVacuumE10()

    def MiVacuumCleanerLight(self):
        self.window.destroy()
        MiVacuumCleanerLight()

    def MiRobotVacuumMop2Lite(self):
        self.window.destroy()
        MiRobotVacuumMop2Lite()

    def MiVacuumCleanerMini(self):
        self.window.destroy()
        MiVacuumCleanerMini()

    def XiaomiAirPurifier4Pro(self):
        self.window.destroy()
        XiaomiAirPurifier4Pro()

    def XiaomiSmartAirPurifier4Lite(self):
        self.window.destroy()
        XiaomiSmartAirPurifier4Lite()

#=====================================================================================================================================#
class Semarthome_Perangkat_pintar:
    def __init__(self):
        self.window = Tk()
        self.window.title("perangkat Pintar")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
        self.window,
        bg = "#FFFFFF",
        height = 832,
        width = 1280,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.button_image_1 = PhotoImage(
            file=("Smarthome_perangkat_pintar/button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.XiaomiSmartCameraC300,
            relief="flat"
        )
        self.button_1.place(
            x=318.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        button_image_2 = PhotoImage(
            file=("Smarthome_perangkat_pintar/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self. Mi360Camera1080p,
            relief="flat"
        )
        self.button_2.place(
            x=629.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        button_image_3 = PhotoImage(
            file=("Smarthome_perangkat_pintar/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.MiWirelessSwitch,
            relief="flat"
        )
        self.button_3.place(
            x=318.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_4 = PhotoImage(
            file=("Smarthome_perangkat_pintar/button_4.png"))
        self.button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.XiaomiPortableElectronicAirCompressor1S,
            relief="flat"
        )
        self.button_4.place(
            x=629.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        self.button_image_5 = PhotoImage(
            file=("Smarthome_perangkat_pintar/button_5.png"))
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.MiSmartAirFryer,
            relief="flat"
        )
        self.button_5.place(
            x=940.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_6 = PhotoImage(
            file=("Smarthome_perangkat_pintar/button_6.png"))
        self.button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.Mi360HomeSecurityCamera2K,
            relief="flat"
        )
        self.button_6.place(
            x=940.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            264.0,
            832.0,
            fill="#F1EBC9",
            outline="")

        button_image_7 = PhotoImage(
            file=("Smarthome_perangkat_pintar/button_7.png"))
        self.button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin,
            relief="flat"
        )
        self.button_7.place(
            x=0.0,
            y=246.0,
            width=264.0,
            height=44.0
        )

        button_image_8 = PhotoImage(
            file=("Smarthome_perangkat_pintar/button_8.png"))
        self.button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin1,
            relief="flat"
        )
        self.button_8.place(
            x=0.0,
            y=290.0,
            width=264.0,
            height=44.0
        )

        button_image_9 = PhotoImage(
            file=("Smarthome_perangkat_pintar/button_9.png"))
        self.button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            # command=self.loginpoin1,
            relief="flat"
        )
        self.button_9.place(
            x=0.0,
            y=334.0,
            width=264.0,
            height=44.0
        )

        entry_image_1 = PhotoImage(
            file=("Smarthome_perangkat_pintar/entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            731.5,
            40.5,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=523.0,
            y=17.0,
            width=417.0,
            height=45.0
        )

        button_image_10 = PhotoImage(
            file=("Smarthome_perangkat_pintar/button_10.png"))
        self.button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        self.button_10.place(
            x=952.0,
            y=17.0,
            width=47.0,
            height=47.0
        )

        self.canvas.create_text(
            87.0,
            102.0,
            anchor="nw",
            text="XIAOMI",
            fill="#000000",
            font=("Lato Black", 24 * -1, "bold")
        )

        button_image_11 = PhotoImage(
            file=("Smarthome_perangkat_pintar/button_11.png"))
        self.button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin2,
            relief="flat"
        )
        self.button_11.place(
            x=0.0,
            y=148.0,
            width=264.0,
            height=44.0
        )

        button_image_12 = PhotoImage(
            file=("Smarthome_perangkat_pintar/button_12.png"))
        self.button_12 = Button(
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_12 clicked"),
            relief="flat"
        )
        self.button_12.place(
            x=0.0,
            y=202.0,
            width=264.0,
            height=44.0
        )

        button_image_13 = PhotoImage(
            file=("Smarthome_perangkat_pintar/button_13.png"))
        self.button_13 = Button(
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin3,
            relief="flat"
        )
        self.button_13.place(
            x=0.0,
            y=388.0,
            width=264.0,
            height=44.0
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    def loginpoin(self):
        self.window.destroy()
        Smarthome_TVmedia()

    def loginpoin1(self):
        self.window.destroy()
        Semarthome_Peralatan_rumah_tangga()

        
    def loginpoin2(self):
        self.window.destroy()
        Newarrival_smartphone()

    def loginpoin3(self):
        self.window.destroy()
        Newarrival_lifestyle()

    def XiaomiSmartCameraC300(self):
        self.window.destroy()
        XiaomiSmartCameraC300()

    def Mi360Camera1080p(self):
        self.window.destroy()
        Mi360Camera1080p()

    def Mi360HomeSecurityCamera2K(self):
        self.window.destroy()
        Mi360HomeSecurityCamera2K()

    def MiWirelessSwitch(self):
        self.window.destroy()
        MiWirelessSwitch()

    def XiaomiPortableElectronicAirCompressor1S(self):
        self.window.destroy()
        XiaomiPortableElectronicAirCompressor1S()

    def MiSmartAirFryer(self):
        self.window.destroy()
        MiSmartAirFryer()
#=====================================================================================================================================#

class Lifestyle_Wearable:
    def __init__(self):
        self.window = Tk()
        self.window.title("Wearable")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        button_image_1 = PhotoImage(
            file=("Lifestyle_wearable/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.Redmibuds4,
            relief="flat"
        )
        self.button_1.place(
            x=318.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        button_image_2 = PhotoImage(
            file=("Lifestyle_wearable/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.Redmibuds4pro,
            relief="flat"
        )
        self.button_2.place(
            x=629.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        button_image_3 = PhotoImage(
            file=("Lifestyle_wearable/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.RedmiWatch3,
            relief="flat"
        )
        self.button_3.place(
            x=318.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_4 = PhotoImage(
            file=("Lifestyle_wearable/button_4.png"))
        self.button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.XiaomiWatchS1Active,
            relief="flat"
        )
        self.button_4.place(
            x=629.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_5 = PhotoImage(
            file=("Lifestyle_wearable/button_5.png"))
        self.button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.Xiaomismartband7,
            relief="flat"
        )
        self.button_5.place(
            x=940.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_6 = PhotoImage(
            file=("Lifestyle_wearable/button_6.png"))
        self.button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.RedmiBuds3Pro,
            relief="flat"
        )
        self.button_6.place(
            x=940.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            264.0,
            832.0,
            fill="#F1EBC9",
            outline="")

        button_image_7 = PhotoImage(
            file=("Lifestyle_wearable/button_7.png"))
        self.button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_7 clicked"),
            relief="flat"
        )
        self.button_7.place(
            x=0.0,
            y=300.0,
            width=264.0,
            height=44.0
        )

        button_image_8 = PhotoImage(
            file=("Lifestyle_wearable/button_8.png"))
        self.button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin,
            relief="flat"
        )
        self.button_8.place(
            x=0.0,
            y=344.0,
            width=264.0,
            height=44.0
        )

        button_image_9 = PhotoImage(
            file=("Lifestyle_wearable/button_9.png"))
        self.button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin1,
            relief="flat"
        )
        self.button_9.place(
            x=0.0,
            y=388.0,
            width=264.0,
            height=44.0
        )

        entry_image_1 = PhotoImage(
            file=("Lifestyle_wearable/entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            731.5,
            40.5,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=523.0,
            y=17.0,
            width=417.0,
            height=45.0
        )

        button_image_10 = PhotoImage(
            file=("Lifestyle_wearable/button_10.png"))
        self.button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        self.button_10.place(
            x=952.0,
            y=17.0,
            width=47.0,
            height=47.0
        )

        self.canvas.create_text(
            87.0,
            102.0,
            anchor="nw",
            text="XIAOMI",
            fill="#000000",
            font=("Lato Black", 24 * -1,"bold")
        )

        button_image_11 = PhotoImage(
            file=("Lifestyle_wearable/button_11.png"))
        self.button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin2,
            relief="flat"
        )
        self.button_11.place(
            x=0.0,
            y=148.0,
            width=264.0,
            height=44.0
        )

        button_image_12 = PhotoImage(
            file=("Lifestyle_wearable/button_12.png"))
        self.button_12 = Button(
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin3,
            relief="flat"
        )
        self.button_12.place(
            x=0.0,
            y=202.0,
            width=264.0,
            height=44.0
        )

        button_image_13 = PhotoImage(
            file=("Lifestyle_wearable/button_13.png"))
        self.button_13 = Button(
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_13 clicked"),
            relief="flat"
        )
        self.button_13.place(
            x=0.0,
            y=256.0,
            width=264.0,
            height=44.0
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    def loginpoin(self):
        self.window.destroy()
        Lifestyle_Kantor()

    def loginpoin1(self):
        self.window.destroy()
        Lifestyle_Aksesoris()

        
    def loginpoin2(self):
        self.window.destroy()
        Newarrival_smartphone()

    def loginpoin3(self):
        self.window.destroy()
        Newarrival_smarthome()

    def Redmibuds4(self):
        self.window.destroy()
        Redmibuds4()

    def Redmibuds4pro(self):
        self.window.destroy()
        Redmibuds4pro()

    def RedmiBuds3Pro(self):
        self.window.destroy()
        RedmiBuds3Pro()

    def RedmiWatch3(self):
        self.window.destroy()
        RedmiWatch3()

    def XiaomiWatchS1Active(self):
        self.window.destroy()
        XiaomiWatchS1Active()

    def Xiaomismartband7(self):
        self.window.destroy()
        Xiaomismartband7()

#=====================================================================================================================================#
class Lifestyle_Kantor:
    def __init__(self):
        self.window = Tk()
        self.window.title("Kantor")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        button_image_1 = PhotoImage(
            file=("Lifestyle_kantor/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.RedmiPad,
            relief="flat"
        )
        self.button_1.place(
            x=318.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        button_image_2 = PhotoImage(
            file=("Lifestyle_kantor/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.RedmiBook15,
            relief="flat"
        )
        self.button_2.place(
            x=629.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        button_image_3 = PhotoImage(
            file=("Lifestyle_kantor/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.MiRouter4C,
            relief="flat"
        )
        self.button_3.place(
            x=318.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_4 = PhotoImage(
            file=("Lifestyle_kantor/button_4.png"))
        self.button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.MiDesktopMonitor27,
            relief="flat"
        )
        self.button_4.place(
            x=629.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_5 = PhotoImage(
            file=("Lifestyle_kantor/button_5.png"))
        self.button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.MiWiFiRangeExtenderAC1200,
            relief="flat"
        )
        self.button_5.place(
            x=940.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_6 = PhotoImage(
            file=("Lifestyle_kantor/button_6.png"))
        self.button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.MiCurvedGamingMonitor34,
            relief="flat"
        )
        self.button_6.place(
            x=940.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            264.0,
            832.0,
            fill="#F1EBC9",
            outline="")

        button_image_7 = PhotoImage(
            file=("Lifestyle_kantor/button_7.png"))
        self.button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin,
            relief="flat"
        )
        self.button_7.place(
            x=0.0,
            y=300.0,
            width=264.0,
            height=44.0
        )

        button_image_8 = PhotoImage(
            file=("Lifestyle_kantor/button_8.png"))
        self.button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_8 clicked"),
            relief="flat"
        )
        self.button_8.place(
            x=0.0,
            y=344.0,
            width=264.0,
            height=44.0
        )

        button_image_9 = PhotoImage(
            file=("Lifestyle_kantor/button_9.png"))
        self.button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin1,
            relief="flat"
        )
        self.button_9.place(
            x=0.0,
            y=388.0,
            width=264.0,
            height=44.0
        )

        entry_image_1 = PhotoImage(
            file=("Lifestyle_kantor/entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            731.5,
            40.5,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=523.0,
            y=17.0,
            width=417.0,
            height=45.0
        )

        button_image_10 = PhotoImage(
            file=("Lifestyle_kantor/button_10.png"))
        self.button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        self.button_10.place(
            x=952.0,
            y=17.0,
            width=47.0,
            height=47.0
        )

        self.canvas.create_text(
            87.0,
            102.0,
            anchor="nw",
            text="XIAOMI",
            fill="#000000",
            font=("Lato Black", 24 * -1, "bold")
        )

        button_image_11 = PhotoImage(
            file=("Lifestyle_kantor/button_11.png"))
        self.button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
             command=self.loginpoin2,
            relief="flat"
        )
        self.button_11.place(
            x=0.0,
            y=148.0,
            width=264.0,
            height=44.0
        )

        button_image_12 = PhotoImage(
            file=("Lifestyle_kantor/button_12.png"))
        self.button_12 = Button(
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin3,
            relief="flat"
        )
        self.button_12.place(
            x=0.0,
            y=202.0,
            width=264.0,
            height=44.0
        )

        button_image_13 = PhotoImage(
            file=("Lifestyle_kantor/button_13.png"))
        self.button_13 = Button(
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_13 clicked"),
            relief="flat"
        )
        self.button_13.place(
            x=0.0,
            y=256.0,
            width=264.0,
            height=44.0
        )

        self.window.resizable(False, False)
        self.window.mainloop()


    def loginpoin(self):
        self.window.destroy()
        Lifestyle_Wearable()


    def loginpoin1(self):
        self.window.destroy()
        Lifestyle_Aksesoris()

        
    def loginpoin2(self):
        self.window.destroy()
        Newarrival_smartphone()

    def loginpoin3(self):
        self.window.destroy()
        Newarrival_smarthome()

    def RedmiPad(self):
        self.window.destroy()
        RedmiPad()

    def RedmiBook15(self):
        self.window.destroy()
        RedmiBook15()

    def MiCurvedGamingMonitor34(self):
        self.window.destroy()
        MiCurvedGamingMonitor34()

    def MiRouter4C(self):
        self.window.destroy()
        MiRouter4C()

    def MiDesktopMonitor27(self):
        self.window.destroy()
        MiDesktopMonitor27()

    def MiWiFiRangeExtenderAC1200(self):
        self.window.destroy()
        MiWiFiRangeExtenderAC1200()
#=====================================================================================================================================#
class Lifestyle_Aksesoris:
    def __init__(self):
        self.window = Tk()
        self.window.title("Kantor")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")



        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.button_image_1 = PhotoImage(
            file=("Lifestyle_Aksesoris/button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.Xiaomi22WPowerBank10000mAh,
            relief="flat"
        )
        self.button_1.place(
            x=318.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        button_image_2 = PhotoImage(
            file=("Lifestyle_Aksesoris/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.Mi37WDualPortCarCharger,
            relief="flat"
        )
        self.button_2.place(
            x=629.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        button_image_3 = PhotoImage(
            file=("Lifestyle_Aksesoris/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Xiaomi67WChargingComboTypeAEU,
            relief="flat"
        )
        self.button_3.place(
            x=318.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_4 = PhotoImage(
            file=("Lifestyle_Aksesoris/button_4.png"))
        self.button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.MiWatchChargingDock,
            relief="flat"
        )
        self.button_4.place(
            x=629.0,
            y=452.0,
            width=273.0,
            height=307.0
        )

        button_image_5 = PhotoImage(
            file=("Lifestyle_Aksesoris/button_5.png"))
        self.button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.MiLCDWritingTablet,
            relief="flat"
        )
        self.button_5.place(
            x=940.0,
            y=452.0,
            width=273.0,
            height=309.0
        )

        button_image_6 = PhotoImage(
            file=("Lifestyle_Aksesoris/button_6.png"))
        self.button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.Xiaomi6ATypeAtoTypeCCable,
            relief="flat"
        )
        self.button_6.place(
            x=940.0,
            y=94.0,
            width=273.0,
            height=309.0
        )

        self.canvas.create_rectangle(
            0.0,
            0.0,
            264.0,
            832.0,
            fill="#F1EBC9",
            outline="")

        button_image_7 = PhotoImage(
            file=("Lifestyle_Aksesoris/button_7.png"))
        self.button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin,
            relief="flat"
        )
        self.button_7.place(
            x=0.0,
            y=300.0,
            width=264.0,
            height=44.0
        )

        button_image_8 = PhotoImage(
            file=("Lifestyle_Aksesoris/button_8.png"))
        self.button_8 = Button(
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=self.loginpoin1,
            relief="flat"
        )
        self.button_8.place(
            x=0.0,
            y=344.0,
            width=264.0,
            height=44.0
        )

        button_image_9 = PhotoImage(
            file=("Lifestyle_Aksesoris/button_9.png"))
        self.button_9 = Button(
            image=button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        self.button_9.place(
            x=0.0,
            y=388.0,
            width=264.0,
            height=44.0
        )

        entry_image_1 = PhotoImage(
            file=("Lifestyle_Aksesoris/entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            731.5,
            40.5,
            image=entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_1.place(
            x=523.0,
            y=17.0,
            width=417.0,
            height=45.0
        )

        button_image_10 = PhotoImage(
            file=("Lifestyle_Aksesoris/button_10.png"))
        self.button_10 = Button(
            image=button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_10 clicked"),
            relief="flat"
        )
        self.button_10.place(
            x=952.0,
            y=17.0,
            width=47.0,
            height=47.0
        )

        self.canvas.create_text(
            87.0,
            102.0,
            anchor="nw",
            text="XIAOMI",
            fill="#000000",
            font=("Lato Black", 24 * -1, "bold")
        )

        button_image_11 = PhotoImage(
            file=("Lifestyle_Aksesoris/button_11.png"))
        self.button_11 = Button(
            image=button_image_11,
            borderwidth=0,
            highlightthickness=0,
             command=self.loginpoin2,
            relief="flat"
        )
        self.button_11.place(
            x=0.0,
            y=148.0,
            width=264.0,
            height=44.0
        )

        button_image_12 = PhotoImage(
            file=("Lifestyle_Aksesoris/button_12.png"))
        self.button_12 = Button(
            image=button_image_12,
            borderwidth=0,
            highlightthickness=0,
             command=self.loginpoin3,
            relief="flat"
        )
        self.button_12.place(
            x=0.0,
            y=202.0,
            width=264.0,
            height=44.0
        )

        button_image_13 = PhotoImage(
            file=("Lifestyle_Aksesoris/button_13.png"))
        self.button_13 = Button(
            image=button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_13 clicked"),
            relief="flat"
        )
        self.button_13.place(
            x=0.0,
            y=256.0,
            width=264.0,
            height=44.0
        )

        self.window.resizable(False, False)
        self.window.mainloop()

    def loginpoin(self):
        self.window.destroy()
        Lifestyle_Wearable()


    def loginpoin1(self):
        self.window.destroy()
        Lifestyle_Kantor()

        
    def loginpoin2(self):
        self.window.destroy()
        Newarrival_smartphone()

    def loginpoin3(self):
        self.window.destroy()
        Newarrival_smarthome()

    def Xiaomi22WPowerBank10000mAh(self):
        self.window.destroy()
        Xiaomi22WPowerBank10000mAh()

    def Mi37WDualPortCarCharger(self):
        self.window.destroy()
        Mi37WDualPortCarCharger()

    def Xiaomi6ATypeAtoTypeCCable(self):
        self.window.destroy()
        Xiaomi6ATypeAtoTypeCCable()

    def Xiaomi67WChargingComboTypeAEU(self):
        self.window.destroy()
        Xiaomi67WChargingComboTypeAEU()

    def MiWatchChargingDock(self):
        self.window.destroy()
        MiWatchChargingDock()

    def MiLCDWritingTablet(self):
        self.window.destroy()
        MiLCDWritingTablet()


#=====================================================================================================================================#
class Xiaomi12Lite5G:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi 12 Lite 5G")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("xiaomi12lite5G/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=("xiaomi12lite5G/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        image_image_2 = PhotoImage(
            file=("xiaomi12lite5G/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_2 = PhotoImage(
            file=("xiaomi12lite5G/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("xiaomi12lite5G/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.40325927734375,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smartphone_xiaomi()

    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()

    def Payment(self):
        self.window.destroy()
        Payment()

#=====================================================================================================================================#
class Xiaomi12pro:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi 12 Pro")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("xiaomi12pro/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=("xiaomi12pro/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("xiaomi12pro/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        image_image_2 = PhotoImage(
            file=("xiaomi12pro/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_3 = PhotoImage(
            file=("xiaomi12pro/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smartphone_xiaomi()
    

    def TelegramBotGUI(self):
        self.window.destroy()
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    
    def Payment(self):
        self.window.destroy()
        Payment()

#=====================================================================================================================================#
class Xiaomi12:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi 12")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Xiaomi12/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Xiaomi12/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Xiaomi12/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Xiaomi12/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Xiaomi12/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smartphone_xiaomi()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()


    def Payment(self):
        self.window.destroy()
        Payment()


#=====================================================================================================================================#

class Xiaomi10t:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi 10 T Pro")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("xiaomi 10t/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=("xiaomi 10t/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        image_image_2 = PhotoImage(
            file=("xiaomi 10t/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_2 = PhotoImage(
            file=("xiaomi 10t/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("xiaomi 10t/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smartphone_xiaomi()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()

    def Payment(self):
        self.window.destroy()
        Payment()

#=====================================================================================================================================#
class Xiaomi11tpro:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi 11 T pro")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")



        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("xiaomi11tpro/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=("xiaomi11tpro/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        image_image_2 = PhotoImage(
            file=("xiaomi11tpro/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_2 = PhotoImage(
            file=("xiaomi11tpro/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("xiaomi11tpro/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smartphone_xiaomi()


    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
    
#=====================================================================================================================================#

class Xiaomi11t:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi 11 T")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")



        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("xiaomi11t/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=("xiaomi11t/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        image_image_2 = PhotoImage(
            file=("xiaomi11t/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_2 = PhotoImage(
            file=("xiaomi11t/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("xiaomi11t/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()


    def back(self):
        self.window.destroy()
        Smartphone_xiaomi()


    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()

#=====================================================================================================================================#

class PocoX55G:
    def __init__(self):
        self.window = Tk()
        self.window.title("Poco X5 5G")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("poco x5 5g/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=("poco x5 5g/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        image_image_2 = PhotoImage(
            file=("poco x5 5g/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_2 = PhotoImage(
            file=("poco x5 5g/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
           command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("poco x5 5g/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smartphone_poco()


    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#

class Pocof4:
    def __init__(self):
        self.window = Tk()
        self.window.title("Poco F4")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("pocof4/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        button_image_1 = PhotoImage(
            file=("pocof4/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        image_image_2 = PhotoImage(
            file=("pocof4/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_3 = PhotoImage(
            file=("pocof4/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()


    def back(self):
        self.window.destroy()
        Smartphone_poco()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#


class Pocof4:
    def __init__(self):
        self.window = Tk()
        self.window.title("Poco F4")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")


        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("poco m4 pro/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("poco m4 pro/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("poco m4 pro/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("poco m4 pro/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("poco m4 pro/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smartphone_poco()

    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#

class pocoM5s:
    def __init__(self):
        self.window = Tk()
        self.window.title("Poco M5s")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("poco m5s/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("poco m5s/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("poco m5s/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("poco m5s/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("poco m5s/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smartphone_poco()
    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()

#=====================================================================================================================================#
class pocoM5:
    def __init__(self):
        self.window = Tk()
        self.window.title("Poco M5")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("poco m5/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("poco m5/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("poco m5/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("poco m5/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("poco m5/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smartphone_poco()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#

class pocof4gt:
    def __init__(self):
        self.window = Tk()
        self.window.title("Poco F4 GT")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("poco f4 gt/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("poco f4 gt/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("poco f4 gt/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("poco f4 gt/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("poco f4 gt/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smartphone_poco()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#

class redminote12pro5g:
    def __init__(self):
        self.window = Tk()
        self.window.title("Redmi Note 12 Pro 5G")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("redmi note 12 pro 5g/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("redmi note 12 pro 5g/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("redmi note 12 pro 5g/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("redmi note 12 pro 5g/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("redmi note 12 pro 5g/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smartphone_redmi()

    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()

#=====================================================================================================================================#

class redminote12:
    def __init__(self):
        self.window = Tk()
        self.window.title("Redmi Note 12")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("redmi note 12/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("redmi note 12/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("redmi note 12/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("redmi note 12/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("redmi note 12/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smartphone_redmi()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#

class redmi102022:
    def __init__(self):
        self.window = Tk()
        self.window.title("Redmi 10 2022")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("redmi 10 2022/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("redmi 10 2022/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("redmi 10 2022/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("redmi 10 2022/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("redmi 10 2022/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smartphone_redmi()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()

#=====================================================================================================================================#
class redminote11pro5g:
    def __init__(self):
        self.window = Tk()
        self.window.title("Redmi Note 11 Pro 5G")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("redmi note 11 pro 5g/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("redmi note 11 pro 5g/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("redmi note 11 pro 5g/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("redmi note 11 pro 5g/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("redmi note 11 pro 5g/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smartphone_redmi()
    
     
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class redminote11pro:
    def __init__(self):
        self.window = Tk()
        self.window.title("Redmi Note 11 Pro")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("redmi note 11 pro/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("redmi note 11 pro/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("redmi note 11 pro/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("redmi note 11 pro/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("redmi note 11 pro/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smartphone_redmi()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class redminote11:
    def __init__(self):
        self.window = Tk()
        self.window.title("Redmi Note 11")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("redmi note 11/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("redmi note 11/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("redmi note 11/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("redmi note 11/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("redmi note 11/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smartphone_redmi()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class XiaomiTvA255:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi TV A2 55")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("XIAOMI TV A2 55/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("XIAOMI TV A2 55/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("XIAOMI TV A2 55/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("XIAOMI TV A2 55/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("XIAOMI TV A2 55/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smarthome_TVmedia()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class XiaomiTvP1E65:
    def __init__(self):
        self.window = Tk()
        self.window.title("XIAOMI TV P1E 65")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("XIAOMI TV P1E 65/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("XIAOMI TV P1E 65/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("XIAOMI TV P1E 65/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("XIAOMI TV P1E 65/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("XIAOMI TV P1E 65/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smarthome_TVmedia()


    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()

#=====================================================================================================================================#
class MiTv455:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi TV 4 55")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Mi TV 4 55/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Mi TV 4 55/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi TV 4 55/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi TV 4 55/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi TV 4 55/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smarthome_TVmedia()


    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class MiTv443bezelless:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi TV 4 55")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Mi TV 4 43 bezel-less/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Mi TV 4 43 bezel-less/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi TV 4 43 bezel-less/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi TV 4 43 bezel-less/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi TV 4 43 bezel-less/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smarthome_TVmedia()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class MiTvStick:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi TV Stick")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Mi TV Stick/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Mi TV Stick/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi TV Stick/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi TV Stick/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi TV Stick/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smarthome_TVmedia()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class XiaomiTVStick4K:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi TV Stick 4K")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Xiaomi TV Stick 4K/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Xiaomi TV Stick 4K/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Xiaomi TV Stick 4K/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Xiaomi TV Stick 4K/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Xiaomi TV Stick 4K/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Smarthome_TVmedia()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class XiaomiRobotVacuumE10:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi Robot Vacuum E10")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Xiaomi Robot Vacuum E10/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Xiaomi Robot Vacuum E10/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Xiaomi Robot Vacuum E10/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Xiaomi Robot Vacuum E10/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Xiaomi Robot Vacuum E10/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Semarthome_Peralatan_rumah_tangga()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class XiaomiRobotVacuumE10:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi Robot Vacuum E10")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Xiaomi Robot Vacuum E10/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Xiaomi Robot Vacuum E10/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Xiaomi Robot Vacuum E10/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Xiaomi Robot Vacuum E10/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Xiaomi Robot Vacuum E10/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Semarthome_Peralatan_rumah_tangga()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class MiVacuumCleanerLight:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi Vacuum Cleaner Light")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Mi Vacuum Cleaner Light/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Mi Vacuum Cleaner Light/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi Vacuum Cleaner Light/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi Vacuum Cleaner Light/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi Vacuum Cleaner Light/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Semarthome_Peralatan_rumah_tangga()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class MiRobotVacuumMop2Lite:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi Robot Vacuum-Mop 2 Lite")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Mi Robot Vacuum-Mop 2 Lite/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Mi Robot Vacuum-Mop 2 Lite/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi Robot Vacuum-Mop 2 Lite/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi Robot Vacuum-Mop 2 Lite/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi Robot Vacuum-Mop 2 Lite/button_2.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Semarthome_Peralatan_rumah_tangga()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class MiVacuumCleanerMini:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi Vacuum Cleaner Mini")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Mi Vacuum Cleaner Mini/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Mi Vacuum Cleaner Mini/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi Vacuum Cleaner Light/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi Vacuum Cleaner Light/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi Vacuum Cleaner Light/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Semarthome_Peralatan_rumah_tangga()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class XiaomiAirPurifier4Pro:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi Air Purifier 4 Pro")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Xiaomi Air Purifier 4 Pro/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Xiaomi Air Purifier 4 Pro/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Xiaomi Air Purifier 4 Pro/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Xiaomi Air Purifier 4 Pro/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Xiaomi Air Purifier 4 Pro/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Semarthome_Peralatan_rumah_tangga()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class XiaomiSmartAirPurifier4Lite:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi Smart Air Purifier 4 Lite")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Xiaomi Smart Air Purifier 4 Lite/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Xiaomi Smart Air Purifier 4 Lite/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Xiaomi Air Purifier 4 Pro/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Xiaomi Air Purifier 4 Pro/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Xiaomi Air Purifier 4 Pro/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Semarthome_Peralatan_rumah_tangga()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()

#=====================================================================================================================================#
class XiaomiSmartCameraC300:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi Smart Camera C300")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Xiaomi Smart Camera C300/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Xiaomi Smart Camera C300/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Xiaomi Smart Camera C300/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Xiaomi Smart Camera C300/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Xiaomi Smart Camera C300/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Semarthome_Perangkat_pintar()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class Mi360Camera1080p:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi 360° Camera (1080p)")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Mi 360° Camera (1080p)/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Mi 360° Camera (1080p)/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi 360° Camera (1080p)/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi 360° Camera (1080p)/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi 360° Camera (1080p)/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Semarthome_Perangkat_pintar()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class Mi360HomeSecurityCamera2K:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi 360° Home Security Camera 2K")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Mi 360° Home Security Camera 2K/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Mi 360° Home Security Camera 2K/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi 360° Home Security Camera 2K/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi 360° Home Security Camera 2K/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi 360° Home Security Camera 2K/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Semarthome_Perangkat_pintar()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class MiWirelessSwitch:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi Wireless Switch")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Mi Wireless Switch/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Mi Wireless Switch/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi Wireless Switch/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi Wireless Switch/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi Wireless Switch/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Semarthome_Perangkat_pintar()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class XiaomiPortableElectronicAirCompressor1S:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi Portable Electronic Air Compressor 1S")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Xiaomi Portable Electronic Air Compressor 1S/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Xiaomi Portable Electronic Air Compressor 1S/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Xiaomi Portable Electronic Air Compressor 1S/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Xiaomi Portable Electronic Air Compressor 1S/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Xiaomi Portable Electronic Air Compressor 1S/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Semarthome_Perangkat_pintar()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class MiSmartAirFryer:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi Smart Air Fryer 3.5L")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Mi Smart Air Fryer 3.5L/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Mi Smart Air Fryer 3.5L/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi Smart Air Fryer 3.5L/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi Smart Air Fryer 3.5L/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi Smart Air Fryer 3.5L/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Semarthome_Perangkat_pintar()
   
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class Redmibuds4:
    def __init__(self):
        self.window = Tk()
        self.window.title("Redmi buds 4")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Redmi buds 4/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Redmi buds 4/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Redmi buds 4/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Redmi buds 4/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Redmi buds 4/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Wearable()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class Redmibuds4pro:
    def __init__(self):
        self.window = Tk()
        self.window.title("Redmi buds 4 Pro")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Redmi buds 4 Pro/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Redmi buds 4 Pro/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Redmi buds 4 Pro/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Redmi buds 4 Pro/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Redmi buds 4 Pro/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Wearable()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class RedmiBuds3Pro:
    def __init__(self):
        self.window = Tk()
        self.window.title("Redmi Buds 3 Pro")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Redmi Buds 3 Pro/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Redmi Buds 3 Pro/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Redmi Buds 3 Pro/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Redmi Buds 3 Pro/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Redmi Buds 3 Pro/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Wearable()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class RedmiBuds3Pro:
    def __init__(self):
        self.window = Tk()
        self.window.title("Redmi Buds 3 Pro")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Redmi Buds 3 Pro/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Redmi Buds 3 Pro/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Redmi Buds 3 Pro/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Redmi Buds 3 Pro/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Redmi Buds 3 Pro/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Wearable()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class RedmiWatch3:
    def __init__(self):
        self.window = Tk()
        self.window.title("Redmi Watch 3")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Redmi Watch 3/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Redmi Watch 3/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Redmi Watch 3/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Redmi Watch 3/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Redmi Watch 3/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Wearable()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class XiaomiWatchS1Active:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi Watch S1 Active")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Xiaomi Watch S1 Active/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Xiaomi Watch S1 Active/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Xiaomi Watch S1 Active/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Xiaomi Watch S1 Active/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Xiaomi Watch S1 Active/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Wearable()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class Xiaomismartband7:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi smart band 7")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Xiaomi smart band 7/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Xiaomi smart band 7/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Xiaomi smart band 7/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Xiaomi smart band 7/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Xiaomi smart band 7/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Wearable()
    

    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class RedmiPad:
    def __init__(self):
        self.window = Tk()
        self.window.title("Redmi Pad")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Redmi pad/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Redmi pad/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Redmi pad/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Redmi pad/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Redmi pad/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Kantor()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class RedmiBook15:
    def __init__(self):
        self.window = Tk()
        self.window.title("RedmiBook 15")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("RedmiBook 15/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("RedmiBook 15/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("RedmiBook 15/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("RedmiBook 15/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("RedmiBook 15/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Kantor()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class MiCurvedGamingMonitor34:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi Curved Gaming Monitor 34")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("MiCurvedGamingMonitor34/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("MiCurvedGamingMonitor34/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("MiCurvedGamingMonitor34/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("MiCurvedGamingMonitor34/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("MiCurvedGamingMonitor34/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Kantor()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class MiRouter4C:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi Router 4C")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Mi Router 4C/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Mi Router 4C/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi Router 4C/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi Router 4C/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi Router 4C/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Kantor()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class MiDesktopMonitor27:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi Desktop Monitor 27”")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Mi Desktop Monitor 27”/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Mi Desktop Monitor 27”/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi Router 4C/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi Router 4C/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi Router 4C/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Kantor()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class MiWiFiRangeExtenderAC1200:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi WiFi Range Extender AC1200")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Mi WiFi Range Extender AC1200/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Mi WiFi Range Extender AC1200/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi Router 4C/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi Router 4C/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi Router 4C/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Kantor()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class Xiaomi22WPowerBank10000mAh:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi 22.5W Power Bank 10000mAh")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Xiaomi 22.5W Power Bank 10000mAh/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Xiaomi 22.5W Power Bank 10000mAh/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi Router 4C/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi Router 4C/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi Router 4C/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Aksesoris()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class Mi37WDualPortCarCharger:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi 37W Dual-Port Car Charger")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Mi 37W Dual-Port Car Charger/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Mi 37W Dual-Port Car Charger/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi 37W Dual-Port Car Charger/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi 37W Dual-Port Car Charger/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi 37W Dual-Port Car Charger/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class Xiaomi6ATypeAtoTypeCCable:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi 6A Type-A to Type-C Cable")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Xiaomi 6A Type-A to Type-C Cable/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Xiaomi 6A Type-A to Type-C Cable/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Xiaomi 6A Type-A to Type-C Cable/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Xiaomi 6A Type-A to Type-C Cable/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Xiaomi 6A Type-A to Type-C Cable/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Aksesoris()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class Xiaomi67WChargingComboTypeAEU:
    def __init__(self):
        self.window = Tk()
        self.window.title("Xiaomi 67W Charging Combo (Type-A) EU")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Xiaomi 67W Charging Combo (Type-A) EU/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Xiaomi 67W Charging Combo (Type-A) EU/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Xiaomi 6A Type-A to Type-C Cable/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Xiaomi 6A Type-A to Type-C Cable/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Xiaomi 6A Type-A to Type-C Cable/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Aksesoris()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class MiWatchChargingDock:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi Watch Charging Dock")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Mi Watch Charging Dock/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Mi Watch Charging Dock/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi Watch Charging Dock/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi Watch Charging Dock/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi Watch Charging Dock/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Aksesoris()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#
class MiLCDWritingTablet:
    def __init__(self):
        self.window = Tk()
        self.window.title("Mi LCD Writing Tablet 13.5&quot")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 832,
            width = 1280,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        image_image_1 = PhotoImage(
            file=("Mi LCD Writing Tablet 13.5&quot/image_1.png"))
        self.image_1 = self.canvas.create_image(
            320.0,
            416.0,
            image=image_image_1
        )

        image_image_2 = PhotoImage(
            file=("Mi LCD Writing Tablet 13.5&quot/image_2.png"))
        self.image_2 = self.canvas.create_image(
            957.0,
            343.0,
            image=image_image_2
        )

        button_image_1 = PhotoImage(
            file=("Mi Watch Charging Dock/button_1.png"))
        self.button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.back,
            relief="flat"
        )
        self.button_1.place(
            x=0.0,
            y=0.0,
            width=35.0,
            height=30.0
        )

        button_image_2 = PhotoImage(
            file=("Mi Watch Charging Dock/button_2.png"))
        self.button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.TelegramBotGUI,
            relief="flat"
        )
        self.button_2.place(
            x=699.0,
            y=669.0,
            width=195.283447265625,
            height=53.4000244140625
        )

        button_image_3 = PhotoImage(
            file=("Mi Watch Charging Dock/button_3.png"))
        self.button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.Payment,
            relief="flat"
        )
        self.button_3.place(
            x=1021.0,
            y=668.0,
            width=195.4033203125,
            height=53.4000244140625
        )
        self.window.resizable(False, False)
        self.window.mainloop()

    def back(self):
        self.window.destroy()
        Lifestyle_Aksesoris()

    
    def TelegramBotGUI(self):
        self.window.destroy()  # Menutup jendela App setelah login berhasil
        self.bot_gui = TelegramBotGUI(None)  # Create a placeholder instance of TelegramBotGUI
        bot = TelegramBot(token, self.bot_gui)  # Pass the self.bot_gui instance as an argument
        self.bot_gui.bot = bot  # Update the self.bot_gui instance with the TelegramBot instance
        self.bot_gui.run()
    def Payment(self):
        self.window.destroy()
        Payment()
#=====================================================================================================================================#

class HappyShopping:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Happy shopping")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")
    

        self.canvas = Canvas(self.window,bg="#FFFFFF",height=832,width=1280,bd=0,highlightthickness=0,relief="ridge")
        self.canvas.place(x=0, y=0)
        self.create_rectangles()
        self.create_buttons()
        self.create_entry()
        
        self.window.resizable(True, True)
        self.window.mainloop()

    def create_rectangles(self):
        self.canvas.create_rectangle(318.0,351.0,591.0,403.0,fill="#F1EBC9",outline="")
        self.canvas.create_rectangle(318.0,709.0,591.0,761.0,fill="#F1EBC9",outline="")
        self.canvas.create_rectangle(629.0,709.0,902.0,761.0,fill="#F1EBC9",outline="")
        self.canvas.create_rectangle(940.0,709.0,1213.0,761.0,fill="#F1EBC9",outline="")
        self.canvas.create_rectangle(629.0,351.0,902.0,403.0,fill="#F1EBC9",outline="")
        self.canvas.create_rectangle(940.0,351.0,1213.0,403.0,fill="#F1EBC9",outline="")
        self.canvas.create_rectangle(0.0,0.0,264.0,832.0,fill="#F1EBC9",outline="")

    def create_buttons(self):
        button_image_1 = PhotoImage(file=("button_1_ktg.png"))
        self.button_1 = Button(image=button_image_1,borderwidth=0,highlightthickness=0,command=self.button1,relief="flat")
        self.button_1.place(x=940.0,y=452.0,width=273.0,height=257.0)

        button_image_2 = PhotoImage(file=("button_2_ktg.png"))
        self.button_2 = Button(image=button_image_2,borderwidth=0, highlightthickness=0,command=self.button2, relief="flat")
        self.button_2.place(x=940.0,y=94.0,width=273.0,height=257.0)

        button_image_3 = PhotoImage(file=("button_3_ktg.png"))
        self.button_3 = Button(image=button_image_3,borderwidth=0,highlightthickness=0,command=self.button3,relief="flat")
        self.button_3.place(x=629.0,y=452.0,width=273.0,height=257.0)

        button_image_4 = PhotoImage(file=("button_4_ktg.png"))
        self.button_4 = Button(image=button_image_4,borderwidth=0,highlightthickness=0,command=self.button4,relief="flat")
        self.button_4.place(x=318.0,y=452.0,width=273.0,height=257.0)

        button_image_5 = PhotoImage(file=("button_5_ktg.png"))
        self.button_5 = Button(image=button_image_5,borderwidth=0,highlightthickness=0,command=self.button5,relief="flat")
        self.button_5.place(x=318.0,y=94.0,width=273.0,height=257.0)

        button_image_6 = PhotoImage(file=("button_6_ktg.png"))
        self.button_6 = Button(image=button_image_6,borderwidth=0,highlightthickness=0,command=self.button6,relief="flat")
        self.button_6.place(x=629.0,y=94.0,width=273.0,height=257.0)

        entry_image_1 = PhotoImage(file=("entry_Search.png"))
        self.entry_bg_1 = self.canvas.create_image(731.5, 40.5, image=entry_image_1)
        self.entry_1 = Entry(bd=0,bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.entry_1.place(x=523.0, y=17.0, width=417.0, height=45.0)

        button_image_7 = PhotoImage(file=("button_Search.png"))
        self.button_7 = Button(image=button_image_7,borderwidth=0,highlightthickness=0,command=lambda: print("button_7 clicked"),relief="flat")
        self.button_7.place(x=952.0, y=17.0, width=47.0, height=47.0)

        

        self.window.resizable(True, False)
        self.window.mainloop()

    def button1(self):
        self.window.destroy()
        Checkout()

    def button2(self):
        self.window.destroy()
        Checkout()

    def button3(self):
        self.window.destroy()
        Checkout()

    def button4(self):
        self.window.destroy()
        Checkout()

    def button5(self):
        self.window.destroy()
        Checkout()

    def button6(self):
        self.window.destroy()
        Checkout()

#=====================================================================================================================================#

class Checkout:
    def __init__(self):
        self.window = Tk()
        self.window.title("Checkout")
        self.window.geometry("1280x832")
        self.window.configure(bg = "#FFFFFF")


        self.canvas = Canvas(self.window, bg = "#FFFFFF", height = 832, width = 1280, bd = 0, highlightthickness = 0, relief = "ridge" )
        self.canvas.place(x = 0, y = 0)
        self.canvas.create_rectangle(0.0, 0.0, 640.0, 832.0, fill="#000000", outline="")
        self.canvas.create_rectangle(699.0, 61.0, 1216.0, 626.0, fill="#F1EBC9", outline="")

        button_image_1 = PhotoImage( file=("button_chat.png"))
        self.button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=self.buttoncs, relief="flat")
        self.button_1.place(x=699.0, y=669.0, width=195.28343200683594, height=53.4000244140625)

        button_image_2 = PhotoImage(file=("button_Shop.png"))
        self.button_2 = Button(image=button_image_2,borderwidth=0,highlightthickness=0,command=lambda: print("button_2 clicked"),relief="flat")
        self.button_2.place(x=1021.0,y=668.0,width=195.40325927734375,height=53.4000244140625)

        button_image_3 = PhotoImage(file=("button_back.png"))
        self.button_3 = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=self.buttonback, relief="flat")
        self.button_3.place(x=0.0, y=0.0, width=35.0, height=30.0)
        self.window.resizable(True, False)
        self.window.mainloop()

    def buttonback(self):
        self.window.destroy()
        HappyShopping()

    # def buttoncs(self):
    #     self.window.destroy()
    #     CustomerService()

    

#======================================================================================================================================#




#======================================================================================================================================#
#======================================================================================================================================#
#======================================================================================================================================#

# class CustomerService:
#     def __init__(self):
#         self.window = Tk()
#         self.window.title("Customer Service")
#         self.window.geometry("1280x832")
#         self.window.configure(bg="#FFFFFF")



#         self.canvas = Canvas(self.window, bg = "#FFFFFF", height = 832, width = 1280, bd = 0, highlightthickness = 0, relief = "ridge")
#         self.canvas.place(x = 0, y = 0)
#         self.canvas.create_rectangle(0.0, 0.0, 640.0, 832.0, fill="#000000", outline="")

#         image_image_1 = PhotoImage(file=("CUSTOMER SERVICE/image_1.png"))
#         self.image_1 = self.canvas.create_image(320.0,416.0,image=image_image_1)

#         entry_image_1 = PhotoImage(
#             file=("CUSTOMER SERVICE/entry_1.png"))
#         self.entry_bg_1 = self.canvas.create_image(
#             917.5,
#             695.7000122070312,
#             image=entry_image_1
#         )
        
#         self.entry_1 = Entry(
#             bd=0,
#             bg="#D9D9D9",
#             fg="#000716",
#             highlightthickness=0
#         )
#         self.entry_1.place(
#             x=703.0,
#             y=669.0,
#             width=429.0,
#             height=51.4000244140625
#         )

#         button_image_1 = PhotoImage(
#             file=("CUSTOMER SERVICE/button_1.png"))
#         self.button_1 = Button(
#             image=button_image_1,
#             borderwidth=0,
#             highlightthickness=0,
#             command=lambda: print("button_1 clicked"),
#             relief="flat"
#         )
#         self.button_1.place(
#             x=0.0,
#             y=0.0,
#             width=35.0,
#             height=30.0
#         )

#         image_image_2 = PhotoImage(
#             file=("CUSTOMER SERVICE/image_2.png"))
#         self.image_2 = self.canvas.create_image(
#             957.0,
#             360.0,
#             image=image_image_2
#         )

#         button_image_2 = PhotoImage(
#             file=("CUSTOMER SERVICE/button_2.png"))
#         self.button_2 = Button(
#             image=button_image_2,
#             borderwidth=0,
#             highlightthickness=0,
#             command=self.send_message,
#             relief="flat"
#         )
#         self.button_2.place(
#             x=1150.0,
#             y=669.0,
#             width=66.0,
#             height=53.0
#         )
#         self.window.resizable(False, False)
#         self.window.mainloop()

        


####

# class CustomerService:
#     def __init__(self, token):
#         self.token = token
#         self.updater = Updater(token=token, use_context=True)
#         self.dispatcher = self.updater.dispatcher

#         self.init_ui()
#         self.init_handlers()

#     def init_ui(self):
#         self.root = tk.Tk()
#         self.root.title("Telegram Bot")

#         self.message_text = tk.Entry(self.root, width=80)
#         self.message_text.pack()

#         self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
#         self.send_button.pack()

#         self.response_text = tk.Text(self.root, width=40, height=10, state="disabled")
#         self.response_text.pack()

#         self.delete_button = tk.Button(self.root, text="Delete", command=self.delete_message)
#         self.delete_button.pack()

#     def init_handlers(self):
#         self.start_handler = CommandHandler('start', self.start)
#         self.dispatcher.add_handler(self.start_handler)

#         self.message_handler = MessageHandler(Filters.text, self.process_message)
#         self.dispatcher.add_handler(self.message_handler)

#     def start(self, update, context):
#         context.bot.send_message(chat_id=update.effective_chat.id, text="Halo! Selamat datang di bot Telegram dengan GUI.")

#     def process_message(self, update, context):
#         message = update.message.text
#         response = "BOT : " + message
#         context.bot.send_message(chat_id=update.effective_chat.id, text=response)
#         self.display_response(response)

#     def display_response(self, response):
#         self.response_text.configure(state="normal")
#         self.response_text.insert("end", response + "\n")
#         self.response_text.configure(state="disabled")

#     def send_message(self):
#         message = self.message_text.get()
#         response = "YOU : " + message
#         self.response_text.configure(state="normal")
#         self.response_text.insert("end", response + "\n")
#         self.response_text.configure(state="disabled")
#         self.updater.bot.send_message(chat_id=ai, text=message)
#         self.message_text.delete(0, "end")

#     def delete_message(self):
#         self.response_text.configure(state="normal")
#         self.response_text.delete("1.0", "end")
#         self.response_text.configure(state="disabled")

#     def run(self):
#         self.updater.start_polling(poll_interval=0.1, timeout=10)
#         self.root.mainloop()


# if __name__ == '__main__':
#     load_dotenv()

#     token = os.getenv('BOT_TOKEN')

#     bot_gui = CustomerService(token)
#     bot_gui.run()


# import tkinter as tk
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# from dotenv import load_dotenv
# import os

# load_dotenv()

# token = os.getenv('BOT_TOKEN')
# ai = os.getenv("ai")

# class CustomerService:
#     def __init__(self):
#         self.window = tk.Tk()
#         self.window.title("Customer Service")
#         self.window.geometry("1280x832")
#         self.window.configure(bg="#FFFFFF")

#         self.canvas = tk.Canvas(self.window, bg="#FFFFFF", height=832, width=1280, bd=0, highlightthickness=0, relief="ridge")
#         self.canvas.place(x=0, y=0)
#         self.canvas.create_rectangle(0.0, 0.0, 640.0, 832.0, fill="#000000", outline="")

#         image_image_1 = tk.PhotoImage(file="CUSTOMER SERVICE/image_1.png")
#         self.image_1 = self.canvas.create_image(320.0, 416.0, image=image_image_1)

#         entry_image_1 = tk.PhotoImage(file="CUSTOMER SERVICE/entry_1.png")
#         self.entry_bg_1 = self.canvas.create_image(917.5, 695.7000122070312, image=entry_image_1)

#         self.entry_1 = tk.Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
#         self.entry_1.place(x=703.0, y=669.0, width=429.0, height=51.4000244140625)

#         button_image_1 = tk.PhotoImage(file="CUSTOMER SERVICE/button_1.png")
#         self.button_1 = tk.Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=self.button_back, relief="flat")
#         self.button_1.place(x=0.0, y=0.0, width=35.0, height=30.0)

#         image_image_2 = tk.PhotoImage(file="CUSTOMER SERVICE/image_2.png")
#         self.image_2 = self.canvas.create_image(957.0, 360.0, image=image_image_2)

#         button_image_2 = tk.PhotoImage(file="CUSTOMER SERVICE/button_2.png")
#         self.button_2 = tk.Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=self.send_message, relief="flat")
#         self.button_2.place(x=1150.0, y=669.0, width=66.0, height=53.0)

#         self.window.resizable(False, False)

#         self.init_bot()

#         self.window.mainloop()

#     def init_bot(self):
#         self.updater = Updater(token=token, use_context=True)
#         self.dispatcher = self.updater.dispatcher

#         self.init_handlers()

#         self.updater.start_polling(poll_interval=0.1, timeout=10)

#     def init_handlers(self):
#         self.start_handler = CommandHandler('start', self.start)
#         self.dispatcher.add_handler(self.start_handler)

#         self.message_handler = MessageHandler(Filters.text, self.process_message)
#         self.dispatcher.add_handler(self.message_handler)

#     def start(self, update, context):
#         context.bot.send_message(chat_id=update.effective_chat.id, text="Halo! Selamat datang di bot Telegram dengan GUI.")

#     def process_message(self, update, context):
#         message = update.message.text
#         response = "BOT : " + message
#         context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    # def button_back(self):
    #     self.window.destroy()
    #     Newarrival


    # def send_message(self):
    #     message = self.entry_1.get()
    #     response = "YOU : " + message
    #     self.updater.bot.send_message(chat_id=ai, text=message)
    #     self.entry_1.delete(0, "end")

# # Inisialisasi objek CustomerService
# customer_service = CustomerService()



#======================================================================================================================================#
class TelegramBot:
    def __init__(self, token,bot_gui=None):
        self.token = token
        self.bot_gui=bot_gui
        self.updater = Updater(token, use_context=True)
        self.init_handlers()
        self.updater.start_polling()
        

    def init_handlers(self):
        dispatcher = self.updater.dispatcher
        start_handler = CommandHandler('start', self.start)
        message_handler = MessageHandler(Filters.text & (~Filters.command), self.process_message)
        dispatcher.add_handler(start_handler)
        dispatcher.add_handler(message_handler)

    def start(self, update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Halo! Selamat datang di bot Telegram dengan GUI.")

    def process_message(self, update: Update, context: CallbackContext):
        message = update.message.text
        response = "BOT: " + message
        self.bot_gui.display_response(response)

        # Kirim pesan ke bot tujuan melalui webhook
        requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage", json={
            "chat_id": bot_to_forward,
            "text": "bot = " + message})

    def send_message(self, message):
        response = "YOU: " + message
        self.bot_gui.display_response(response)

        # Kirim pesan ke bot tujuan melalui webhook
        requests.post(f"https://api.telegram.org/bot{self.token}/sendMessage", json={
            "chat_id": bot_to_forward,
            "text": message
        })


class TelegramBotGUI:
    def __init__(self, bot):
        self.bot = bot

    def init_ui(self):
        self.root = tk.Tk()
        self.root.title("Telegram Bot")
        self.root.geometry("1280x832")
        self.root.configure(bg="#FFFFFF")

        self.canvas = tk.Canvas(self.root, bg="#FFFFFF", height=832, width=1280, bd=0, highlightthickness=0,
                                relief="ridge")
        self.canvas.place(x=0, y=0)

        image_image_1 = tk.PhotoImage(file=("image_1.png"))
        self.image_1 = self.canvas.create_image(320.0, 416.0, image=image_image_1)

        self.response_text = tk.Text(self.root, height=10, width=50, bg="cornsilk", fg="black")
        self.response_text.place(x=700.0, y=60.0, width=520.0, height=557.0)
        self.response_text.configure(state="disabled")

        entry_image_1 = tk.PhotoImage(file="chat.png")
        self.entry_bg_1 = self.canvas.create_image(917.5, 695.6999969482422, image=entry_image_1)
        self.message_text = tk.Entry(self.root, bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.message_text.place(x=700.0, y=667.0, width=429.0, height=51.4000244140625)

        button_image_2 = tk.PhotoImage(file="send.png")
        self.send_button = tk.Button(self.root, image=button_image_2, borderwidth=0, highlightthickness=0,
                                     command=self.send_message, relief="flat", text="Send")
        self.send_button.place(x=1150.0, y=667.0, width=66.0, height=53.0)
        button_image_5 = PhotoImage(file="back.png")
        data = Button(self.root,image=button_image_5,width=10,fg='yellow',bg='brown',text="< Back",font=('Microsoft YaHei UI Light', 12),command=self.back)
        data.place(x=0.0, y=0.0, width=35.0, height=30.0) 

        self.root.mainloop()

    def send_message(self):
        message = self.message_text.get().strip()
        self.bot.send_message(message)
        self.message_text.delete(0, "end")

    def display_response(self, response):
        self.response_text.configure(state="normal")
        self.response_text.insert(tk.END, response + "\n")
        self.response_text.configure(state="disabled")
        self.response_text.see(tk.END)
    
    def back(self):
        self.root.destroy()
        Newarrival()

    def run(self):
        self.init_ui()

#     def button_back(self):
#         self.root.destroy()
#         HappyShopping()

# # class HappyShopping:
# #     def __init__(self):
# #         self.window = tk.Tk()
# #         self.window.title("Happy shopping")
# #         self.window.geometry("1280x832")
# #         self.window.configure(bg="#FFFFFF")

# #         self.window.resizable(False, False)
# #         self.window.mainloop()

# if __name__ == '__main__':
#     logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                         level=logging.INFO)

#     bot = TelegramBot(token)
#     bot_gui = TelegramBotGUI(bot)
#     bot_gui.run()
#======================================================================================================================================#

# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk


# class Product:
#     def __init__(self, name, image_path, price, additional_info):
#         self.name = name
#         self.image_path = image_path
#         self.price = price
#         self.additional_info = additional_info


# class KumpulanProduk(tk.Tk):
#     def __init__(self, products):
#         super().__init__()
#         self.title("Binary Search Product")
#         self.products = products

#         self.search_var = tk.StringVar()
#         self.search_var.trace("w", self.filter_products)

#         self.entry_search = ttk.Entry(self, textvariable=self.search_var)
#         self.entry_search.pack(fill=tk.NONE, padx=10, pady=10)

#         self.canvas = tk.Canvas(self)
#         self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

#         self.product_frame = ttk.Frame(self.canvas)
#         self.product_frame.pack()

#         self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
#         self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

#         self.canvas.configure(yscrollcommand=self.scrollbar.set)
#         self.canvas.create_window((0, 0), window=self.product_frame, anchor=tk.NW)

#         self.display_products()

#         self.product_frame.bind("<Configure>", self.on_frame_configure)
#         self.canvas.bind("<Configure>", self.on_canvas_configure)

#         self.cart = []
#         self.geometry("1280x832")

#     def filter_products(self, *args):
#         query = self.search_var.get().lower()
#         filtered_products = [product for product in self.products if query in product.name.lower()]
#         self.display_products(filtered_products)

#     def add_to_cart(self, product):
#         print(f"{product.name} GO TO DESCRIPTION!")

#     def update_cart(self):
#         self.cart_label.configure(text=f"({len(self.cart)} items)")

#     def display_products(self, products=None):
#         if products is None:
#             products = self.products

#         for widget in self.product_frame.winfo_children():
#             widget.destroy()

#         num_cols = 6
#         row = 0
#         col = 0

#         for product in products:
#             product_frame = ttk.Frame(self.product_frame)
#             product_frame.grid(row=row, column=col, padx=15, pady=15)

#             # Resize the image
#             image = Image.open(product.image_path)
#             image = image.resize((100, 100), Image.ANTIALIAS)
#             photo = ImageTk.PhotoImage(image)

#             image_label = ttk.Label(product_frame, image=photo)
#             image_label.image = photo  # save a reference to the image
#             image_label.pack()

#             name_label = ttk.Label(product_frame, text=product.name)
#             name_label.pack()

#             price_label = ttk.Label(product_frame, text=f"Price: {product.price:,}")
#             price_label.pack()

#             button = ttk.Button(product_frame, text="REVIEW", command=lambda p=product: self.review_product(p))
#             button.pack()

#             col += 1
#             if col == num_cols:
#                 col = 0
#                 row += 1

#     def on_frame_configure(self, event):
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))

#     def on_canvas_configure(self, event):
#         self.canvas.itemconfigure(self.product_frame, width=event.width)

#     def review_product(self, product):
#         review_page = ReviewPage(self, product)
#         review_page.pack()
#         self.product_frame.pack_forget()

#     def back_to_main_page(self):
#         self.product_frame.pack()
#         self.display_products()

#     def destroy_review_page(self, review_page):
#         review_page.destroy()
#         self.back_to_main_page()


# class ReviewPage(ttk.Frame):
#     def __init__(self, master, product):
#         super().__init__(master)
#         self.product = product

#         name_label = ttk.Label(self, text=product.name)
#         name_label.pack(pady=10)

#         # Add additional info
#         additional_info_label = ttk.Label(self, text="Additional Information:")
#         additional_info_label.pack()

#         for info in product.additional_info:
#             info_label = ttk.Label(self, text=info)
#             info_label.pack()

#         back_button = ttk.Button(self, text="Back", command=self.back_to_main_page)
#         back_button.pack(pady=10)

#     def back_to_main_page(self):
#         self.master.destroy_review_page(self)

class Product:
    def __init__(self, name, image_path, price, description):
        self.name = name
        self.image_path = image_path
        self.price = price
        self.description = description
        


class KumpulanProduk(tk.Tk):
    def __init__(self, products):
        super().__init__()
        self.title("Binary Search Product")
        self.geometry("1280x832")
        self.products = sorted(products, key=lambda x: x.name.lower())  # Mengurutkan produk berdasarkan nama

        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.filter_products)

        self.entry_search = ttk.Entry(self, textvariable=self.search_var)
        self.entry_search.pack(fill=tk.NONE, padx=10, pady=10)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.product_frame = ttk.Frame(self.canvas)
        self.product_frame.pack()
        
        button1 = ttk.Button(self, text="<< BACK",command=self.back)
        button1.place(x=0.0, y=0.0, width=100.0, height=30.0) 

        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.create_window((0, 0), window=self.product_frame, anchor=tk.NW)
        
        

        self.display_products()

        self.product_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        self.cart = []
        
    def back(self):
        self.destroy()
        Newarrival()

    def filter_products(self, *args):
        query = self.search_var.get().lower()
        filtered_products = [product for product in self.products if query in product.name.lower()]
        self.display_products(filtered_products)
#khasfihihaefslhdsjlkbvsvbajbvsjBVJLbjk.vBSABjbsJ>AbSBrvbsARJegbareg
    def binary_search(self, products, target):
        start = 0
        end = len(products) - 1

        while start <= end:
            mid = (start + end) // 2
            if products[mid].name.lower().startswith(target):
                return products[mid:]
            elif products[mid].name.lower() < target:
                start = mid + 1
            else:
                end = mid - 1

        return []



    def add_to_cart(self, product):
        messagebox.showinfo("Product Description", "\n".join(product.description))

    def display_products(self, products=None):
        if products is None:
            products = self.products

        for widget in self.product_frame.winfo_children():
            widget.destroy()

        num_cols = 6
        row = 0
        col = 0

        for product in products:
            product_frame = ttk.Frame(self.product_frame)
            product_frame.grid(row=row, column=col, padx=15, pady=15)

            # Resize the image
            image = Image.open(product.image_path)
            image = image.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)

            image_label = ttk.Label(product_frame, image=photo)
            image_label.image = photo  # save a reference to the image
            image_label.pack()

            name_label = ttk.Label(product_frame, text=product.name)
            name_label.pack()

            price_label = ttk.Label(product_frame, text=f"Price: {product.price:,}")
            price_label.pack()

            button = ttk.Button(product_frame, text="REVIEW", command=lambda p=product: self.add_to_cart(p))
            button.pack()
            
            # button1 = ttk.Button(product_frame, text="REVIEW", command=lambda p=product: self.add_to_cart(p))
            # button1.place(x=0.0, y=0.0, width=35.0, height=30.0) 
            
            # button_image_18 = PhotoImage(file="back.png")
            # data = ttk.Button(product_frame,image=button_image_18,width=10,fg='yellow',bg='brown',text="< Back",font=('Microsoft YaHei UI Light', 12),command=self.back)
            # data.place(x=0.0, y=0.0, width=35.0, height=30.0) 

            col += 1
            if col == num_cols:
                col = 0
                row += 1

    # def back(self):
    #     self.destroy()
    #     Newarrival()
    
    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfigure(self.product_frame, width=event.width)




def run():
    products = [
        Product('Mi 37W Dual-Port Car Charger', 'Mi 37W Dual-Port Car Charger.png', 109000,
                [
                    "Nomor model = CCO6ZM",
                    "Output = USB-A",
                    "Parameter input = 12V-24V=4A",
                    "Parameter output = USB1: 5V-2A",
                    "USB2: 5V=3A 9V=3A 12V=2.25A 20V= 1.35A",
                    "Dimensi produk = 74.7 x 30.8 x 30.8mm"
                ]),

        Product('Mi 360 Camera (1080p)', 'Mi 360Camera (1080p).png', 449000,
                [
                    "Model",
                    "MJSXJ10CM",
                    "Apertur",
                    "F2.1",
                    "Resolusi",
                    "1920x1080",
                    "Memori yang dapat ditambah",
                    "Kartu Micro SD (hingga 32 GB)",
                    "Suhu pengoperasian",
                    "-10℃一40℃",
                    "Konektivitas nirkabel",
                    "Wi-Fi IEEE 802.11b/g/n, 2.4 GHz",
                    "Berat netto",
                    "254 g",
                    "Input daya",
                    "5V/2A",
                ]),

        Product('Mi Curved Gaming Monitior 34', 'Mi Curved Gaming Monitor 34_.png', 5599000,
                [
                    "Spesifikasi Layar",
                    "Resolusi: 3440 x 1440",
                    "Kelengkungan layar: 1500R",
                    "Waktu respons: 4 mdtk (Waktu respons skala abu-abu)",
                    "Warna: 16,7 juta (8-bit)",
                    "Kecerahan: 300 cd/m²",
                    "Layar: 21:9",
                    "Refresh rate: 144 Hz",
                    "Gamut warna: 121% SRGB",
                    "Rasio kontras: 3000:1 (TIPIKAL)",
                    "Mode jendela",
                    "Satu jendela",
                    "Layar terpisah kiri/kanan",
                    "Mode gambar dalam gambar",
                ]),

        Product('Mi Desktop Monitor 27”', 'Mi Desktop Monitor 27.png', 1699000,
                [
                    "No. model produkRMMNT27NF",
                    "Input daya12V, 2A",
                    "Daya terukur*Maks. 24 W",
                    "Ukuran layar27 inci",
                    "Ukuran layar (diagonal)685,98 mm",
                    "Dot pitch0,3114 x 0,3114 mm",
                    "Kecerahan300 cd/m² (UMUM)",
                    "Kontras1000:1 (UMUM)",
                    "Kontras dinamis1000000:1",
                    "Jumlah warna16,7 juta",
                    "Rasio aspek16:9",
                    "Waktu respons6 ms (GTG)",
                    "Resolusi maksimum1920x1080",
                    "Resolusi yang disarankan1920x1080",
                    "Refresh rate maksimum75 Hz",
                    "Refresh rate yang disarankan60 Hz",
                    "Dimensi613,2 (P) x 205,3 (L) x 476,0 (T) mm",
                ]),

        Product('Mi LCD Writing Tablet 13.5"', 'Mi LCD Writing Tablet 13.5&quot.png', 2699000,
                
                [
                    "Nama produk",
                    "Mi LCD Writing Tablet 13,5",
                    "Model produk",
                    "XMXHB02WC",
                    "Baterai",
                    "Sel kancing (CR2025)",
                    "Dimensi produk",
                    "318 mm x 225 mm x 7 mm 0,345 kg",
                    "Berat netto",
                    "0,345 kg (termasuk baterai tipe",
                    "sel kancing)",
                    "Bahan utama",
                    "Lapisan film lembut LCD yang",
                    "terbuat dari polimer padat ABS",
                ]),

        Product('Mi Robot Vacuum-Mop 2 Lite', 'Mi Robot Vacuum-Mop 2 Lite.png', 2799000,
                [
                    "ModelMJSTL",
                    "Dimensi Item353 x 81,3 mm",
                    "Daya Terukur35 W",
                    "Tegangan Terukur14,4 V⎓",
                    "Berat Bersih3,1 kg",
                    "Kapasitas Baterai2500 mAh (kapasitas terukur)",
                    "2600 mAh (kapasitas nominal)",
                    "ModelCDZMJSTL",
                    "Input Tetapan100-240 V ~ 50/60 Hz 0,6 A",
                    "Output Terukur20 V ⎓ 1,2 A",
                    "Dimensi Item150 x 135 x 97,4 mm",
                ]),

        Product('Mi Router 4C', 'Mi Router 4C.png', 199000,
                [
                    "ProsesorMT7628DA",
                    "Memori internal64MB DDR2",
                    "2.4GhzLNA dan PA terintegrasi",
                    "5GHzTidak didukung",
                    "Disipasi panasPanas alami",
                    "Kelembapan pengoperasian:10-90% RH (tanpa kondensasi)",
                    "Kelembapan penyimpanan:5-90% RH (tanpa kondensasi)",
                    "Standar protokolIEEE 802.11b/g/nIEEE 802.3/3u",
                    "ROM16MB NorFlash",
                    "Wi-Fi 2.4GHz2.4GHz Wi-Fi2x2",
                    "(mendukung protokol IEEE 802.11N, kecepatan maksimum 300 Mbps)",
                    "Wi-Fi 5GHzTidak didukung",
                    "Antena4x antena band tunggal eksternal",
                ]),
        Product('Mi Smart Air Fryer (3.5L)', 'Mi Smart Air Fryer (3.5L).png', 1199000,
                [
                    "ModelMAF02",
                    "Tegangan Terukur220-240 V",
                    "Frekuensi Terukur50-60 Hz",
                    "Berat Bersih3,9 kg",
                    "Berat Kotor5,2 kg",
                    "Daya Terukur1500 W",
                    "Volume Terukur3,5 L",
                    "Bahan KeranjangLogam Alclad",
                ]),
        Product('Mi TV 4 43', 'Mi TV 4 43.png', 3599000,
                [
                    "FHD tampilan",
                    "2x Stereo Speaker 8W",
                    "PatchWall 3.0 dengan Konten lebih dari 700.000 Jam",
                    "Android TV Google Assistant",
                    "Penghemat Data",
                    "FHD",
                    "Resolusi:1920 x 1080",
                    "Sudut pandang: 178°",
                    "Refresh rate: 60Hz",
                    "Lampu latar:: DLED",
                    "Powerful speaker",
                    "Daya audio: 2 x 8W 8ohm",
                    "CPU: Amlogic Cortex A53 quad-core",
                    "RAM: 1GB DDR",
                    "GPU: Mali-450 MP3",
                    "Penyimpanan: 8GB eMMC",
                ]),
        Product('Mi TV 4 55', 'Mi TV 4 55.png', 5999000,
                [
                    "Layar 4K HDR",
                    "2x Stereo Speaker 10W",
                    "PatchWall 3.0 dengan Konten lebih dari 700.000 Jam",
                    "Android TV Google Assistant",
                    "Penghemat Data",
                    "Resolusi: 3840 x 2160",
                    "Sudut pandang: 178°",
                    "Refresh rate: 60Hz",
                    "Lampu latar: DLED",
                    "CPU: Amlogic Cortex A53 quad-core",
                    "RAM: 2GB DDR",
                    "GPU: Mali-450 MP3",
                    "Penyimpanan: 8GB eMMC",
                ]),

        Product('Mi TV Stick', 'Mi TV Stick.png', 599000,
                [
                    "Resolusi output",
                    "1080P (1920x1080@60fps)",
                    "RAM",
                    "1GB",
                    "CPU",
                    "Quad-core Cortex-A53",
                    "Memori Penyimpanan",
                    "8GB",
                    "GPU",
                    "ARM Mali-450",
                    "Sistem operasi",
                    "Android 9.0",
                    "Wi-Fi",
                    "802.11a/b/g/n/ac 2.4GHz/5GHz",
                    "Bluetooth",
                    "4.2",
                ]),
        Product('Mi Vacuum Cleaner Light', 'Mi Vacuum Cleaner Light.png', 1499000,
                [
                    "Nama produk21,6 V",
                    "Tegangan operasi Mi Vacuum Cleaner Light",
                    "Daya operasi 220 W",
                    "Kapasitas baterai lithium 2500 mAh",
                    "Waktu kerja (mode standar/mode MAX)45 mnt/",
                    "13 mnt (tanpa sikat ground listrik)",
                    "Tegangan pengisian daya26,0 V",
                    "Pengisian daya arus kecil0,5 A",
                    "Durasi pengisian daya Kira-kira 5 jam",
                    "Berat Kira-kira 2,3kg",
                    "Kebisingan≤ 79 dB",
                    "Dimensi 240 x 148 x 1132 mm",
                ]),
        Product('Mi Vacuum Cleaner Mini.jpg', 'Mi Vacuum Cleaner Mini.jpg.png', 649000,
                [
                    "Nama produk Mi Vacuum Cleaner Mini",
                    "Berat bersih produk Sekitar 0,5 kg (unit utama)",
                    "Daya Terukur 40W",
                    "Dimensi Produk 267 x 55 x 55 mm",
                    "Tegangan pengenal 10,8V",
                ]),

        Product('Mi Watch Charging Dock', 'Mi Watch Charging Dock.png', 69000,
                [
                    "Nama produk",
                    "Mi Watch Charging Dock",
                    "Material produk",
                    "PC + ABS",
                    "Ukuran produk",
                    "40,3x40,3x9,8 mm",
                ]),

        Product('Mi WiFi Range Extender AC1200', 'Mi WiFi Range Extender AC1200.png', 249000,
                [
                    "ModelRA75",
                    "StandarIEEE 802.11ac/n/a 5GHz, IEEE 802.11n/b/g 2,4GHz",
                    "Kecepatan WiFi5 GHz: 867Mbps (802.11ac, 2*2 @80MHz)" 
                    "2,4 GHz: 300Mbps (802.11n, 2*2 @40MHz)",
                    "ModeMode Range Extender, Mode Access Point",
                    "Keamanan NirkabelWPA-PSK / WPA2-PSK",
                    "Daya Transmisi<20 dBm (2,4 GHz), <23 dBm (5 GHz)",
                    "RAM64MB",
                    "PortPort Ethernet 1*10/100Mbps",
                    "TombolTombol WPS, Tombol Reset",
                    "Input100~240V, 50/60Hz, 0,3A",
                    "Dimensi84x100x82mm*",

                ]),
        Product('Mi Wireless Switch', 'Mi Wireless Switch.png', 99000,
                [
                    "No. model produk",
                    "WXKGO1LM",
                    "Dimensi produk",
                    "50 x 50 x 13 mm",
                    "Konektivitas nirkabel",
                    "Zigbee",
                    "Spesifikasi baterai",
                    "CR2032",
                    "Suhu pengoperasian",
                    "-10°C hingga +50°C",
                    "Kelembapan kerja",
                    "0-95% RH, non-condensasi",
                ]),
        Product('POCO F4 GT', 'POCO F4 GT.png', 7999000,
                [
                    "RAM LPDDR5 + Penyimpanan UFS3.1",
                    "Tinggi: 162,5 mm",
                    "Lebar: 76,7 mm",
                    "Ketebalan: 8,5 mm",
                    "Berat: 210 g",
                    "Snapdragon® 8 Gen 1",
                    "Proses manufaktur 4nm",
                    "CPU: CPU Octa-core Qualcomm® Kryo™, hingga 3,0 GHz",
                    "GPU: GPU Qualcomm® Adreno™",
                    "AI: Qualcomm® AI Engine Generasi ke-7",
                    "Modem Snapdragon® X65 5G",
                    "LiquidCool Technology 3.0",
                    "DotDisplay AMOLED datar 6,67",
                    "Resolusi: FHD+ 2400 x 1080",
                    "Rasio aspek: 20:9",
                    "Refresh rate: Hingga 120 Hz",
                ]),

        Product('POCO F4', 'POCO F4.png', 5199000,
                [
                    "LPDDR5+ UFS 3.1",
                    "Tinggi: 163,2 mm",
                    "Lebar: 75,95 mm",
                    "Ketebalan: 7,7 mm",
                    "Berat: 195 g",
                    "Snapdragon® 870",
                    "CPU: CPUI Octa-core® Qualcomm Kryo™ 585",
                    "Proses manufaktur 7nm 1x Prime core ",
                    "berbasis A77, 3,2 GHz 3x Gold core",
                    "berbasis A77, 2,42 GHz 4x Silver core" ,
                    "berbasis A55, 1,8 GHz",
                    "GPU: GPU Qualcomm® Adreno™ 650",
                    "Modem X55 untuk konektivitas 5G" ,
                    "AMOLED 120 Hz 6,67”",
                    "DotDisplay ultra-mungil 2.76 mm",
                    "20:9, 2400x1080 FHD+",
                    "DCI-P3 100% (standar)",

                ]),
        Product('poco M4 pro', 'poco M4 pro.png', 3399000,
                [
                    "RAM LPDDR4X + Penyimpanan UFS2.2",
                    "Tinggi: 159,87 mm",
                    "Lebar: 73,87 mm",
                    "Ketebalan: 8,09 mm",
                    "Berat: 179,5 g",
                    "MediaTek Helio G96",
                    "CPU: CPU octa-core, hingga 2,05 GHz",
                    "GPU: Mali-G57 MC2",
                    "Baterai 5000mAh (typ)",
                    "Pengisian cepat 33W Pro",
                    "DotDisplay AMOLED FHD+ 6,43FHD+" ,
                    "2400x1080Rasio kontras: 4.500.000:1",
                    "Tingkat kecerahan: 2048",
                    "Refresh rate: 90 Hz",
                    "Touch sampling rate: 180 Hz",
                    "Sunlight displaySGS Eye Care DisplaySGS" ,
                    "Seamless Display",
                ]),
        Product('POCO M5', 'POCO M5.png', 2299000,
                [
                    "Tinggi: 163,99 mm",
                    "Lebar: 76,09 mm",
                    "Ketebalan: 8,9 mm",
                    "Berat: 201 g",
                    "MediaTek Helio G99",
                    "Proses manufaktur 6nm",
                    "CPU: CPU octa-core, hingga 2,2 GHz",
                    "GPU: Arm Mali-G57 MC2",
                    "Layar 6,58 FHD+ DotDrop" ,
                    "Resolusi: FHD+ 2408 x 1080",
                    "Rasio aspek: 20:9",
                    "Refresh rate: 30 / 60 / 90 Hz",
                    "Touch sampling rate: 240 Hz",
                    "Kecerahan: 500 nit (HBM)",
                    "Rasio kontras: 1500:1",
                    "Corning® Gorilla® Glass",
                ]),
        Product('POCO M5s', 'POCO M5s.png', 2599000,
                [
                    "MediaTek Helio G95CPU:",
                    "CPU octa-core, hingga 2,05 GHz",
                    "GPU: Arm Mali-G76 MC4",
                    "Tinggi: 160,46 mm",
                    "Lebar: 74,5 mm",
                    "Ketebalan: 8,29 mm",
                    "Berat: 178,8 g",
                    "DotDisplay AMOLED 6,43”",
                    "Resolusi: FHD+, 2400 x 1080",
                    "PPI: 409",
                    "Kecerahan:",
                    "Mode kecerahan tinggi: 700 nit",
                    "Kecerahan puncak 1100 nit",
                    "Rasio kontras: 4500000:1",
                    "Peredupan DCSunlight display",
                    "Mode Baca",
                    "Corning® Gorilla® Glass",
                ]),
        Product('POCO X5 5G', 'POCO X5 5G.png', 3499000,
                [
                    "LPDDR4X + UFS2.2",
                    "Penyimpanan dapat diperbesar hingga 1TB",
                    "Tinggi: 165,88 mm",
                    "Lebar: 76,21 mm",
                    "Ketebalan: 7,98 mm",
                    "Berat: 189 g",
                    "Snapdragon® 695 5G Mobile Platform",
                    "CPU: CPU octa-core, hingga 2,2 GHz",
                    "GPU: Qualcomm® Adreno™ 619",
                    "5.000 mAh (standar)",
                    "Pengisian daya cepat 33 W",
                    "6.67' FHD+ AMOLED DotDisplay",
                    "Refresh rate: Hingga 120 Hz",
                    "Kecerahan: 700 nit (HBM), 1.200 nit (maksimal)Rasio kontras: 4.500.000:1",
                    "Resolusi: 2400 x 1080Gamut warna luas DCI-P3",
                ]),
        Product('Redmi 10 2022', 'Redmi 10 2022.png', 2299000,
                [
                    "LPDDR4X +eMMC",
                    "Tinggi: 161,95 mm",
                    "Lebar: 75,53 mm",
                    "Ketebalan: 8,92 mm",
                    "Berat: 181 g",
                    "MediaTek Helio G882 x Arm Cortex-A75 @ 2",
                    "GHz6 x Arm Cortex-A55 @ 1,8 GHzProses",
                    "manufaktur 12 nmGPU Arm Mali-G52",
                    "DotDisplay FHD+ 6,5",
                    "Refresh rate: 90 Hz",
                    "AdaptiveSync: 45/60/90 Hz",
                    "2400 x 1080, 405 ppi",
                    "Sunlight display",
                    "Mode baca 3.0Corning® Gorilla® Glass 3",
                    "Baterai 5000 mAh (standar)",
                    "Pengisian daya cepat 18 W",
                    "Reverse charging 9 W",
                ]),
        Product('Redmi Buds 3 Pro', 'Redmi Buds 3 Pro.png', 699000,
                [
                    "No. model produkTWSEJ01ZM",
                    "Waktu pengisian daya earbudSekitar 1 jam",
                    "Konektivitas nirkabelBluetooth 5.2",
                    "Waktu pengisian dengan dudukan pengisian daya",
                    "Sekitar 2,5 jam(pengisian daya dengan kabel)",
                    "Berat bersih satu earbudSekitar 4,9 g",
                    "Dimensi earbud25,4*20,3*21,3 mm",
                    "Berat total termasuk dudukan pengisian dayaSekitar 55 g",
                    "Dimensi dudukan pengisian daya65*48*26 mm",
                    "Impedansi speaker32 Ω",
                ]),

        Product('Redmi buds 4 Pro', 'Redmi buds 4 Pro.png', 949000,
                [
                    "No. model produkM2132E1",
                    "Parameter input earbudMAKS. 5,25 V ⎓ 160 mA (satu earbud)",
                    "Parameter input dudukan pengisian dayaMAKS. 5 V = 0,5 A",
                    "Port pengisian dayaUSB-C",
                    "Konektivitas nirkabelBluetooth® 5.3",
                    "Profil BluetoothBluetooth®Low Energy/HFP/A2DP/AVRCP",
                    "Jarak operasional10 m (ruang terbuka tanpa penghalang)",
                    "Impedansi speaker24 Ω",
                ]),
        Product('Redmi buds 4', 'Redmi buds 4.png', 549000,
                [
                    "Nomor model produk:M2137E1",
                    "Parameter input earbud:5V ⎓ 100mA",
                    "Parameter input kasing pengisi daya: 5V ⎓ 450mA",
                    "Koneksi nirkabel: Bluetooth 5.2 HSP, HFP",
                    "Protokol Bluetooth: HSP、HFP、A2DP、AVRCP",
                    "Jarak operasi: 10m (ruang terbuka bebas hambatan)",
                    "Berat bersih earbud tunggal: Kira-kira. 4,5g",
                    "Berat total termasuk wadah pengisi daya: Kira-kira 55g",
                    "Port pengisian daya: Tipe-C",
                    "Impedansi speaker: 1602",
                ]),
        Product('Redmi Note 11 Pro 5G', 'Redmi Note 11 Pro 5G.png', 4099000,
                [
                    "Snapdragon® 695",
                    "CPU: CPU octa-core, hingga 2,2 GHz",
                    "GPU: Qualcomm® Adreno™ 619",
                    "LPDDR4X + UFS2.2",
                    "Tinggi: 164,19 mm",
                    "Lebar: 76,1 mm",
                    "Ketebalan: 8,12 mm",
                    "Berat: 202 g",
                    "DotDisplay AMOLED FHD+ 6,67",
                    "Refresh rate: Hingga 120 Hz",
                    "Kecerahan: HBM 700 nit (standar)",
                    "1200 nit kecerahan puncak (standar)",
                    "Rasio kontras: 4.500.0000:1",
                    "Resolusi: 2400 x 1080",
                    "Rentang warna luas DCI-P3",
                    "395 ppi",
                    "Sunlight display",
                ]),

        Product('Redmi Note 11 Pro', 'Redmi Note 11 Pro.png', 3699000,
                [
                    "MediaTek Helio G96",
                    "CPU: CPU octa-core, hingga 2,05GHz",
                    "GPU: ARM Mali-G57 MC2",
                    "6GB+128GB / 8GB+128GB",
                    "LPDDR4X + UFS2.2",
                    "Tinggi: 164,19 mm",
                    "Lebar: 76,1 mm",
                    "Ketebalan: 8,12 mm",
                    "Berat: 202 g",
                    "Layar 120Hz Super AMOLED",
                    "Refresh rate: Hingga 120Hz",
                    "Kecerahan: HBM 700 nit (typ),", 
                    "1200 nit kecerahan puncak (typ)",
                    "Rasio kontras: 4.500.0000:1",
                    "Resolusi: 2400 x 1080",
                    "Rentang warna luas DCI-P3",
                    "395 ppi",

                ]),
        Product('Redmi Note 11', 'Redmi Note 11.png', 2699000,
                [
                    "Snapdragon® 680",
                    "Proses manufaktur 6nm",
                    "CPU: CPU octa-core, hingga 2,4 GHz",
                    "GPU: GPU Qualcomm® Adreno™ 610",
                    "LPDDR4X + UFS2.2",
                    "Tinggi: 159,87 mm",
                    "Lebar: 73,87 mm",
                    "Ketebalan: 8,09 mm",
                    "Berat: 179 g",
                    "DotDisplay AMOLED FHD+ 6,43",
                    "Refresh rate: Hingga 90 Hz",
                    "Touch sampling rate: Hingga 180Hz",
                    "Kecerahan: HBM 700 nit (standar) ",
                    "1000 nit kecerahan puncak (standar)",
                    "Rasio kontras: 4.500.0000:1",
                    "Resolusi: 2400 x 1080",
                    "Rentang warna luas DCI-P3409 ppi",

                ]),
        Product('Redmi Note 12 Pro 5G', 'Redmi Note 12 Pro 5G.png', 4599000,
                [
                    "MediaTek Dimensity 1080",
                    "Proses manufaktur 6 nm",
                    "CPU: Octa-core CPU, hingga 2.6GHz", 
                    "GPU: Mali-G68",
                    "8GB+5GB* | 256GBLPDDR4X + UFS 2.2",
                    "Tinggi: 162.9mm",
                    "Lebar: 76mm",
                    "Ketebalan: 7.9mm",
                    "Berat: 187g",
                    "Layar 6.67 FHD+ P-OLED",
                    "Refresh rate: Hingga 120Hz",
                    "Kecerahan: ",
                    "kecerahan puncak 900 nits", 
                    "(typ)Rasio kontras: 5,000,000:1",
                    "Resolusi: 2400 x 1080Gamut ",
                    "warna lebar DCI-P3",
                    "Corning® Gorilla® Glass 5 protection",
                    "Mendukung Dolby Vision®",
                ]),
        Product('Redmi Note 12', 'Redmi Note 12.png', 2999000,
                [
                    "Snapdragon® 685",
                    "CPU: CPU octa-core, hingga 2,8 GHz",
                    "GPU: Adreno 610Proses manufaktur 6 nm",
                    "4 + 128/6 + 128/8 + 128 GBLPDDR4X + UFS 2.2",
                    "5.000 mAh",
                    "DotDisplay AMOLED 6,67",
                    "Bahan: E2 Pro",
                    "Refresh rate: 120 Hz",
                    "Touch sampling rate: Hingga 240 HzKecerahan: 450 nit (umum)",
                    "HBM 700 nit (umum)",
                    "kecerahan puncak 1.200 nit",
                    "Rasio kontras: 4.500.000:18 bit",
                    "Gamut warna DCI-P3 yang kaya",
                    "Resolusi: 2.400 x 1.080PPI 395Sunlight displayMode baca",
                ]),
        Product('Redmi Pad', 'Redmi Pad.png', 3499000,
                [
                    "Nama produk",
                    "Mi LCD Writing Tablet 13,5",
                    "Model produk",
                    "XMXHB02WC",
                    "Baterai",
                    "Sel kancing (CR2025)",
                    "Dimensi produk",
                    "318 mm x 225 mm x 7 mm 0,345 kg", 
                    "Berat netto",
                    "0,345 kg (termasuk baterai tipe",
                    "sel kancing)",
                    "Bahan utama",
                    "Lapisan film lembut LCD yang",
                    "terbuat dari polimer padat ABS",

                ]),
        Product('Redmi Watch 3', 'Redmi Watch 3.png', 1199000,
                [
                    "42.58 x 36.56 x 9.99mm",
                    "*Height, width and thickness dimensions exclude the strap and protrusions",
                    "37g (only watch body)",
                    "Black strap: TPU strap",
                    "size: 135 200mm",
                    "Ivory strap: Silicone strap",
                    "size: 135 200mm",
                    "Heart rate sensor (with blood oxygen sensor), accelerometer, gyroscope, geomagnetic sensor",
                    "Typical use time: 12 days Heavy use time: 7 days",
                    "Capacity: 289mAh",
                ]),
        Product('RedmiBook 15', 'RedmiBook 15.png', 7499000,
                [
                    "Tipe Layar: 15.6” FHD",
                    "Resolusi: 1920 x 1080",
                    "PPI: 141",
                    "Kontrol Kecerahan: Peredupan DC",
                    "Kecerahan: 220 nit (umum)",
                    "Rasio kontras: 500:1",
                    "Gamut warna: NTSC 45% (umum)",
                    "Sudut tampilan: 90°(H)",
                    "Windows 10 Home",
                    "11th Generation Intel® Core™ i3-1115G4 ",
                    "(up to 4.1 GHz, 2 Cores, 4 Threads, 6 MB Cache)", 
                    "11th Generation Intel® Core™ i5-11300H" ,
                    "(up to 4.4 GHz, 4 Cores, 8 Threads, 8 MB Cache)",
                    "Intel® UHD Graphics",
                    "Bluetooth 5.0",
                    "Wi-Fi 5 2.4Ghz/5GHz",
                ]),
        Product('Xiaomi 6A Type-A to Type-C Cable', 'Xiaomi 6A Type-A to Type-C Cable.png', 79000,
                [
                    "Nama produk",
                    "Kabel Tipe-A ke Tipe-C 6 A Xiaomi",
                    "Bahan",
                    "TPE",
                    "Port",
                    "USB-A ke Tipe-C",
                    "Warna",
                    "Putih",
                    "Perangkat yang kompatibel",
                    "Smartphone dan perangkat digital lain dengan port USB Tipe-C",
                    "Arus",
                    "6 A",
                    "Panjang",
                    "1 m",
                ]),
        Product('xiaomi 10t Pro', 'xiaomi 10t.png', 6999000,
                [
                    "Tinggi: 165,1 mm",
                    "Lebar: 76,4 mm",
                    "Ketebalan: 9,33 mm",
                    "Bobot: 218g (Mi 10T Pro), 216g (Mi 10T)",
                    "Qualcomm® Snapdragon™ 865 dengan 5G",
                    "Proses manufaktur efisien daya 7nmQualcomm® Kryo™ 585",
                    "CPU Octa-core, hingga 2,84 GHzQualcomm® ",
                    "Adreno™ 650 GPUModem X55 untuk konektivitas 5G secepat kilat",
                    "Resolusi: 2400 x 1080 FHD+",
                    "Mendukung Adaptive Sync dalam 30Hz/48Hz/50Hz/60Hz/90Hz/120 Hz/144 Hz",
                    "Bentang warna: NTSC 96% (typ), DCI-P3 98% (typ)",
                    "Tampilan True Color: JNCD≈0,39, Delta E≈0,63Mendukung MEMC",
                    "Mode Baca 3.0",

                ]),
        Product('xiaomi 11 T pro', 'xiaomi 11 T pro.png', 6199000,
                [
                    "Tinggi: 164,1 mm",
                    "Lebar: 76,9 mm",
                    "Ketebalan: 8,8 mm",
                    "Berat: 204 g",
                    "Qualcomm® Snapdragon™ 888",
                    "Proses pembuatan 5nm yang hemat daya",
                    "Kryo 680 CPU, hingga 2,84GHz, dengan teknologi ARM Cortex-X1",
                    "GPU: GPU Qualcomm® Adreno™ 660",
                    "AI: Mesin AI Generasi ke-6",
                    "Modem 5G Snapdragon X60",
                    "AMOLED 6,67” DotDisplay",
                    "2400 x 1080",
                    "Rasio aspek: 20:9",
                    "Dolby Vision® Support",
                    "Refresh rate: 120Hz",
                    "Touch sampling rate: hingga 480Hz",

                ]),

        Product('xiaomi 11 T', 'xiaomi 11 T.png', 4999000,
                [
                    "RAM & Penyimpanan",
                    "8GB+256GB",
                    "Penyimpanan RAM LPDDR4X + UFS 3.1",
                    "Dimensi",
                    "Tinggi: 164,1 mm",
                    "Lebar: 76,9 mm",
                    "Ketebalan: 8,8 mm",
                    "Berat: 203 g",
                    "Prosesor",
                    "Dimensity 1200-Ultra",
                    "Layar",
                    "AMOLED 6,67” DotDisplay",
                    "Resolusi: 2400 x 1080 FHD+",
                    "Rasio aspek: 20:9",
                    "Refresh rate: 120Hz",
                    "Touch sampling rate: hingga 480Hz",
                ]),
        Product('Xiaomi 22.5W Power Bank 10000mAh', 'Xiaomi 22.5W Power Bank 10000mAh.png', 4599000,
                [
                    "Nomor model:PB100LZM",
                    "Jenis baterai: Baterai polimer Lithium-ion",
                    "Daya baterai:37Wh 3,7V 10.000 mAh",
                    "Kapasitas maksim:5500 mAh (5.1V/2.6A)",
                    "Port input:Micro-USB/USB-C",
                    "Port output:2 x USB-A.",
                    "Parameter input:5V/2.1A",
                    "Parameter output:Output satu port 5, 1V/2,4A",
                    "Port output ganda 5.1V/2.6A",
                    "Dimensi produk: 150,5 x 73,6 x 15,1 mm",
                ]),
        Product('Xiaomi 67W Charging Combo (Type-A) EU', 'Xiaomi 67W Charging Combo (Type-A) EU.png', 299000,
                [
                    "Nama produk",
                    "Xiaomi 67W Charging Combo (Tipe-A)",
                    "Model produk",
                    "MDY-12-EH",
                    "Tipe port",
                    "USB-A untuk Tipe-C",
                    "Parameter input",
                    "100-240V~, 50/60Hz, 1,7A",
                    "Parameter output",
                    "5 V⎓3 A / 5-20 V⎓6,2-3,25 A (Maks. 67 W)",
                    "Dimensi",
                    "73x49.3x28mm (excludes pin length)",
                    "Suhu pengoperasian",
                    "-10℃~40℃",
                ]),
        Product('Xiaomi Air Purifier 4 Pro', 'Xiaomi Air Purifier 4 Pro.png', 3499000,
                [
                    "ModelAC-M15- SC Tingkat Penyaluran Udara Bersih Partikel",
                    "(Partikel CADR)500 m³/jam",
                    "Berat BersihSekitar 6,8 kg",
                    "Dimensi Item275x275x680 mm",
                    "Tingkat Kebisingan≤65 dB(A)",
                    "Area jangkauan efektif35-60㎡",
                ]),
        Product('Xiaomi Portable Electronic Air Compressor 1S', 'Xiaomi Portable Electronic Air Compressor 1S.png', 549000,
                [
                    "Nama Xiaomi Portable Electric Air Compressor 1S",
                    "ModelMJCQB05QJ",
                    "Standar yang diterapkan QXMQJ0002-2019",
                    "Dimensi124 x 71 x 45,3 mm",
                    "(Kompresor udara, tidak termasuk selang udara)",
                    "Kisaran tekanan pemompaan0,2-10,3 bar/3-150 psi",
                    "Suhu pengoperasianPengisian: 0℃—45℃. Pengosongan: -10℃—45℃",
                    "Suhu penyimpanan-10℃ hingga 45℃",
                    "Kapasitas baterai14,8 Wh",
                    "Nilai kebisingan selama pengoperasian<80 dB pada jarak 1 meter",
                    "Parameter input5V ⎓ 2A",

                ]),
        Product('Xiaomi Robot Vacuum E10', 'Xiaomi Robot Vacuum E10.png', 2499000,
                [
                    "Name Robotic Vacuum Cleaner",
                    "Model numberB112",
                    "Main unit dimensionsΦ325x80mm",
                    "Rated power35W",
                    "Rated voltage14.4V⎓",
                    "Charging voltage20V⎓",
                    "Battery capacity2500mAh (rated capacity)",
                    "2600mAh (nominal capacity)",
                    "Charging dock modelCDZB112",
                    "Rated input20V⎓ 0.6A",
                    "Rated output20V⎓ 0.6A",
                    "Product dimensions146x122x87.5mm",
                ]),
        Product('Xiaomi Smart Air Purifier 4 Lite', 'Xiaomi Smart Air Purifier 4 Lite.png', 1799000,
                [
                    "Nama produk",
                    "Xiaomi Smart Air Purifier 4 Lite",
                    "Model produk",
                    "AC-M17-SC",
                    "Dimensi produk",
                    "240 x 240 x 533,5 mm",
                    "Berat bersih produk",
                    "Sekitar 4,8 kg",
                    "Area jangkauan efektif",
                    "25-43 m²",
                    "Kebisingan",
                    "≤ 61dB(A)",
                    "PM CADR",
                    "360m³/jam",
                    "Efisiensi Purifikasi Partikel",
                    "Tinggi",
                ]),
        Product('Xiaomi smart band 7', 'Xiaomi smart band 7.png', 699000,
                [
                    "46,5 mm x 20,7 mm x 12,25 mm",
                    "Dimensi tinggi, lebar, dan ketebalan",
                    "Berat: 13,5 g",
                    "Ukuran: 160 mm-224 mm",
                    "Bahan: TPU",
                    "Gesper tali: aloi aluminium",
                    "Layar Sentuh AMOLED 1,62 inci",
                    "Resolusi: 192 x 490 piksel 326 PPI",
                    "Kecerahan: hingga 500 nit, dapat disesuaikan",
                    "Kaca antigores dengan lapisan anti-sidik jari",
                    "Tema layar: 100+",
                    "Jenis pengisian daya: pengisian daya secara magnetik",
                    "Waktu pengisian daya: ≤2 jam",

                ]),
        Product('Xiaomi Smart Camera C300', 'Xiaomi Smart Camera C300.png', 599000,
                [
                    "Nama produk",
                    "Xiaomi Smart Camera C300",
                    "No model produkXMC01",
                    "Dimensi Produk115 x 78 x 78mm",
                    "Kompatibel dengan",
                    "Android 4.4 atau iOS 9.0 dan keatas",
                    "Koneksi nirkabel",
                    "Wi-Fi IEEE 802.11b/g/n 2.4Ghz",
                    "Berat produk327g",
                    "Input daya5V=1A",
                    "ApertureF1.4",
                    "Resolusi2304 x 1296",
                    "Video encodingH.265",
                    "Penyimpanan",
                    "Kartu Micro SD (mendukung hingga 256GB)",
                ]),
        Product('Xiaomi TV Stick 4K', 'Xiaomi TV Stick 4K.png', 699000,
                [
                    "Output Resolution",
                    "4k",
                    "CPU",
                    "Quad-core Cortex-A35",
                    "GPU",
                    "Mali-G31 MP2",
                    "RAM",
                    "2GB",
                    "Storage",
                    "8GB",
                    "Operating System",
                    "Android TV™ 11",
                    "Content",
                    "Netflix, Amazon Prime Video and Youtube pre-installed",
                ]),
        Product('Xiaomi Watch S1 Active', 'Xiaomi Watch S1 Active.png', 1999000,
                [
                    "Sensor:Sensor detak jantung (dengan sensor saturasi oksigen)",
                    "akselerometer, giroskop, sensor geomagnetik, sensor atmosfer" ,
                    "sensor cahaya ambien",
                    "Dimensi:46,5 x 47,3 x 11 mm (tidak termasuk tali dan bagian pinggiranya)",
                    "Sistem penentuan posisi satelit:GPS, GLONASS, GALILEO, BDS, QZSS",
                    "Bingkai:Poliamida yang diperkuat serat kaca",
                    "Kapasitas baterai470 mAh",
                    "Layar:Layar AMOLED 1,43",
                    "Peringkat tahan air:5 ATM",
                    "Resolusi:466 x 466",
                    "Suhu pengoperasian:-10℃-45℃",
                    "Tali:TPU hitam dan biru, silikon putih",
                ]),
        Product('Xiaomi12', 'Xiaomi12.png', 6999000,
                [
                    "RAM & Kapasitas Penyimpanan",
                    "8GB+256GBRAM LPDDR5 + Media Penyimpanan UFS 3.1",
                    "Dimensi",
                    "Tinggi: 152,7 mmLebar: 69,9 mmKetebalan: 8,16 mmBerat: 180 g",
                    "Layar",
                    "DotDisplay Super AMOLED 6,28” FHD+",
                    "Prosesor",
                    "Snapdragon® 8 Gen 1",
                    "Kamera Belakang",
                    "50MP kamera wide",
                    "Baterai & Pengisian Daya",
                    "Baterai 4500mAh (typ)Pengisian daya turbo 67W", 
                    "dengan kabel Pengisian daya turbo 50W",
                    "nirkabel Reverse charging 10W",
                    "nirkabelPengisi daya 67W",
                    "disertakanUSB tipe CXiaomi AdaptiveCharge",
                ]),
        Product('xiaomi12lite5G', 'xiaomi12lite5G.png', 4799000,
                [
                    "Design",
                    "Matte finish",
                    "Dimension: 159.3 x 73.7 x 7.29mm",
                    "Weight: 173g",
                    "Display",
                    "6.55 FHD+ AMOLED DotDisplay",
                    "Rear camera",
                    "108MP wide-angle camera",
                    "8MP ultra-wide angle camera",
                    "2MP macro camera",
                    "Rear camera photography features",
                    "Rear camera video features",
                    "Rear video recording",
                    "Front camera",
                    "32MP in-display selfie camera",
                    "Processor",
                    "Snapdragon® 778G",

                ]),
        Product('xiaomi12pro', 'xiaomi12pro.png', 12199000,
                [
                    "Layar",
                    "WQHD+ DotDisplay AMOLED 6,73",
                    "Dimensi",
                    "Tinggi: 163,6mmLebar: 74,6mmKetebalan: 8,16mmBerat: 205g",
                    "Kamera Belakang",
                    "Rangkaian 50MP kamera tripel pro-grade",
                    "Kamera depan",
                    "Kamera depan 32 MP di sisi atas layar",
                    "Memori",
                    "12GB + 256GB",
                    "Prosesor",
                    "Snapdragon® 8 Gen 1",
                    "Baterai & Pengisian Daya",
                    "Baterai 4600 mAh (typ)120W Xiaomi HyperCharge ",
                    "Mode boost untuk pengisian daya hingga 100 Persen selama 18 menit",
                ]),
        Product('Mi 360 Home Security Camera 2K', 'Mi 360 Home Security Camera 2K.png', 599000,
                [
                    "Nama produkMi 360° Home Security Camera 2K",
                    "Berat bersih produk310 g",
                    "No. model produkMJSXJ09CM",
                    "Input daya5V=2A",
                    "Suhu pengoperasian-10°C hingga 50°C",
                    "AperturF1.4",
                    "Lens angle110°",
                    "Resolusi2304 x 1296",
                    "Dimensi produk115 x 78 x 78 mm",
                    "Video encodingH.265",
                    "Kompatibel denganAndroid 4.4 & iOS 9.0 atau lebih baru",
                    "PenyimpananKartu Micro SD (mendukung hingga 32 GB)",

                ]),
        Product('XIAOMI TV A2 55_', 'XIAOMI TV A2 55.jpg', 5899000,
                [
                    "Tipe Layar: UHD 4K",
                    "Resolusi: 3840 x 2160",
                    "Gamut warna: DCI-P3 90% (umum)",
                    "Kedalaman warna: 1,07 miliar",
                    "Refresh rate: 60 Hz",
                    "MEMC: hingga UHD 60 Hz",
                    "Sudut tampilan: 178°(H)/178°(V)",
                    "Mendukung Dolby Vision®, HDR10, HLG",
                    "Speaker (Output Suara): 2 x 12 W",
                    "Mendukung Dolby Audio™ dan DTS-HD®",
                    "Android TV™ 10",
                    "CPU: Quad A55",
                    "GPU: Mali G52 MP2",
                    "RAM: 2 GB",
                    "Penyimpanan: 16 GB",
                    "Netflix, Amazon Prime Video, dan YouTube bawaan",

                ]),
        Product('XIAOMI TV P1E 65_', 'XIAOMI TV P1E 65.jpg', 9399000,
                [
                    "Tipe Layar",
                    "UHD 4K",
                    "Resolusi",
                    "3840 x 2160",
                    "Gamut warna",
                    "DCI-P3 78% (standar)",
                    "Kedalaman warna",
                    "1,07 miliar (8-bit + FRC)",
                    "Refresh rate",
                    "60 Hz",
                    "MEMC",
                    "UHD 60 Hz",
                    "Sudut tampilan",
                    "178°(H)/178°(V)",
                    "Mendukung HDR10, HLG, Dolby Vision®",
                ]),
            ]

    kumpulan_produk = KumpulanProduk(products)
    kumpulan_produk.mainloop()


# if __name__ == "__main__":
#     run()



#============================================================================================================================================#


# class SortingProduct:
#     def __init__(self, name, gambar, harga):
#         self.name = name
#         self.image_path = gambar
#         self.price = harga
#         # print("Ana pusing")


# class PriceSort(tk.Tk):
#     def __init__(self, barang):
#         super().__init__()
#         self.title("Price Bubble Sort")
#         self.geometry("1280x832")
#         self.products = barang

#         # Canvas with scrollbar
#         self.canvas = tk.Canvas(self, borderwidth=0, background="#F1EBC9")
#         self.barang_frame = tk.Frame(self.canvas, background="#F1EBC9")
#         self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)

#         self.canvas.configure(yscrollcommand=self.scrollbar.set)
#         self.scrollbar.pack(side="right", fill="y")
#         self.canvas.pack(side="left", fill="both", expand=True)
#         self.canvas.create_window((4, 4), window=self.barang_frame, anchor="nw")

#         self.barang_frame.bind("<Configure>", self.on_frame_configure)
#         self.canvas.bind("<Configure>", self.on_canvas_configure)

#         # Add products to the frame
#         self.products = barang
#         self.add_barang()

#         # Sort buttons
#         self.sort_button1 = tk.Button(self, text="High To Low", command=self.sort_high_to_low)
#         self.sort_button2 = tk.Button(self, text="Low To High", command=self.sort_low_to_high)
#         self.sort_button1.pack(side="left")
#         self.sort_button2.pack(side="right")

#     def add_barang(self):
#         num_columns = 5  # Number of columns
#         col = 0
#         row = 0

#         for barang in self.products:
#             # Load product image
#             image = Image.open(barang.image_path)
#             image = image.resize((100, 100), Image.ANTIALIAS)
#             photo = ImageTk.PhotoImage(image)

#             # Create product label
#             product_label = tk.Label(
#                 self.barang_frame,
#                 text=barang.name,
#                 image=photo,
#                 compound="top",
#                 font=("Helvetica", 9),
#                 bg="#ffffff",
#                 fg="black",
#             )
#             product_label.photo = photo
#             product_label.grid(row=row, column=col, padx=10, pady=10)

#             # Create price label
#             price_label = tk.Label(
#                 self.barang_frame,
#                 text=f"Price: {barang.price}",
#                 font=("Helvetica", 10),
#                 bg="#ffffff",
#                 fg="black",
#             )
#             price_label.grid(row=row + 1, column=col, padx=10, pady=5)

#             # Bind click event to product label
#             product_label.bind("<Button-1>", lambda event, p=barang: self.on_product_click(p))

#             col += 1
#             if col >= num_columns:
#                 col = 0
#                 row += 2

#     def on_frame_configure(self, event):
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))

#     def on_canvas_configure(self, event):
#         self.canvas.itemconfigure(self.product_frame, width=event.width)

#     def sort_high_to_low(self):
#         self.bubble_sort(reverse=True)
#         self.product_frame.destroy()
#         self.product_frame = tk.Frame(self.canvas, background="#ffffff")
#         self.canvas.create_window((4, 4), window=self.product_frame, anchor="nw")
#         self.add_products()

#     def sort_low_to_high(self):
#         self.bubble_sort(reverse=False)
#         self.product_frame.destroy()
#         self.product_frame = tk.Frame(self.canvas, background="#ffffff")
#         self.canvas.create_window((4, 4), window=self.product_frame, anchor="nw")
#         self.add_products()

#     def bubble_sort(self, reverse):
#         n = len(self.products)
#         for i in range(n - 1):
#             for j in range(0, n - i - 1):
#                 if reverse:
#                     if self.products[j].harga < self.products[j + 1].harga:
#                         self.products[j], self.products[j + 1] = self.products[j + 1], self.products[j]
#                 else:
#                     if self.products[j].harga > self.products[j + 1].harga:
#                         self.products[j], self.products[j + 1] = self.products[j + 1], self.products[j]

#     def on_product_click(self, product):
#         print(f"You clicked on product: {product.name}")

class SortingProduct:
    def __init__(self, name, image_path, price):
        self.name = name
        self.image_path = image_path
        self.price = price


class PriceSort(tk.Tk):
    def __init__(self, products):
        super().__init__()
        self.title("Price Bubble Sort")
        self.geometry("1280x832")
        self.products = products

        # Canvas with scrollbar
        self.canvas = tk.Canvas(self, borderwidth=0, background="#F1EBC9")
        self.product_frame = tk.Frame(self.canvas, background="#F1EBC9")
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4, 4), window=self.product_frame, anchor="nw")

        self.product_frame.bind("<Configure>", self.on_frame_configure)
        self.canvas.bind("<Configure>", self.on_canvas_configure)

        # Add products to the frame
        self.products = products
        self.add_products()

        # Sort buttons
        self.sort_button1 = tk.Button(self, text="High To Low", command=self.sort_high_to_low)
        self.sort_button2 = tk.Button(self, text="Low To High", command=self.sort_low_to_high)
        self.sort_button1.pack(side="left")
        self.sort_button2.pack(side="right")
        
        button2 = tk.Button(self, text="<< BACK",command=self.back)
        button2.place(x=1150, y=0.0, width=100.0, height=30.0) 
        
    def back(self):
        self.destroy()
        Newarrival()

    def add_products(self):
        num_columns = 5  # Number of columns
        col = 0
        row = 0

        for product in self.products:
            # Load product image
            image = Image.open(product.image_path)
            image = image.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)

            # Create product label
            product_label = tk.Label(
                self.product_frame,
                text=product.name,
                image=photo,
                compound="top",
                font=("Helvetica", 9),
                bg="#ffffff",
                fg="black",
            )
            product_label.photo = photo
            product_label.grid(row=row, column=col, padx=10, pady=10)

            # Create price label
            price_label = tk.Label(
                self.product_frame,
                text=f"Price: {product.price}",
                font=("Helvetica", 10),
                bg="#ffffff",
                fg="black",
            )
            price_label.grid(row=row + 1, column=col, padx=10, pady=5)

            # Bind click event to product label
            product_label.bind("<Button-1>", lambda event, p=product: self.on_product_click(p))

            col += 1
            if col >= num_columns:
                col = 0
                row += 2

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfigure(self.product_frame, width=event.width)

    def sort_high_to_low(self):
        self.bubble_sort(reverse=True)
        self.product_frame.destroy()
        self.product_frame = tk.Frame(self.canvas, background="#ffffff")
        self.canvas.create_window((4, 4), window=self.product_frame, anchor="nw")
        self.add_products()

    def sort_low_to_high(self):
        self.bubble_sort(reverse=False)
        self.product_frame.destroy()
        self.product_frame = tk.Frame(self.canvas, background="#ffffff")
        self.canvas.create_window((4, 4), window=self.product_frame, anchor="nw")
        self.add_products()

    def bubble_sort(self, reverse):
        n = len(self.products)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if reverse:
                    if self.products[j].price < self.products[j + 1].price:
                        self.products[j], self.products[j + 1] = self.products[j + 1], self.products[j]
                else:
                    if self.products[j].price > self.products[j + 1].price:
                        self.products[j], self.products[j + 1] = self.products[j + 1], self.products[j]

    def on_product_click(self, product):
        print(f"You clicked on product: {product.name}")



def lari ():
    products = [
            SortingProduct('Mi 37W Dual-Port Car Charger', 'Mi 37W Dual-Port Car Charger.png', 109000),
            SortingProduct('Mi 360 Camera (1080p)', 'Mi 360Camera (1080p).png', 449000),
            SortingProduct('Mi Curved Gaming Monitior 34', 'Mi Curved Gaming Monitor 34_.png', 5599000),
            SortingProduct('Mi Desktop Monitor 27”', 'Mi Desktop Monitor 27.png', 1699000),
            SortingProduct('Mi LCD Writing Tablet 13.5"', 'Mi LCD Writing Tablet 13.5&quot.png', 2699000),
            SortingProduct('Mi Robot Vacuum-Mop 2 Lite', 'Mi Robot Vacuum-Mop 2 Lite.png', 2799000),
            SortingProduct('Mi Router 4C', 'Mi Router 4C.png', 199000),
            SortingProduct('Mi Smart Air Fryer (3.5L)', 'Mi Smart Air Fryer (3.5L).png', 1199000),
            SortingProduct('Mi TV 4 43', 'Mi TV 4 43.png', 3599000),
            SortingProduct('Mi TV 4 55', 'Mi TV 4 55.png', 5999000),
            SortingProduct('Mi TV Stick', 'Mi TV Stick.png', 599000),
            SortingProduct('Mi Vacuum Cleaner Light', 'Mi Vacuum Cleaner Light.png', 1499000),
            SortingProduct('Mi Vacuum Cleaner Mini.jpg', 'Mi Vacuum Cleaner Mini.jpg.png', 649000),
            SortingProduct('Mi Watch Charging Dock', 'Mi Watch Charging Dock.png', 69000),
            SortingProduct('Mi WiFi Range Extender AC1200', 'Mi WiFi Range Extender AC1200.png', 249000),
            SortingProduct('Mi Wireless Switch', 'Mi Wireless Switch.png', 99000),
            SortingProduct('POCO F4 GT', 'POCO F4 GT.png', 7999000),
            SortingProduct('POCO F4', 'POCO F4.png', 5199000),
            SortingProduct('poco M4 pro', 'poco M4 pro.png', 3399000),
            SortingProduct('POCO M5', 'POCO M5.png', 2299000),
            SortingProduct('POCO M5s', 'POCO M5s.png', 2599000),
            SortingProduct('POCO X5 5G', 'POCO X5 5G.png', 3499000),
            SortingProduct('Redmi 10 2022', 'Redmi 10 2022.png', 2299000),
            SortingProduct('Redmi Buds 3 Pro', 'Redmi Buds 3 Pro.png', 699000),
            SortingProduct('Redmi buds 4 Pro', 'Redmi buds 4 Pro.png', 949000),
            SortingProduct('Redmi buds 4', 'Redmi buds 4.png', 549000),
            SortingProduct('Redmi Note 11 Pro 5G', 'Redmi Note 11 Pro 5G.png', 4099000),
            SortingProduct('Redmi Note 11 Pro', 'Redmi Note 11 Pro.png', 3699000),
            SortingProduct('Redmi Note 11', 'Redmi Note 11.png', 2699000),
            SortingProduct('Redmi Note 12 Pro 5G', 'Redmi Note 12 Pro 5G.png', 4599000),
            SortingProduct('Redmi Note 12', 'Redmi Note 12.png', 2999000),
            SortingProduct('Redmi Pad', 'Redmi Pad.png', 3499000),
            SortingProduct('Redmi Watch 3', 'Redmi Watch 3.png', 1199000),
            SortingProduct('RedmiBook 15', 'RedmiBook 15.png', 7499000),
            SortingProduct('Xiaomi 6A Type-A to Type-C Cable', 'Xiaomi 6A Type-A to Type-C Cable.png', 79000),
            SortingProduct('xiaomi 10t Pro', 'xiaomi 10t.png', 6999000),
            SortingProduct('xiaomi 11 T pro', 'xiaomi 11 T pro.png', 6199000),
            SortingProduct('xiaomi 11 T', 'xiaomi 11 T.png', 4999000),
            SortingProduct('Xiaomi 22.5W Power Bank 10000mAh', 'Xiaomi 22.5W Power Bank 10000mAh.png', 4599000),
            SortingProduct('Xiaomi 67W Charging Combo (Type-A) EU', 'Xiaomi 67W Charging Combo (Type-A) EU.png', 299000),
            SortingProduct('Xiaomi Air Purifier 4 Pro', 'Xiaomi Air Purifier 4 Pro.png', 3499000),
            SortingProduct('Xiaomi Portable Electronic Air Compressor 1S', 'Xiaomi Portable Electronic Air Compressor 1S.png', 549000),
            SortingProduct('Xiaomi Robot Vacuum E10', 'Xiaomi Robot Vacuum E10.png', 2499000),
            SortingProduct('Xiaomi Smart Air Purifier 4 Lite', 'Xiaomi Smart Air Purifier 4 Lite.png', 1799000),
            SortingProduct('Xiaomi smart band 7', 'Xiaomi smart band 7.png', 699000),
            SortingProduct('Xiaomi Smart Camera C300', 'Xiaomi Smart Camera C300.png', 599000),
            SortingProduct('Xiaomi TV Stick 4K', 'Xiaomi TV Stick 4K.png', 699000),
            SortingProduct('Xiaomi Watch S1 Active', 'Xiaomi Watch S1 Active.png', 1999000),
            SortingProduct('Xiaomi12', 'Xiaomi12.png', 6999000),
            SortingProduct('xiaomi12lite5G', 'xiaomi12lite5G.png', 4799000),
            SortingProduct('xiaomi12pro', 'xiaomi12pro.png', 12199000),
            SortingProduct('Mi 360 Home Security Camera 2K', 'Mi 360 Home Security Camera 2K.png', 599000),
            SortingProduct('XIAOMI TV A2 55_', 'XIAOMI TV A2 55.jpg', 5899000),
            SortingProduct('XIAOMI TV P1E 65_', 'XIAOMI TV P1E 65.jpg', 9399000),
        ]
    bisa=PriceSort(products)
    bisa.mainloop()


#======================================================================================================================================#



# class SortingProduct:
#     def __init__(self, name, image_path, price):
#         self.name = name
#         self.image_path = image_path
#         self.price = price


# class PriceSort(tk.Toplevel):
#     def __init__(self, products):
#         super().__init__()
#         self.title("Price Binery Sort")
#         self.geometry("1280x832")  

#         # Canvas with scrollbar
#         self.canvas = tk.Canvas(self, borderwidth=0, background="#F1EBC9")
#         self.product_frame = tk.Frame(self.canvas, background="#F1EBC9")
#         self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)

#         self.canvas.configure(yscrollcommand=self.scrollbar.set)
#         self.scrollbar.pack(side="right", fill="y")
#         self.canvas.pack(side="left", fill="both", expand=True)
#         self.canvas.create_window((4, 4), window=self.product_frame, anchor="nw")

#         self.product_frame.bind("<Configure>", self.on_frame_configure)
#         self.canvas.bind("<Configure>", self.on_canvas_configure)

#         # Add products to the frame
#         self.products = products
#         self.add_products()

#         # Sort buttons
#         self.sort_button1 = tk.Button(self, text="High To Low", command=self.sort_high_to_low)
#         self.sort_button2 = tk.Button(self, text="Low To High", command=self.sort_low_to_high)
#         self.sort_button1.pack(side="left")
#         self.sort_button2.pack(side="right")

#     def add_products(self):
#         num_columns = 5  # Number of columns
#         col = 0
#         row = 0

#         for product in self.products:
#             # Load product image
#             image = Image.open(product.image_path)
#             image = image.resize((100, 100), Image.ANTIALIAS)
#             photo = ImageTk.PhotoImage(image)

#             # Create product label
#             product_label = tk.Label(
#                 self.product_frame,
#                 text=product.name,
#                 image=photo,
#                 compound="top",
#                 font=("Helvetica", 9),
#                 bg="#ffffff",
#                 fg="black",
#             )
#             product_label.photo = photo
#             product_label.grid(row=row, column=col, padx=10, pady=10)

#             # Create price label
#             price_label = tk.Label(
#                 self.product_frame,
#                 text=f"Price: {product.price}",
#                 font=("Helvetica", 10),
#                 bg="#ffffff",
#                 fg="black",
#             )
#             price_label.grid(row=row + 1, column=col, padx=10, pady=5)

#              # Bind click event to product label
#             product_label.bind("<Button-1>", lambda event, p=product: self.on_product_click(p))

#             col += 1
#             if col >= num_columns:
#                 col = 0
#                 row += 2

#     def on_frame_configure(self, event):
#         self.canvas.configure(scrollregion=self.canvas.bbox("all"))

#     def on_canvas_configure(self, event):
#         self.canvas.itemconfigure(self.product_frame, width=event.width)

#     def sort_high_to_low(self):
#         self.binary_sort(products=self.products, start=0, end=len(self.products) - 1, reverse=True)
#         self.product_frame.destroy()
#         self.product_frame = tk.Frame(self.canvas, background="#ffffff")
#         self.canvas.create_window((4, 4), window=self.product_frame, anchor="nw")
#         self.add_products()

#     def sort_low_to_high(self):
#         self.binary_sort(products=self.products, start=0, end=len(self.products) - 1, reverse=False)
#         self.product_frame.destroy()
#         self.product_frame = tk.Frame(self.canvas, background="#ffffff")
#         self.canvas.create_window((4, 4), window=self.product_frame, anchor="nw")
#         self.add_products()

#     def bubble_sort(self, products, start, end, reverse):
#         if start < end:
#             mid = (start + end) // 2
#             self.bubble_sort(products, start, mid, reverse)
#             self.bubble_sort(products, mid + 1, end, reverse)
#             self.partition(products, start, mid, end, reverse)

#     def bubbleSort (data):
#         for i in range (len (data) -1,0, -1):
#             print ("langkah")
#             for j in range(0, len (data) -1):
#                 if (data[j] > data[j+1]):
#                     data[j],data[j+1] = data[j+1], data[j]
#             print (data)

#     # def bubble_sort(self, products, start, end, reverse):
#     #     if start < end:
#     #         pivot = self.partition(products, start, end, reverse)
#     #         self.bubble_sort(products, start, pivot - 1, reverse)
#     #         self.bubble_sort(products, pivot + 1, end, reverse)

#     def partition(self, products, start, end, reverse):
#         pivot = products[end].price
#         i = start - 1
#         for i in range (len (products) -1,0, -1):
#             print ("langkah")
#             for j in range(0, len (products) -1):
#                 if (products[j] > products[j+1]):
#                     products[j],products[j+1] = products[j+1], products[j]
#             print (products)

#     # def merge(self, products, start, mid, end, reverse):
#     #     left = products[start:mid + 1]
#     #     right = products[mid + 1:end + 1]

#     #     i = j = 0
#     #     k = start

#     #     if reverse:
#     #         while i < len(left) and j < len(right):
#     #             if left[i].price > right[j].price:
#     #                 products[k] = left[i]
#     #                 i += 1
#     #             else:
#     #                 products[k] = right[j]
#     #                 j += 1
#     #             k += 1
#     #     else:
#     #         while i < len(left) and j < len(right):
#     #             if left[i].price < right[j].price:
#     #                 products[k] = left[i]
#     #                 i += 1
#     #             else:
#     #                 products[k] = right[j]
#     #                 j += 1
#     #             k += 1

#     #     while i < len(left):
#     #         products[k] = left[i]
#     #         i += 1
#     #         k += 1

#     #     while j < len(right):
#     #         products[k] = right[j]
#     #         j += 1
#     #         k += 1

#     def on_product_click(self, product):
#         print(f"You clicked on product: {product.name}")


# # Example usage
# if __name__ == "__main__":
#     products = [
#     SortingProduct('Mi 37W Dual-Port Car Charger', 'PRODUCT/Mi 37W Dual-Port Car Charger.png', 109000),
#     SortingProduct('Mi 360 Camera (1080p)', 'PRODUCT/Mi 360° Camera (1080p).png', 449000),
#     SortingProduct('Mi Curved Gaming Monitior 34', 'PRODUCT/Mi Curved Gaming Monitor 34_.png', 5599000),
#     SortingProduct('Mi Desktop Monitor 27”', 'PRODUCT/Mi Desktop Monitor 27”.png', 1699000),
#     SortingProduct('Mi LCD Writing Tablet 13.5"', 'PRODUCT/Mi LCD Writing Tablet 13.5&quot.png', 2699000),
#     SortingProduct('Mi Robot Vacuum-Mop 2 Lite', 'PRODUCT/Mi Robot Vacuum-Mop 2 Lite.png', 2799000),
#     SortingProduct('Mi Router 4C', 'PRODUCT/Mi Router 4C.png', 199000),
#     SortingProduct('Mi Smart Air Fryer (3.5L)', 'PRODUCT/Mi Smart Air Fryer (3.5L).png', 1199000),
#     SortingProduct('Mi TV 4 43', 'PRODUCT/Mi TV 4 43.png', 3599000),
#     SortingProduct('Mi TV 4 55', 'PRODUCT/Mi TV 4 55.png', 5999000),
#     SortingProduct('Mi TV Stick', 'PRODUCT/Mi TV Stick.png', 599000),
#     SortingProduct('Mi Vacuum Cleaner Light', 'PRODUCT/Mi Vacuum Cleaner Light.png', 1499000),
#     SortingProduct('Mi Vacuum Cleaner Mini.jpg', 'PRODUCT/Mi Vacuum Cleaner Mini.jpg.png', 649000),
#     SortingProduct('Mi Watch Charging Dock', 'PRODUCT/Mi Watch Charging Dock.png', 69000),
#     SortingProduct('Mi WiFi Range Extender AC1200', 'PRODUCT/Mi WiFi Range Extender AC1200.png', 249000),
#     SortingProduct('Mi Wireless Switch', 'PRODUCT/Mi Wireless Switch.png', 99000),
#     SortingProduct('POCO F4 GT', 'PRODUCT/POCO F4 GT.png', 7999000),
#     SortingProduct('POCO F4', 'PRODUCT/POCO F4.png', 5199000),
#     SortingProduct('poco M4 pro', 'PRODUCT/poco M4 pro.png', 3399000),
#     SortingProduct('POCO M5', 'PRODUCT/POCO M5.png', 2299000),
#     SortingProduct('POCO M5s', 'PRODUCT/POCO M5s.png', 2599000),
#     SortingProduct('POCO X5 5G', 'PRODUCT/POCO X5 5G.png', 3499000),
#     SortingProduct('Redmi 10 2022', 'PRODUCT/Redmi 10 2022.png', 2299000),
#     SortingProduct('Redmi Buds 3 Pro', 'PRODUCT/Redmi Buds 3 Pro.png', 699000),
#     SortingProduct('Redmi buds 4 Pro', 'PRODUCT/Redmi buds 4 Pro.png', 949000),
#     SortingProduct('Redmi buds 4', 'PRODUCT/Redmi buds 4.png', 549000),
#     SortingProduct('Redmi Note 11 Pro 5G', 'PRODUCT/Redmi Note 11 Pro 5G.png', 4099000),
#     SortingProduct('Redmi Note 11 Pro', 'PRODUCT/Redmi Note 11 Pro.png', 3699000),
#     SortingProduct('Redmi Note 11', 'PRODUCT/Redmi Note 11.png', 2699000),
#     SortingProduct('Redmi Note 12 Pro 5G', 'PRODUCT/Redmi Note 12 Pro 5G.png', 4599000),
#     SortingProduct('Redmi Note 12', 'PRODUCT/Redmi Note 12.png', 2999000),
#     SortingProduct('Redmi Pad', 'PRODUCT/Redmi Pad.png', 3499000),
#     SortingProduct('Redmi Watch 3', 'PRODUCT/Redmi Watch 3.png', 1199000),
#     SortingProduct('RedmiBook 15', 'PRODUCT/RedmiBook 15.png', 7499000),
#     SortingProduct('Xiaomi 6A Type-A to Type-C Cable', 'PRODUCT/Xiaomi 6A Type-A to Type-C Cable.png', 79000),
#     SortingProduct('xiaomi 10t Pro', 'PRODUCT/xiaomi 10t.png', 6999000),
#     SortingProduct('xiaomi 11 T pro', 'PRODUCT/xiaomi 11 T pro.png', 6199000),
#     SortingProduct('xiaomi 11 T', 'PRODUCT/xiaomi 11 T.png', 4999000),
#     SortingProduct('Xiaomi 22.5W Power Bank 10000mAh', 'PRODUCT/Xiaomi 22.5W Power Bank 10000mAh.png', 4599000),
#     SortingProduct('Xiaomi 67W Charging Combo (Type-A) EU', 'PRODUCT/Xiaomi 67W Charging Combo (Type-A) EU.png', 299000),
#     SortingProduct('Xiaomi Air Purifier 4 Pro', 'PRODUCT/Xiaomi Air Purifier 4 Pro.png', 3499000),
#     SortingProduct('Xiaomi Portable Electronic Air Compressor 1S', 'PRODUCT/Xiaomi Portable Electronic Air Compressor 1S.png', 549000),
#     SortingProduct('Xiaomi Robot Vacuum E10', 'PRODUCT/Xiaomi Robot Vacuum E10.png', 2499000),
#     SortingProduct('Xiaomi Smart Air Purifier 4 Lite', 'PRODUCT/Xiaomi Smart Air Purifier 4 Lite.png', 1799000),
#     SortingProduct('Xiaomi smart band 7', 'PRODUCT/Xiaomi smart band 7.png', 699000),
#     SortingProduct('Xiaomi Smart Camera C300', 'PRODUCT/Xiaomi Smart Camera C300.png', 599000),
#     SortingProduct('Xiaomi TV Stick 4K', 'PRODUCT/Xiaomi TV Stick 4K.png', 699000),
#     SortingProduct('Xiaomi Watch S1 Active', 'PRODUCT/Xiaomi Watch S1 Active.png', 1999000),
#     SortingProduct('Xiaomi12', 'PRODUCT/Xiaomi12.png', 6999000),
#     SortingProduct('xiaomi12lite5G', 'PRODUCT/xiaomi12lite5G.png', 4799000),
#     SortingProduct('xiaomi12pro', 'PRODUCT/xiaomi12pro.png', 12199000),
#     SortingProduct('Mi 360 Home Security Camera 2K', 'PRODUCT/Mi 360° Home Security Camera 2K.png', 599000),
#     SortingProduct('XIAOMI TV A2 55_', 'PRODUCT/XIAOMI TV A2 55.jpg', 5899000),
#     SortingProduct('XIAOMI TV P1E 65_', 'PRODUCT/XIAOMI TV P1E 65.jpg', 9399000),
# ]

    # root = tk.Tk()
    # app = PriceSort(root, products)
    # root.mainloop()

#======================================================================================================================================#


# class Payment:
#     def __init__(self):
#         self.window = Tk()
#         self.window.title("Online Shop Login")
#         self.window.geometry("1280x832")
#         self.window.configure(bg="#FFFFFF")

#         self.nama_var = StringVar()
#         self.almt_var = StringVar()
#         self.tlp_var = StringVar()
#         self.bayar_var = StringVar()
#         self.tkt_var = StringVar()
#         self.banyak_var = StringVar()

#         canvas = Canvas(
#             self.window, bg="#FFFFFF", height=832, width=1280, bd=0, highlightthickness=0, relief="ridge"
#         )
#         canvas.place(x=0, y=0)

#         image_image_1 = PhotoImage(file=("image_1.png"))
#         image_1 = canvas.create_image(320.0, 416.0, image=image_image_1)


#         ttl = Label(canvas, text="NAMA\t:", font=("catalyc", 15))
#         ttl.place(x=700, y=200)
#         ttl_isi = Entry(canvas, bd=5, textvariable=self.nama_var, bg="white")
#         ttl_isi.place(x=900, y=200, width=300, height=30)

#         no = Label(canvas, text="ALAMAT\t:", font=("catalyc", 15))
#         no.place(x=700, y=250)
#         no_dpn = Entry(canvas, bd=5, textvariable=self.almt_var, bg="white")
#         no_dpn.place(x=900, y=250, width=300, height=30)

#         umur = Label(canvas, text="No.Telp :", font=("catalyc", 15))
#         umur.place(x=700, y=300)
#         umur_isi = Entry(canvas, bd=5, textvariable=self.tlp_var, bg="white")
#         umur_isi.place(x=900, y=300, width=300, height=30)

#         asal = Label(canvas, text="PEMBAYARAN :", font=("catalyc", 15))
#         asal.place(x=700, y=350)
#         asal_isi = ttk.Combobox(
#             canvas,
#             values=[
#                 'Cash On Delivery', 'BCA', 'BRI', 'BNI', 'BTN', 'BUKOPIN', 'CIMB NIAGA', 'DANAMON INDONESIA', 'JATIM', 'MANDIRI', 'MAYBANK', 'MAYAPADA', 
#                                                    'MEGA SYARIAH', 'MESTIKA', 'NAGARI', 'PANIN', 'SEABANK INDONESIA', 'SINAR MAS'],
#             textvariable=self.bayar_var,
#         )
#         asal_isi.place(x=900, y=350, width=300, height=30)

#         jenis_tkt = Label(canvas, text="LAYANAN PENGIRIM :", font=("catalyc", 15))
#         jenis_tkt.place(x=700, y=400)
#         jenis_isi = ttk.Combobox(
#             canvas,
#             values=["SiCepat", "J&T Express", "Ninja Express", "AnterAja"],
#             textvariable=self.tkt_var,
#         )
#         jenis_isi.place(x=900, y=400, width=300, height=30)

#         banyak = Label(canvas, text="MASA PENGIRIMAN :", font=("catalyc", 15))
#         banyak.place(x=700, y=450)
#         banyak_isi = ttk.Combobox(
#             canvas,
#             values=["INSTANT", "NEXT DAY", "ONE WEEK", "NORMAL"],
#             textvariable=self.banyak_var,
#         )
#         banyak_isi.place(x=900, y=450, width=300, height=30)

#         kop = Button(canvas,text="SIMPAN",width=10,height=1,command=self.save_data,font=('Microsoft YaHei UI Light', 12,"bold"))
#         kop.place(x=851.0000610351562,y=564.0,width=175.0,height=60.0)
#         button_image_0 = PhotoImage(file="back.png")
#         data = Button(canvas,image=button_image_0,width=10,command=self.back)
#         data.place(x=0.0, y=0.0, width=35.0, height=30.0)
#         self.window.resizable(True, True)
#         self.window.mainloop()

#     def save_data(self):
#         nama = self.nama_var.get()
#         alamat = self.almt_var.get()
#         no_telp = self.tlp_var.get()
#         pembayaran = self.bayar_var.get()
#         layanan_pengiriman = self.tkt_var.get()
#         masa_pengiriman = self.banyak_var.get()

#         # Check if all fields are filled
#         if not all([nama, alamat, no_telp, pembayaran, layanan_pengiriman, masa_pengiriman]):
#             messagebox.showwarning("Incomplete Data", "Please fill in all the fields.")
#             return

#         data = [[nama, alamat, no_telp, pembayaran, layanan_pengiriman, masa_pengiriman]]
#         file_path = "data pembayaran.csv"  # Specify the desired file path for saving the data

#         # Check if the file exists
#         file_exists = os.path.isfile(file_path)

#         with open(file_path, "a", newline="") as file:
#             writer = csv.writer(file)

#             # Write the data only if the file is empty
#             if not file_exists:
#                 header = ["Nama", "Alamat", "No. Telp", "Pembayaran", "Layanan Pengiriman", "Masa Pengiriman"]
#                 writer.writerow(header)

#             writer.writerows(data)

#         # Reset the entry fields
#         self.nama_var.set("")
#         self.almt_var.set("")
#         self.tlp_var.set("")
#         self.bayar_var.set("")
#         self.tkt_var.set("")
#         self.banyak_var.set("")

#         # Show message box
#         messagebox.showinfo("Data Saved", "The data has been saved successfully.")
    
#     def run(self):
#         self.window.mainloop()


# if __name__ == "__main__":
#     app = App()

class Payment:
    def __init__(self):
        self.window = Tk()
        self.window.title("Online Shop Login")
        self.window.geometry("1280x832")
        self.window.configure(bg="#FFFFFF")

        self.nama_var = StringVar()
        self.almt_var = StringVar()
        self.tlp_var = StringVar()
        self.bayar_var = StringVar()
        self.tkt_var = StringVar()
        self.banyak_var = StringVar()

        canvas = Canvas(
            self.window, bg="#FFFFFF", height=832, width=1280, bd=0, highlightthickness=0, relief="ridge"
        )
        canvas.place(x=0, y=0)

        image_image_1 = PhotoImage(file=("image_1.png"))
        image_1 = canvas.create_image(320.0, 416.0, image=image_image_1)

        ttl = Label(canvas, text="NAMA\t:", font=("catalyc", 15))
        ttl.place(x=700, y=200)
        ttl_isi = Entry(canvas, bd=5, textvariable=self.nama_var, bg="white")
        ttl_isi.place(x=900, y=200, width=300, height=30)

        no = Label(canvas, text="ALAMAT\t:", font=("catalyc", 15))
        no.place(x=700, y=250)
        no_dpn = Entry(canvas, bd=5, textvariable=self.almt_var, bg="white")
        no_dpn.place(x=900, y=250, width=300, height=30)

        umur = Label(canvas, text="No.Telp :", font=("catalyc", 15))
        umur.place(x=700, y=300)
        umur_isi = Entry(canvas, bd=5, textvariable=self.tlp_var, bg="white")
        umur_isi.place(x=900, y=300, width=300, height=30)

        asal = Label(canvas, text="PEMBAYARAN :", font=("catalyc", 15))
        asal.place(x=700, y=350)
        asal_isi = ttk.Combobox(
            canvas,
            values=[
                'Cash On Delivery', 'BCA', 'BRI', 'BNI', 'BTN', 'BUKOPIN', 'CIMB NIAGA', 'DANAMON INDONESIA', 'JATIM', 'MANDIRI', 'MAYBANK', 'MAYAPADA', 
                'MEGA SYARIAH', 'MESTIKA', 'NAGARI', 'PANIN', 'SEABANK INDONESIA', 'SINAR MAS'
            ],
            textvariable=self.bayar_var,
            state='readonly'  # Set the state to readonly
        )
        asal_isi.place(x=900, y=350, width=300, height=30)

        jenis_tkt = Label(canvas, text="LAYANAN PENGIRIM :", font=("catalyc", 15))
        jenis_tkt.place(x=700, y=400)
        jenis_isi = ttk.Combobox(
            canvas,
            values=["SiCepat", "J&T Express", "Ninja Express", "AnterAja"],
            textvariable=self.tkt_var,
            state='readonly'  # Set the state to readonly
        )
        jenis_isi.place(x=900, y=400, width=300, height=30)

        banyak = Label(canvas, text="MASA PENGIRIMAN :", font=("catalyc", 15))
        banyak.place(x=700, y=450)
        banyak_isi = ttk.Combobox(
            canvas,
            values=["INSTANT", "NEXT DAY", "ONE WEEK", "NORMAL"],
            textvariable=self.banyak_var,
            state='readonly'  # Set the state to readonly
        )
        banyak_isi.place(x=900, y=450, width=300, height=30)

        kop = Button(canvas, text="SIMPAN", width=10, height=1, command=self.save_data, font=('Microsoft YaHei UI Light', 12, "bold"))
        kop.place(x=851.0000610351562, y=564.0, width=175.0, height=60.0)
        button_image_0 = PhotoImage(file="back.png")
        data = Button(self.window, image=button_image_0, width=10, command=self.back)
        data.place(x=0.0, y=0.0, width=35.0, height=30.0)
        self.window.resizable(True, True)
        self.window.mainloop()

    def save_data(self):
        nama = self.nama_var.get()
        alamat = self.almt_var.get()
        no_telp = self.tlp_var.get()
        pembayaran = self.bayar_var.get()
        layanan_pengiriman = self.tkt_var.get()
        masa_pengiriman = self.banyak_var.get()

        # Check if all fields are filled
        if not all([nama, alamat, no_telp, pembayaran, layanan_pengiriman, masa_pengiriman]):
            messagebox.showwarning("Pengiriman Data Gagal", "Tolonh masukkan data dengan lengkap !")
            return

        data = [[nama, alamat, no_telp, pembayaran, layanan_pengiriman, masa_pengiriman]]
        file_path = "data_pembayaran.csv"  # Specify the desired file path for saving the data

        # Check if the file exists
        file_exists = os.path.isfile(file_path)

        with open(file_path, "a", newline="") as file:
            writer = csv.writer(file)

            # Write the data only if the file is empty
            if not file_exists:
                header = ["Nama", "Alamat", "No. Telp", "Pembayaran", "Layanan Pengiriman", "Masa Pengiriman"]
                writer.writerow(header)

            writer.writerows(data)

        # Reset the entry fields
        self.nama_var.set("")
        self.almt_var.set("")
        self.tlp_var.set("")
        self.bayar_var.set("")
        self.tkt_var.set("")
        self.banyak_var.set("")

        # Show message box
        messagebox.showinfo("Data Tersimpan", "Pemesanan Anda berhasil di Lakukan.")

    def back(self):
        self.window.destroy()
        Newarrival()
    def run(self):
        self.window.mainloop()


#======================================================================================================================================#



if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    app = OnlineShop()
    app.window.mainloop()
    
