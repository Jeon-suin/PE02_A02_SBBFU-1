from src import process , IVfitting, Measured_Spectra , Processed_spectra , Ref_fitting ,tocsv
import glob , time

xml=[]
for filename in glob.glob('.\dat\P184640\**\*LMZ?.xml', recursive= True):
    xml.append(filename)

start = time.time()

for i in xml:
    # fitting 실행
    process.fitting(i,True,True) #빈칸에 save figure 및 show figure를 True or False 로 입력하세요.
    filename = i.split('\\')[-1][:-4]
    print(filename + "이 완료되었습니다." + "(" + str(int(xml.index(i)) + 1) + "/" + str(len(xml)) + ")")
    if int(xml.index(i)) + 1 == len(xml):
        print("모든 파일이 완료되었습니다 빠이루")
        break

    #csv 실행
    process.csv_mod(i)

print("실행 시간 :" + str(round(time.time()-start,1))+"초")