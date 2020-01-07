# Crowd-Detection-And-Analyzation
A Python Program to detect the maximum numbers of people present in the frame and show visualised analyse of the data.
CrowdDetection.py First the program uses opencv to detect the avgerage number of people present in the frame for a minute. It uses a specially trained algorithm known as the cascade of a program and this cascade uses diffrent Objects.caffemodel Objects.prototxt.txt training model to learn and try to detect many objets and people. Since we just need our program to detect only the number of people in the given frame we enable only the people model to detect people. With the help of the ids of each detection, the program counts the number of people in the frame for one minute. This data is converted to an average of one minute. The time library is used to keep a track of time. Both the average and current time data is used for processing the further project.The average value per minute along with the is being stroed as a csv file. This file is later used to plot the graphs

plot.py HeatMap.py

Using this data a normal realtime plot-line graph is used along with a custom heat map which uses only one input at a time.

P.S. if you are using the heat map please close the map to see the change for the second value in the csv file and if the data is not being written in the csv file then try deleting the csv file and run the program again.Run the program for atleast one-two minutes to see the data written in the file since the program writes the data in the csv file every one mintue.

Hence you have a program to detect the number of people in the frame and to plot two diffrent graphs. Hope you guys like it! ENJOY YOUR CODE


*WE HAVE INCLUDED EXAMPLE CSV FILE SO YOU CAN DIRCETLY RUN PLOT.PY AND HEATMAP.PY TO CHECK THE OUTPUT*



DIRECTIONS OF USE:

1-Install all the necessary python packages:
  ~numpy
  ~imutils
  ~opencv
  ~opencv-contribute
  ~matpoltlib
  ~pandas
  ~seaborn
  ~psutil
  
 2-Comands to run the program:
  ~python CrowdDetection.py --prototxt Objects.prototxt.txt --model Objects.caffemodel
  ~python plot.py
  ~python HeatMap.py
 
3.Output
