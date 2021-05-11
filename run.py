import process
import glob
#Move Folder from "Data" to "Result"
from distutils.dir_util import  copy_tree
copy_tree("./Data", "./Result")

xml=[]
for filename in glob.glob('./Result/P184640/**/*LMZ*.xml', recursive= True):
    xml.append(filename)

for i in xml:
    process.fitting(i)
    process.csv_mod(i)
