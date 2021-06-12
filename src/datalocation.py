import tkinter
from tkinter import filedialog

window = tkinter.Tk()
window.withdraw()
dirPath = filedialog.askdirectory(parent=window, initialdir="./dat", title='데이터를 선택해주세요.')

def location(dirpath):
    file_Path = '.\\'+dirpath[dirpath.find('dat'):].replace("/","\\")+'**\*LMZ?.xml'
    return file_Path

path = location(dirPath)
window.destroy()