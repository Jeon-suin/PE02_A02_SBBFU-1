<h6>PE02_A02<h6>
<h1> SBBFU Project <h1>
 
 
<h2> Description <h2>

#####
>간단한 설명 블라블라
>
>
<h2> Installation <h2>
 
 
#####
 > Entered the Terminal, write down 'pip install -r requirements.txt' and download it. \
\
>``(base) C:\Download\PE02_A02_SBBFU-1>pip install -r requirements.txt``


***

<h2> How to Run  <h2>
 
 
#####
 > Enter True or False in the fitting in the run.py file to determine whether to show figure or save figure.
 Save csv files with True or False input.

>\
``file_path = '.\dat\P184640\**\*LMZ?.xml'``\
``save_figure = 'T' `` \
``show_figure = 'T' `` \
``save_csv = 'T'``
***



<h2> Description of the module file feature <h2>

 <h3> 1. Fitting module <h3>
 
#####
  >-   The graph is drawn by parsing the raw data of Wavelengthsweep, IL, Current, and Voltage in the xml file.
  >-   The fitting of parsing a raw data and displays the data value y-axis corresponding to x-axis by the customer and the desired R-squared, etc. and stored in the graph to visualize the image.
 
![P184640_D08_(0,2)_GORILLA5_DCM_LMZC xml](https://user-images.githubusercontent.com/80964488/117802229-3211e380-b290-11eb-81dc-c5e460009392.png)


 <h3> 2. CSV module <h3>
 
#####
  >- Create a dataframe so that the meausured information in the xml file can be viewed at a glance.
  >- Save this data frome in csv format in the 'Result' folder.
 
 
 ![캡처](https://user-images.githubusercontent.com/80964488/117802539-903ec680-b290-11eb-969f-6fd459a8d594.PNG)
