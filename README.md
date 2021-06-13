![header](https://capsule-render.vercel.app/api?type=wave&color=auto&height=200&section=header&text=SBBFU%20PROJECT&fontSize=50)

###### PE02_A02

# 👍 SBBFU Project :+1:
##### Hi :wave:
##### Thank you for looking for us. The project is called SBBFU, which means "Special Black Box For U."
##### Analyze customer-provided data and provide results.
---
### 1. Introduction
##### - PE2 : SBBFU Project
##### - contributors : 

>- Jeon su in :girl: : qqy78@hanmail.net
>- Park seoung min :boy: : psm401@hanyang.ac.kr
>>- Bae ju han :boy: : noreply@github.com


> - We aim to develop Python-based data analysis software \
> The goal is to develop software that can analyze wafer scale data in detail.
### 2. Objective of project
  ##### 1) Detailed project 
> ##### The main task is to receive data from the customer and then receive the request.
> Main request 
> + Lot
> + Wafer
> + Die row & colum
> 
> We can analyze the selected data by specifying specific elements
> In order to develop such analysis software, a black box(software) that implements this function is created to solve the customer's request.
>
> Please put the data in the 'dat' folder specify the file path Run the Run.py 

  ##### 2) Run file description
> First, extract only the file named 'LMZ' from the file that the customer gave us. 
> 
> Then, after analyzing the raw data given by the customer using various modules, make a csv file.

### 3. Project information

#####
>* Getting Stared
>   + Entered the Terminal, write down 'pip install -r requirements.txt' and download it. \
>``(base) C:\Download\PE02_A02_SBBFU-1>pip install -r requirements.txt``
>
>* How to Run
>   + Choose the raw data folder customer want to analyze.
>   + Choose to automatically start data analysis.
>   
>	 + After select the data you want to analyze, select various options such as wafer, die option, figure shape (show figure, save figure, save csv) and press run button.
<img src = "https://user-images.githubusercontent.com/84078034/121799780-f55b5280-cc68-11eb-859f-a0cf73b37ee1.png" width="350" height="300">


### 4. Description of the module file feature

##### 1) Fitting module
  >-   The graph is drawn by parsing the raw data of Wavelengthsweep, IL, Current, and Voltage in the xml file.
  >-   The fitting of parsing a raw data and displays the data value y-axis corresponding to x-axis by the customer and the desired R-squared, etc. and stored in the graph to visualize the image.
 <img src ="https://user-images.githubusercontent.com/84078034/121302547-d2613380-c934-11eb-8ef4-6b330f316406.png" width="600" height="350">

##### 2) CSV module
  >- The following photo is a csv file that analyzes the data provided by the customer.
  >- It contains a variety of data information, including Lot, Wafer, and Operator etc.
  >- Create a dataframe so that the meausured information in the xml file can be viewed at a glance.
  >- Save this data frome in csv format in the 'Result' folder.
  >- If 'r-squared' is less than 0.95, an ‘Errorflag’ appears in the csv file.

 <img src = "https://user-images.githubusercontent.com/80964488/117802539-903ec680-b290-11eb-969f-6fd459a8d594.PNG" width= "600" height="350">
 
### 5. :warning:precautions:warning:

 1) You must select all the options in the 'Checkbox'. If you don't, you'll make a error.
 2) When fitting sometimes doesn't work, it keeps running until fitting is done well.
 3) If you choose the All option when Wafer is selected, you must not choose any other option.
 
### 6. Conclusion
  >- After passing the law data provided by the customer, they use the ‘fitting module’ to fit.
  >- Save this fitting figure in the ‘result’ folder.
  >- Save the csv file to the 'result' folder based on the data provided by the customer.
