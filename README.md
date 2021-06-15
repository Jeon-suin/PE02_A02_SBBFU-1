![header](https://capsule-render.vercel.app/api?type=wave&color=auto&height=200&section=header&text=SBBFU%20PROJECT&fontSize=50)

###### PE02_A02
### Contents

[1. Introduction](#1-introduction)\
[2. Objective of project](#2-objective-of-project)\
[3. Project information](#3-project-information)\
[4. Description of the module file feature](#4-description-of-the-module-file-feature)\
[5. Conclusion](#5-conclusion)

# 👍 SBBFU Project :
##### Hi :wave:
##### Thank you for looking for us. The project is called SBBFU, which means "Special Black Box For U."
##### Analyze customer-provided data and provide results.
---
## 1. Introduction
#### - PE2 : SBBFU Project
We aim to develop Python-based data analysis software. 
The goal is to develop software that can analyze wafer scale data in detail.
#### - contributors : 
|name|E-mail|:smile:|
|:---:|:---:|:---:|
|Jeon su in:girl:|qqy78@hanmail.net|<img src = "https://user-images.githubusercontent.com/84078034/121825406-2aa98400-cced-11eb-82d7-3fbbb3cdff28.png" width = "100" height = "100">|
|Park seoung min:boy:|psm401@hanyang.ac.kr|<img src = "https://user-images.githubusercontent.com/84078034/121825519-e074d280-cced-11eb-8507-995dd571eaf4.png" width = "100" height = "100">|
|Bae joo han :boy:|joohan0115@hanyang.ac.kr|<img src = "https://user-images.githubusercontent.com/84078034/121825720-e7501500-ccee-11eb-9093-d83795514a94.png" width = "100" height = "100">|
---
## 2. Objective of project
 #### Detailed project 
 The main task is to receive data from the customer and then receive the request.
 Main request 
 + Wafer
 + Die row & colum
 + option
 
 We can analyze the selected data by specifying specific elements
In order to develop such analysis software, a black box(software) that implements this function is created to solve the customer's request.

 #### Run file description
First, extract only the file named 'LMZ' from the file that the customer gave us. 

Then, after analyzing the raw data given by the customer using various modules, make a csv file.
---
## 3. Project information

####
* Getting Stared
   + Entered the Terminal, write down 'pip install -r requirements.txt' and download it. \
``(base) C:\Download\PE02_A02_SBBFU-1>pip install -r requirements.txt``

* How to Run
  + Choose the raw data folder customer want to analyze.
   
	+ After select the data you want to analyze, select various options such as wafer, die option, figure shape (show figure, save figure, save csv) and press run button.

---
## 4. Description of the module file feature

#### Fitting module
 -   The graph is drawn by parsing the raw data of Wavelengthsweep, IL, Current, and Voltage in the xml file.
 -   The fitting of parsing a raw data and displays the data value y-axis corresponding to x-axis by the customer and the desired R-squared, etc. and stored in the graph to visualize the image.

#### CSV module
 - It contains a variety of data information, including Lot, Wafer, and Operator etc.
 - Create a dataframe so that the meausured information in the xml file can be viewed at a glance.
 - Save this data frome in csv format in the 'Result' folder.
 ---
## 5. Conclusion
 - After passing the law data provided by the customer, they use the ‘fitting module’ to fit.
 - Save this fitting figure in the ‘result’ folder.
 - Save the csv file to the 'result' folder based on the data provided by the customer.
---
## :warning:precautions:warning:

 1) You must select all the options in the 'Checkbox'. If you don't, you'll make a error.
 2) When fitting sometimes doesn't work, it keeps running until fitting is done well.
 3) If you choose the All option when Wafer is selected, you must not choose any other option.
 
