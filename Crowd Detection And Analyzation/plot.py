#python plot.py

#importing all the packages
import csv 
import matplotlib.pyplot as plt 
import time

x=[]
y=[]

#reading data from the csv file 
while True:
    with open("data.csv",'r')as csvfile:
            plots= csv.reader(csvfile, delimiter=',')
            for row in plots:
                x.append(str(row[0]))
                y.append(int(row[1]))

    # marking points on the graph 
    plt.plot(x,y, marker='o')

    plt.title('Data from the CSV File: Time vs NUmber of Person')

    plt.xlabel('Time')
    plt.ylabel('Number of People')
    plt.show()




