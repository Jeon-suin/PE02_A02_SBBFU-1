<h6>PE02_A02<h6>
<h1> SBBFU Project <h1>
 
***
  
<h2>About the project <h2>
 
#####
> We aim to develop Python-based data analysis software
> The goal is to develop software that can analyze wafer scale data in detail.
>
> At first,
>
> The main task is to receive data from the customer and then receive the request.
> 
> Main request 
> + Lot
> + Wafer
> + Die row & colum
> 
> We can analyze the selected data by specifying specific elements    
> In order to develop such analysis software, 
> a black box(software) that implments this function is created to solve the customer's request.
>
> In the software,
> We process the raw data and print it out. 
> We show the processed data as a 2*3 figure and save the file. 
> 
> In addition, it creates an Excel csv file that can analyze varous 
> xml files as a result file and makes a dataframe that can be compared simply.
>
> Finally, the final report The final goal is to make documentation about the tasks 
> we did using a jupyter notebook and report it to the customer.
>
> Please put the data in the 'Data' folder
> specify the file path
> Run the Run.py 


***

<h2> Run file description <h2>
 
 >Create a folder corresponding to the output that can be delivered to customers by copying the data in the **'Data'** folder to **'Result'**
 >Data is processed by selecting only files with the filename "LMZ"
 >Load the module that processes and fits raw data and the module that makes the data parsed from xml file into a csv file, respectively.


<h2> Description of the module file feature <h2>
 
 <h3> Fitting module <h3>
  - The graph is drawn by parsing the raw data of Wavelenthsweep, IL, Current, and Voltage in the xml file.
  - The fitting of parsing a raw data and displays the data value y-axis corresponding to x-axis by the customer and the desired R-squared, etc. and stored in the graph to visualize the image.
 
 <h3> csv module <h3>
 
  - Create a dataframe so that the meausured information in the xml file can be viewed at a glance.
  - Save this data frome in csv format in the 'Result' folder.
 
