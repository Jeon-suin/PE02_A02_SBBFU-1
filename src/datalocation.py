import tkinter
from tkinter import filedialog

window = tkinter.Tk()
window.withdraw()
dirPath = filedialog.askdirectory(parent=window, initialdir="./dat", title='Please select data.')

def location(dirpath):
    file_Path = '.\\'+dirpath[dirpath.find('dat'):].replace("/","\\")+'\\**\*LMZ?.xml'
    return file_Path


# C:/Download/PE02_A02_SBBFU/dat/P184640


path = location(dirPath)
window.destroy()