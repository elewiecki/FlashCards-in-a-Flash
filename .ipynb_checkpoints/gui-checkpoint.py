import tkinter as tk
from tkinter import filedialog, Text
import os



def rungui():

    root = tk.Tk()

    canvas1 = tk.Canvas(root, width = 600, height = 300)
    canvas1.pack()

    frame = tk.Frame(root, bg ="white")
    frame.place(relwidth=0.8, relheight=0.8, relx= 0.1, rely=0.1, )

    def addText():
        text = textWidget.get("1.0", "end")
        file1 = open("input.txt", "w+", encoding ='utf8')
        file1.write(text)
        

    textWidget = Text(root, height = 10, width = 100)
    textWidget.pack()
    importText = tk.Button(root, text="Submit Text", padx = 10, pady = 15, fg ="white", bg="#263D42", command=addText)
    importText.place(relx = 0.0, rely=15)
    importText.pack()

    importImg = tk.Button(root, text="Import Image", padx = 10, pady = 15, fg ="white", bg="#263D42")
    importImg.place(relx = 0.0, rely=15)
    importImg.pack()

    root.mainloop()

rungui()