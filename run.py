from src import process , IVfitting, Measured_Spectra , Processed_spectra , Ref_fitting ,tocsv
import glob , time
from tqdm import tqdm

xml=[]
for filename in glob.glob('.\dat\P184640\**\*LMZ?.xml', recursive= True):
    xml.append(filename)

start = time.time()
xml1 = tqdm(xml)

for i in xml1:
    filename = i.split('\\')[-1][:-4]
    xml1.set_description(f'Processing {filename}')
    # fitting 실행
    process.fitting(i,'T','F') #빈칸에 save figure 및 show figure를 True or False 로 입력하세요.

    if int(xml.index(i)) + 1 == len(xml):
        print("모든 파일이 완료되었습니다 빠이루")
        break

    #csv 실행
    process.csv_mod(i,'T') # 빈칸에 csv 파일로 저장하고 싶으면 True or False를 입력하세요.

print("실행 시간 :" + str(round(time.time()-start,1))+"초")