import customtkinter
from tkinter import messagebox
import tkinter.messagebox
import webbrowser
import csv


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



class Window:
    

    def __init__(self,master):
        self.master=master
        self.frame = customtkinter.CTkFrame(self.master)
        self.frame.pack(pady=20,padx=60,fill='both',expand=True)

        self.label = customtkinter.CTkLabel(self.frame, text="Password Manager")
        self.label.pack(pady=8,padx=10)

        self.entry1 = customtkinter.CTkEntry(self.frame, placeholder_text='username',placeholder_text_color='grey')
        self.entry1.pack(pady=15,padx=10)

        self.entry2 = customtkinter.CTkEntry(self.frame, placeholder_text='password',placeholder_text_color='grey',show='*')
        self.entry2.pack(pady=15,padx=10)
        
        self.entry3 = customtkinter.CTkEntry(self.frame, placeholder_text='Notes',placeholder_text_color='grey')
        self.entry3.pack(pady=15,padx=10)
        

        self.button = customtkinter.CTkButton(self.frame, text = 'Save', command = self.add_item)
        self.button.pack(pady=15,padx=10)
    
    def add_item(self):
        c1 = self.entry1.get()
        c2 = self.entry2.get()
        c3 = self.entry3.get()
        objects = [c1,c2,c3]
        f = open("passwords.csv","a",newline='')
        w = csv.writer(f)
        w.writerow(objects)







root = customtkinter.CTk()
root.geometry("600x400")

window = Window(root)
root.mainloop()





