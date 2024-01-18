#python HeatMap.py


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import matplotlib.animation as animation
import pyautogui
import time
import os
import psutil
import csv


listOfProcessNames = list()
#Iterate over all running processes
x=[]
y=[]


while True:
  with open("data.csv",'r')as csvfile:
    df=csv.reader(csvfile,delimiter=',')
    
    for row in df:
      x.append(str(row[0]))
      y.append(int(row[1]))
      a=len(x)
      
  for i in range(a):
    
    df = pd.DataFrame({'Time': x[i], 'No.of People': y[i],'value':y[i]},index=[0])
    uniform_data = df.pivot(index='No.of People', columns='Time', values='value')
    ax = sns.heatmap(uniform_data, cbar_kws={'ticks': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]}, vmin=0, vmax=20,cmap="PuBu",linecolor='red',linewidths=1) 
    
    plt.show()




  