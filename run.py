from src import process
from src import IVfitting
from src import Measured_Spectra
from src import Processed_spectra
from src import Ref_fitting
from src import tocsv
import glob
import time
import matplotlib.pyplot as plt

xml=[]
for filename in glob.glob('.\Data\P184640\**\*LMZ?.xml', recursive= True):
    xml.append(filename)

custom_W = str(input('figure를 보시기를 원하십니까?(T/F) :'))
custom_a = str(input('figure를 저장하기를 원하십니까?(T/F) :'))
start = time.time()

for i in xml:
    # fitting 실행
    process.fitting(i)
    filename = i.split('\\')[-1][:-4]
    print(filename + "이 완료되었습니다." + "(" + str(int(xml.index(i)) + 1) + "/" + str(len(xml)) + ")")
    if int(xml.index(i)) + 1 == len(xml):
        print("모든 파일이 완료되었습니다 빠이루")
        break




    # save figure 옵션
    if custom_a == 'T':
        if 'D07' in filename:
            plt.savefig('.\\res\\D07\\' + filename + '.png', bbox_inches='tight')
        elif 'D08' in filename:
            plt.savefig('.\\res\\D08\\' + filename + '.png', bbox_inches='tight')
        elif 'D23' in filename:
            plt.savefig('.\\res\\D23\\' + filename + '.png', bbox_inches='tight')
        else:
            plt.savefig('.\\res\\D24\\' + filename + '.png', bbox_inches='tight')


    # show figure 옵션
    if custom_W == 'T':
        plt.show()
    else:
        plt.show(block=False)



    #csv 실행
    process.csv_mod(i)

print("실행 시간 :" + str(round(time.time()-start,1))+"초")