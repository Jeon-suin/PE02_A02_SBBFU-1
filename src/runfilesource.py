from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk
import tkinter.font
import time
import glob
import os
import webbrowser
import shutil
from tqdm import tqdm
from src import process , IVfitting, Measured_Spectra , Processed_spectra , Ref_fitting ,tocsv
from src import Date
try:
    shutil.rmtree('.\\res\\csv')
except:
    FileNotFoundError
    pass

def checkbox(file_path):
    window = Tk()
    window.title("Run to data")

    def status1_print():
        return (CheckVar1.get())

    def status2_print():
        return (CheckVar2.get())

    def status3_print():
        return (CheckVar3.get())

    def status4_print():
        return (CheckVar4.get())

    def status5_print():
        return (CheckVar5.get())

    def status6_print():
        return (CheckVar6.get())

    def status7_print():
        return (CheckVar7.get())

    def status8_print():
        return (CheckVar8.get())

    def getcombo2():
        return combo1.get()

    def getcombo3():
        return combo2.get()

    def clicked():
        messagebox.showinfo('help', 'psm401@hanyang.ac.kr')
    def clicked1():
        messagebox.showwarning('Error', '옵션을 다시 선택하여 주세요.')
    def clicked2():
        messagebox.showwarning('Error', 'figure type를 선택하여 주세요')
    def clicked3():
        messagebox.showwarning('Error', 'row and column을 선택하여 주세요')

    def check_status(file_path = file_path):
        d = status4_print()
        e = status5_print()
        f = status6_print()
        g = status7_print()
        h = status8_print()

        if d == 1 and e == 0 and f == 0 and g == 0 and h == 0:
            file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
            xml = []
            for filename in glob.glob(file_path, recursive=True):
                xml.append(filename)
        elif e == 1 and d == 0 and f == 0 and g == 0 and h == 0:
            file_path = '.\dat\P184640\D08\**\*LMZ?.xml'
            xml = []
            for filename in glob.glob(file_path, recursive=True):
                xml.append(filename)
        elif f == 1 and d == 0 and e == 0 and g == 0 and h == 0:
            file_path = '.\dat\P184640\D23\**\*LMZ?.xml'
            xml = []
            for filename in glob.glob(file_path, recursive=True):
                xml.append(filename)
        elif g == 1 and f == 0 and d == 0 and e == 0 and h == 0:
            file_path = '.\dat\P184640\D24\**\*LMZ?.xml'
            xml = []
            for filename in glob.glob(file_path, recursive=True):
                xml.append(filename)

        elif d == 1 and e == 1 and f == 0 and g == 0 and h == 0:
            file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
            xml = []
            for filename in glob.glob(file_path, recursive=True):
                xml.append(filename)
            file_path1 = '.\dat\P184640\D08\**\*LMZ?.xml'
            for filename in glob.glob(file_path1, recursive=True):
                xml.append(filename)
        elif d == 1 and e == 0 and f == 1 and g == 0 and h == 0:
            file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
            xml = []
            for filename in glob.glob(file_path, recursive=True):
                xml.append(filename)
            file_path1 = '.\dat\P184640\D23\**\*LMZ?.xml'
            for filename in glob.glob(file_path1, recursive=True):
                xml.append(filename)
        elif d == 1 and e == 0 and f == 0 and g == 1 and h == 0:
            file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
            xml = []
            for filename in glob.glob(file_path, recursive=True):
                xml.append(filename)
            file_path1 = '.\dat\P184640\D24\**\*LMZ?.xml'
            for filename in glob.glob(file_path1, recursive=True):
                xml.append(filename)
        elif d == 0 and e == 1 and f == 1 and g == 0 and h == 0:
            file_path = '.\dat\P184640\D08\**\*LMZ?.xml'
            xml = []
            for filename in glob.glob(file_path, recursive=True):
                xml.append(filename)
            file_path1 = '.\dat\P184640\D23\**\*LMZ?.xml'
            for filename in glob.glob(file_path1, recursive=True):
                xml.append(filename)
        elif d == 0 and e == 1 and f == 0 and g == 1 and h == 0:
            file_path = '.\dat\P184640\D08\**\*LMZ?.xml'
            xml = []
            for filename in glob.glob(file_path, recursive=True):
                xml.append(filename)
            file_path1 = '.\dat\P184640\D24\**\*LMZ?.xml'
            for filename in glob.glob(file_path1, recursive=True):
                xml.append(filename)
        elif d == 0 and e == 0 and f == 1 and g == 1 and h == 0:
            file_path = '.\dat\P184640\D24\**\*LMZ?.xml'
            xml = []
            for filename in glob.glob(file_path, recursive=True):
                xml.append(filename)
            file_path1 = '.\dat\P184640\D23\**\*LMZ?.xml'
            for filename in glob.glob(file_path1, recursive=True):
                xml.append(filename)

        elif d == 1 and e == 1 and f == 1 and g == 0 and h == 0:
            file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
            xml = []
            for filename in glob.glob(file_path, recursive=True):
                xml.append(filename)
            file_path1 = '.\dat\P184640\D08\**\*LMZ?.xml'
            for filename in glob.glob(file_path1, recursive=True):
                xml.append(filename)
            file_path1 = '.\dat\P184640\D23\**\*LMZ?.xml'
            for filename in glob.glob(file_path1, recursive=True):
                xml.append(filename)
        elif d == 1 and e == 1 and f == 0 and g == 1 and h == 0:
            file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
            xml = []
            for filename in glob.glob(file_path, recursive=True):
                xml.append(filename)
            file_path1 = '.\dat\P184640\D08\**\*LMZ?.xml'
            for filename in glob.glob(file_path1, recursive=True):
                xml.append(filename)
            file_path2 = '.\dat\P184640\D24\**\*LMZ?.xml'
            for filename in glob.glob(file_path2, recursive=True):
                xml.append(filename)
        elif d == 1 and e == 0 and f == 1 and g == 1 and h == 0:
            file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
            xml = []
            for filename in glob.glob(file_path, recursive=True):
                xml.append(filename)
            file_path1 = '.\dat\P184640\D24\**\*LMZ?.xml'
            for filename in glob.glob(file_path1, recursive=True):
                xml.append(filename)
            file_path2 = '.\dat\P184640\D23\**\*LMZ?.xml'
            for filename in glob.glob(file_path2, recursive=True):
                xml.append(filename)
        elif d == 0 and e == 1 and f == 1 and g == 1 and h == 0:
            file_path = '.\dat\P184640\D08\**\*LMZ?.xml'
            xml = []
            for filename in glob.glob(file_path, recursive=True):
                xml.append(filename)
            file_path1 = '.\dat\P184640\D23\**\*LMZ?.xml'
            for filename in glob.glob(file_path1, recursive=True):
                xml.append(filename)
            file_path2 = '.\dat\P184640\D24\**\*LMZ?.xml'
            for filename in glob.glob(file_path2, recursive=True):
                xml.append(filename)
        else:
            xml = []
            for filename in glob.glob(file_path, recursive=True):
                xml.append(filename)

        if combo2.get() == 'row & column':
            clicked3()
        else:
            xml1 = []
            for i in xml:
                if combo2.get() in i:
                    xml1.append(i)
                elif combo2.get() == 'ALL':
                    xml1 = xml

            for i in xml1:
                Date.Date(i)




    def save_status(file_path = file_path):
        a = status1_print()
        b = status2_print()
        c = status3_print()
        d = status4_print()
        e = status5_print()
        f = status6_print()
        g = status7_print()
        h = status8_print()

        if a + b + c == 0 or d + e + f + g + h == 0:
            clicked1()
        else:
            start = time.time()
            if d == 1 and e == 0 and f == 0 and g == 0 and h == 0:
                file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
            elif e == 1 and d == 0 and f == 0 and g == 0 and h == 0:
                file_path = '.\dat\P184640\D08\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
            elif f == 1 and d == 0 and e == 0 and g == 0 and h == 0:
                file_path = '.\dat\P184640\D23\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
            elif g == 1 and f == 0 and d == 0 and e == 0 and h == 0:
                file_path = '.\dat\P184640\D24\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)

            elif d == 1 and e == 1 and f == 0 and g == 0 and h == 0:
                file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D08\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
            elif d == 1 and e == 0 and f == 1 and g == 0 and h == 0:
                file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D23\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
            elif d == 1 and e == 0 and f == 0 and g == 1 and h == 0:
                file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D24\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
            elif d == 0 and e == 1 and f == 1 and g == 0 and h == 0:
                file_path = '.\dat\P184640\D08\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D23\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
            elif d == 0 and e == 1 and f == 0 and g == 1 and h == 0:
                file_path = '.\dat\P184640\D08\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D24\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
            elif d == 0 and e == 0 and f == 1 and g == 1 and h == 0:
                file_path = '.\dat\P184640\D24\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D23\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)

            elif d == 1 and e == 1 and f == 1 and g == 0 and h == 0:
                file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D08\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D23\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
            elif d == 1 and e == 1 and f == 0 and g == 1 and h == 0:
                file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D08\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
                file_path2 = '.\dat\P184640\D24\**\*LMZ?.xml'
                for filename in glob.glob(file_path2, recursive=True):
                    xml.append(filename)
            elif d == 1 and e == 0 and f == 1 and g == 1 and h == 0:
                file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D24\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
                file_path2 = '.\dat\P184640\D23\**\*LMZ?.xml'
                for filename in glob.glob(file_path2, recursive=True):
                    xml.append(filename)
            elif d == 0 and e == 1 and f == 1 and g == 1 and h == 0:
                file_path = '.\dat\P184640\D08\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D23\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
                file_path2 = '.\dat\P184640\D24\**\*LMZ?.xml'
                for filename in glob.glob(file_path2, recursive=True):
                    xml.append(filename)
            else:
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)

            if combo2.get() == 'row & column':
                clicked3()
            else:
                xml1 =[]
                for i in xml:
                    if combo2.get() in i:
                        xml1.append(i)
                    elif combo2.get() == 'ALL':
                        xml1 = xml



                if combo1.get() == 'Pick figure dat':
                    clicked2()
                else:
                    for i in xml1:
                        xml_tqdm = tqdm(xml1)
                    for i in xml_tqdm:
                        filename = i.split('\\')[-1][:-4]
                        xml_tqdm.set_description(f'Processing {filename}')

                        # fitting 실행
                        if combo1.get() == 'All figure':
                            process.fitting(i, a, b)
                        elif combo1.get() == 'Transmission spectra':
                            Measured_Spectra.Measured(i, a, b)
                        elif combo1.get() == 'IV raw dat':
                            IVfitting.IVfitting(i, a, b)
                        elif combo1.get() == 'Processed and fitting':
                            Ref_fitting.Ref_fitting(i, a, b)
                        else:
                            Processed_spectra.Pro_spe(i, a, b)

                    # csv 실행
                    process.csv_mod(i, c)

                    if int(xml.index(i)) + 1 == len(xml):
                        print("모든 파일이 완료되었습니다. 수고하셨습니다.")

                    print("실행 시간 :" + str(round(time.time() - start, 1)) + "초")



    frame = Frame(window)
    frame.pack()

    CheckVar4 = IntVar()
    CheckVar5 = IntVar()
    CheckVar6 = IntVar()
    CheckVar7 = IntVar()
    CheckVar8 = IntVar()

    c4 = Checkbutton(frame, text="D07", variable=CheckVar4, command=status4_print)
    c5 = Checkbutton(frame, text="D08", variable=CheckVar5, command=status5_print)
    c6 = Checkbutton(frame, text="D23", variable=CheckVar6, command=status6_print)
    c7 = Checkbutton(frame, text="D24", variable=CheckVar7, command=status7_print)
    c8 = Checkbutton(frame, text="ALL", variable=CheckVar8, command=status8_print)

    label = tkinter.Label(frame, text="Wafer", width=4, height=3, fg="black", )
    label.pack()

    label2 = tkinter.Label(window, text="made by A02", fg="black", )
    label2.pack()
    label2.place(x=420,y=380)

    list1 = ['Transmission spectra','IV raw dat','Processed and fitting','Spectra except ref','All figure']
    combo1 = ttk.Combobox(frame, values=list1)
    combo1.set("Pick figure dat")

    list2 = ['ALL','(-1,-1)','(-1,-3)','(-1,3)','(-3,-3)','(-3,0)','(-3,2)','(-4,-1)','(0,-4)','(0,0)','(0,2)',
             '(2,-1)','(2,-3)','(2,2)','(3,0)']
    combo2 = ttk.Combobox(frame, values=list2)
    combo2.set("row & column")

    c4.pack()
    c5.pack()
    c6.pack()
    c7.pack()
    c8.pack()

    combo2.pack(pady=10)
    combo1.pack(pady=10)


    def btn():
        os.startfile('res')
    def btn2():
        code = "jupyter notebook"
        os.system(code)
    def btn3():
        os.startfile('dat')

    def callback(url):
        webbrowser.open_new(url)

    link1 = Label(window, text="Github", fg="blue", cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://github.com/SBBFU/PE02_A02_SBBFU"))
    link1.place(x=10,y=10)

    # link2 = Label(frame, text="Ecosia Hyperlink", fg="blue", cursor="hand2")
    # link2.pack()
    # link2.bind("<Button-1>", lambda e: callback("http://www.ecosia.org"))

    doc_btn = Button(window,width=15 ,text="Final Report", command=btn2)
    doc_btn.pack()
    doc_btn.place(x=10, y= 290)

    res_btn = Button(window, width=15,text="res folder", command=btn)
    res_btn.pack()
    res_btn.place(x=10,y=260)

    dat_btn = Button(window, width=15, text="dat folder", command=btn3)
    dat_btn.pack()
    dat_btn.place(x=10, y=230)

    btn = Button(window, text='help', command=clicked)
    btn.place(x=450, y=10)

    save_btn = Button(frame, text="run",command =lambda :[getcombo2(),getcombo3(),save_status(),])
    save_btn.pack(side="bottom",fill="both")

    check_btn = Button(frame, text="Check", command=lambda: [getcombo3(),check_status()])
    check_btn.pack(side="bottom", fill="both")

    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()

    c1 = Checkbutton(frame, text="save figure", variable=CheckVar1, command=status1_print)
    c2 = Checkbutton(frame, text="show figure", variable=CheckVar2, command=status2_print)
    c3 = Checkbutton(frame, text="save csv ", variable=CheckVar3, command=status3_print)

    c1.pack()
    c2.pack()
    c3.pack()

    window.geometry('500x400+220+200')
    window.mainloop()
