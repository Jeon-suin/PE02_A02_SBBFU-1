from src import process , IVfitting, Measured_Spectra , Processed_spectra , Ref_fitting ,tocsv
import glob, time
from tqdm import tqdm

file_path = '.\dat\P184640\D24\**\*LMZ?.xml'
save_figure = 'F'
show_figure = 'T'
save_csv = 'F'

xml=[]
for filename in glob.glob(file_path, recursive= True):
    xml.append(filename)

start = time.time()

xml_tqdm = tqdm(xml)
for i in xml_tqdm:
    filename = i.split('\\')[-1][:-4]
    xml_tqdm.set_description(f'Processing {filename}')

    # fitting 실행
    process.fitting(i,save_figure,show_figure)
    if int(xml.index(i)) + 1 == len(xml):
        print("모든 파일이 완료되었습니다. 수고하셨습니다.")

    #csv 실행
    process.csv_mod(i,save_csv)

print("실행 시간 :" + str(round(time.time()-start,1))+"초")