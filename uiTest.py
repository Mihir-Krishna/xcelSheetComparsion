import tkinter as tk
from tkinter import filedialog
from main import compareExcel

window = tk.Tk()

window.title("excel comparator")
window.geometry("500x400")

excel1Path = ""
excel2Path = ""

label = tk.Label(window, text="Excel comparator tool")
label.pack()


def chooseFile1():
    global excel1Path
    excel1Path = filedialog.askopenfilename()
    print(excel1Path)

def chooseFile2():
    global excel2Path
    excel2Path = filedialog.askopenfilename()
    print(excel2Path)

button = tk.Button(window, text="priya's first xcel", command=chooseFile1)
button.pack()

button = tk.Button(window, text="priya's first xcel", command=chooseFile2)
button.pack()


def sendFilesToMain():
    compareExcel(excel1Path, excel2Path)
    
button = tk.Button(window, text="compare", command=sendFilesToMain)
button.pack()

window.mainloop()



