from tkinter import *
import tkinter as tk
import tkinter.ttk
import tkinter.font
import os
import time
import glob
from tqdm import tqdm
from src import process , IVfitting, Measured_Spectra , Processed_spectra , Ref_fitting ,tocsv

def checkbox(file_path):
    window = Tk()
    window.title("check box test")

    def status1_print():
        return (CheckVar1.get())

    def status2_print():
        return (CheckVar2.get())

    def status3_print():
        return (CheckVar3.get())

    def close_window():
        window.destroy()

    def save_status(event):
        a = status1_print()
        b = status2_print()
        c = status3_print()
        xml = []
        for filename in glob.glob(file_path, recursive=True):
            xml.append(filename)

        start = time.time()
        xml_tqdm = tqdm(xml)
        for i in xml_tqdm:
            filename = i.split('\\')[-1][:-4]
            xml_tqdm.set_description(f'Processing {filename}')

            # fitting 실행
            process.fitting(i, a, b)
            if int(xml.index(i)) + 1 == len(xml):
                print("모든 파일이 완료되었습니다. 수고하셨습니다.")

            # csv 실행
            process.csv_mod(i, c)

        print("실행 시간 :" + str(round(time.time() - start, 1)) + "초")


    CheckVar1=IntVar()
    CheckVar2=IntVar()
    CheckVar3=IntVar()

    c1=Checkbutton(window,text="save figure",variable=CheckVar1, command=status1_print)
    c2=Checkbutton(window,text="show figure",variable=CheckVar2, command=status2_print)
    c3=Checkbutton(window,text="save csv",variable=CheckVar3, command=status3_print)

    c1.pack()
    c2.pack()
    c3.pack()

    save_btn = tkinter.Label(window, text="save",bg='grey19', fg = 'snow')
    save_btn.bind('<Button-1>', save_status)
    save_btn.place(x=110,y=100)
    window.geometry('250x250+220+200')
    window.mainloop()
