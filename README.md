<h6>PE02_A02<h6>
<h1> SBBFU Project <h1>
 
#####
> We aim to develop Python-based data analysis software \
> The goal is to develop software that can analyze wafer scale data in detail.
>
> Main request 
> + Lot
> + Wafer
> + Die row & colum
> 
> We can analyze the selected data by specifying specific elements
>
> Finally, the final report The final goal is to make documentation about the tasks 
> we did using a jupyter notebook and report it to the customer.
>
> Please put the data in the 'Data' folder specify the file path Run the Run.py 

 
***

<h2> Project information <h2>

#####
>* Getting Stared
>   + Entered the Terminal, write down 'pip install -r requirements.txt' and download it. \
>``(base) C:\Download\PE02_A02_SBBFU-1>pip install -r requirements.txt``
>
>
>* How to Run
>   + Please enter the file_location and parameter of save_figure, show_figure, save_csv. \
``file_path = '.\dat\P184640\**\*LMZ?.xml'``\
The customer can choose the option (save figure, show figure, save csv).
 
 ![image](https://user-images.githubusercontent.com/84078034/121302349-87472080-c934-11eb-8532-9d4e715bd922.png)
***



<h2> Description of the module file feature <h2>

 <h3> 1. Fitting module <h3>
 
#####
  >-   The graph is drawn by parsing the raw data of Wavelengthsweep, IL, Current, and Voltage in the xml file.
  >-   The fitting of parsing a raw data and displays the data value y-axis corresponding to x-axis by the customer and the desired R-squared, etc. and stored in the graph to visualize the image.
 ![image](https://user-images.githubusercontent.com/84078034/121302547-d2613380-c934-11eb-8ef4-6b330f316406.png)


 <h3> 2. CSV module <h3>
 
#####
  >- The following photo is a csv file that analyzes the data provided by the customer.
  >- It contains a variety of data information, including Lot, Wafer, and Operator etc.
  >- Create a dataframe so that the meausured information in the xml file can be viewed at a glance.
  >- Save this data frome in csv format in the 'Result' folder.
  >- If 'r-squared' is less than 0.95, an ‘Errorflag’ appears in the csv file.
 
 
 ![캡처](https://user-images.githubusercontent.com/80964488/117802539-903ec680-b290-11eb-969f-6fd459a8d594.PNG)
  
<h4>  <h4>
  #####
   >- After passing the law data provided by the customer, they use the ‘fitting module’ to fit.
   >- Save this fitting figure in the ‘result’ folder.
   >- Save the csv file to the 'result' folder based on the data provided by the customer.
