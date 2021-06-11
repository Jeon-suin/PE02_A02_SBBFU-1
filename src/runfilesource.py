from tkinter import *
import tkinter.ttk as ttk
import tkinter.font
import time
import glob
import shutil

from tqdm import tqdm
from src import process , IVfitting, Measured_Spectra , Processed_spectra , Ref_fitting ,tocsv

try:
    shutil.rmtree('.\\res\\csv')
except FileNotFoundError:
    pass

def checkbox(file_path):
    window = Tk()
    window.title("check box test")

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

    def getcombo2():
        return combo1.get()

    def save_status(file_path = file_path):
        a = status1_print()
        b = status2_print()
        c = status3_print()
        d = status4_print()
        e = status5_print()
        f = status6_print()
        g = status7_print()

        if a + b + c == 0:
            print('옵션을 다시 선택하여 주세요. 프로그램을 종료합니다.')
        else:
            start = time.time()
            if d == 1 and e == 0 and f == 0 and g == 0:
                file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
            elif e == 1 and d == 0 and f == 0 and g == 0:
                file_path = '.\dat\P184640\D08\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
            elif f == 1 and d == 0 and e == 0 and g == 0:
                file_path = '.\dat\P184640\D23\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
            elif g == 1 and f == 0 and d == 0 and e == 0:
                file_path = '.\dat\P184640\D24\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
            elif d == 1 and e == 1 and f == 0 and g == 0:
                file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D08\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
            elif f == 1 and d == 1 and e == 0 and g == 0:
                file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D23\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
            elif g == 1 and d == 1 and e == 0 and f == 0:
                file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D024\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
            elif e == 1 and f == 1 and d == 0 and g == 0:
                file_path = '.\dat\P184640\D08\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D23\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
            elif e == 1 and g == 1 and d == 0 and f == 0:
                file_path = '.\dat\P184640\D08\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D23\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
            elif f == 1 and g == 1 and d == 0 and g == 0:
                file_path = '.\dat\P184640\D24\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D23\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
            elif d == 1 and e == 1 and f == 1 and g == 0:
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
            elif e == 1 and d == 1 and g == 1 and f == 0:
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
            elif d == 1 and g == 1 and f == 1 and e == 0:
                file_path = '.\dat\P184640\D07\**\*LMZ?.xml'
                xml = []
                for filename in glob.glob(file_path, recursive=True):
                    xml.append(filename)
                file_path1 = '.\dat\P184640\D04\**\*LMZ?.xml'
                for filename in glob.glob(file_path1, recursive=True):
                    xml.append(filename)
                file_path2 = '.\dat\P184640\D23\**\*LMZ?.xml'
                for filename in glob.glob(file_path2, recursive=True):
                    xml.append(filename)
            elif e == 1 and g == 1 and f == 1 and d == 0:
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

            xml_tqdm = tqdm(xml)
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

    c4 = Checkbutton(frame, text="D07", variable=CheckVar4, command=status4_print)
    c5 = Checkbutton(frame, text="D08", variable=CheckVar5, command=status5_print)
    c6 = Checkbutton(frame, text="D23", variable=CheckVar6, command=status6_print)
    c7 = Checkbutton(frame, text="D24", variable=CheckVar7, command=status7_print)

    label = tkinter.Label(frame, text="Wafer", width=4, height=3, fg="black", )
    label.pack()

    list1 = ['Transmission spectra','IV raw dat','Processed and fitting','Spectra except ref','All figure']
    combo1 = ttk.Combobox(frame, values=list1)
    combo1.set("Pick figure dat")

    c4.pack()
    c5.pack()
    c6.pack()
    c7.pack()

    combo1.pack(pady=10)

    save_btn = Button(frame, text="run",command =lambda :[getcombo2(),save_status()])
    save_btn.pack(side="bottom",fill="both")

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
