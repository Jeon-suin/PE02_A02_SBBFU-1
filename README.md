<h6>PE02_A02<h6>
<h1> 안녕하세요 당신의 Black Box를 책임지는 A02입니다! <h1> 
  

We aim to develop Python-based data analysis software
The goal is to develop software that can analyze wafer scale data in detail.

At first,

The main task is to receive data from the customer and then receive the request.
Main request -Lot
             -Wafer
             -Die row & colum
We can analyze the selected data by specifying specific elements    
In order to develop such analysis software, a black box(software) that implments this function is created to solve the customer's request.

In the software,
We process the raw data and print it out. We show the processed data as a 2*3 figure and save the file. In addition, it creates an Excel csv file that can analyze varous xml files as a result file and makes a dataframe that can be compared simply.

Finally, the final report The final goal is to make documentation about the tasks we did using a jupyter notebook and report it to the customer.

Please put the data in the 'Data' folder
specify the file path
Run the Run.py



plt사진, csv 캡쳐사진
Python-based data analysis software 개발이 목표 
세부적으로 Wafer Scale의 데이터를 분석할 수 있는 소프트웨어 개발하는 것이 목표 

주요 과제로 우선 Customer에게 data를 받은 후 요청사항에 대해 전달받는다. 

주요 요청사항으로는  

-Lot 

-Wafer 

-Die row & column과 같이 특정 데이터만을 지정해서 선택한 데이터를 분석한다.  

이러한 분석하는 software를 개발하기 위해서 이 기능을 구현하는 black box를 만들어 customer의 요청사항을 해결해 주는 것이다. 

 

Blackbox의 목표로는 Input data를 가공하여 Output로 출력하여서 보여준다. 이를 2*3 figure로 보여준 후 파일을 저장한다. 또한, result file로  다양한 xml file들을 분석할 수 있는 엑셀 csv 파일을 만들어 간단하게 비교 할 수 있는 dataframe을 만들어 준다. 마지막으로 최종 report 우리가 했던 과제들에 대해서 documentation를  jupyter notebook을 이용해서 만들어서 customer에게 보고해주는 것이 최종 목표이다. 
