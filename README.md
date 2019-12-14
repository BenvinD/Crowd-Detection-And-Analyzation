# Crowd-Detection-And-Analyzation
A Python Program to detect the maximum numbers of people present in the frame and show visualised analyse of the data
CrowdDetection.py First the program uses opencv to detet the people in the frame. It uses a specially trained algorithm known as the cascade of a program and this cascade uses diffrent

Objects.caffemodel Objects.prototxt.txt

training model to learn and try to detect many objets and people. Since we just need our program to detect only the number of people in the given frame we enable only the people model to detect people. With the help of the ids of each detection, the program counts the number of people in the frame for one minute. This data is converted to an average of one minute. The time library is used to keep a track of time. Both the average and current time data is used for processing the further project.

The average value and the time got are stroed as a csv file. This file is later used to plot the graphs

plot.py HeatMap.py

USing this data a normal realtime plot-line graph is used along with a custom heat map which uses only one input at a time.

P.S. if you are using the heat map please close the map to see the change for the second value in the csv.

Hence you have a program to detect the number of people in the frame and to plot two diffrent graphs. Hope you guys like it! ENJOY YOUR CODE


*WE HAVE INCLUDED AN EXAMPLE CSV FILE*
