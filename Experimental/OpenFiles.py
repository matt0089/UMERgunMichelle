import tkinter as tk
from tkinter.filedialog import askopenfilenames
from os.path import split

def open_multiple():
    filenames = []
    title = "Choose Files"
    while True:
        filename = askopenfilenames(title=title)
        if not filename:
            break
        filenames.extend(filename)
        title = "Got {}. Next filename".format(split(filenames[-1])[1])
    return filenames

if __name__ == "__main__":
    open_multiple()