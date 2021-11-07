import tkinter as tk
from tkinter import font

def rungui():
    root = tk.Tk()
    root.title("Flashcards in a Flash")

    canvas = tk.Canvas(root, width=600, height=300)
    canvas.grid(columnspan=4, rowspan=10)
    labelList = []

    instructions = tk.Label(root, text="Import texts or image to create flashcards", font="Helvetica")
    instructions.grid(columnspan=4, column=0, row=0)

    def removeLabel():
        if len(labelList) != 0:
            labelList[0].grid_forget()
            labelList.clear()

    def addTextToBox(): 
        removeLabel()
        textInstructions = tk.Label(root, text="Enter texts", font="Helvetica")
        textInstructions.grid(columnspan=4, column=0, row=3) 
        labelList.append(textInstructions)
        text_box = tk.Text(root, height=20, width=75, padx = 15, pady = 15)
        text_box.grid(columnspan=2, column=1, rowspan=2, row=7)

        submit_text = tk.StringVar()
        submitBtn = tk.Button(root,textvariable=submit_text, font="Helvetica", bg = "#20bebe", fg="white", height=1, width=10, command=lambda:writeToFile())
        submit_text.set("submit")
        submitBtn.grid(columnspan=2, column=1,row=9)
        def writeToFile():
            text = text_box.get("1.0", "end")
            file1 = open("input.txt", "w+")
            file1.write(text)



    def addImageToBox():  
        removeLabel()
        imageInstructions = tk.Label(root, text="Enter image's file path", font="Helvetica")
        imageInstructions.grid(columnspan=4, column=0, row=3)  
        labelList.append(imageInstructions)
        text_box = tk.Text(root, height=20, width=75, padx = 15, pady = 15)
        text_box.grid(columnspan=2, column=1, rowspan=2, row=7)

        submit_text = tk.StringVar()
        submitBtn = tk.Button(root,textvariable=submit_text, font="Helvetica", bg = "#20bebe", fg="white", height=1, width=10, command=lambda:writeToFile())
        submit_text.set("submit")
        submitBtn.grid(columnspan=2, column=1,row=9)
        def writeToFile():
            text = text_box.get("1.0", "end")
            file1 = open("guiimage.txt", "w+")
            file1.write(text)




    import_text = tk.StringVar()
    importTextBtn = tk.Button(root,textvariable=import_text, font="Helvetica", bg = "#20bebe", fg="white", height=1, width=10, command=lambda:addTextToBox(),)
    import_text.set("Import Text")
    importTextBtn.grid(column=1, row=2)

    import_image = tk.StringVar()
    importImageBtn = tk.Button(root,textvariable=import_image, font="Helvetica", bg = "#20bebe", fg="white", height=1, width=10, command=lambda:addImageToBox())
    import_image.set("Import Image")
    importImageBtn.grid(column=2, row=2)


    canvas = tk.Canvas(root, width=600, height=250)
    canvas.grid(columnspan=4)




    root.mainloop()


