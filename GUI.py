from tkinter import *
from tkinter import filedialog
from Splitter import SplitFile
from Combiner import CombineFiles

window = Tk()

window.title("Excelor")

def openFile():
    file = filedialog.askopenfile()
    return file.name

def openFolder():
    folder = filedialog.askdirectory()
    return folder

e = Entry(window)
e.grid(row=1, column=1)

n = Entry(window)
n.grid(row=1, column=2)

label1 = Label(window, text="Column Name")
label1.grid(row=0, column=1)

label2 = Label(window, text="File 1 or Sheet 2")
label2.grid(row=0, column=2)

button2 = Button(text="Split File", command=lambda: SplitFile(openFile(), e.get(), n.get()))
button2.grid(row=1, column=3)

button3 = Button(text="Combine Folder", command=lambda: CombineFiles(openFolder()))
button3.grid(row=2, column=3)


window.mainloop()