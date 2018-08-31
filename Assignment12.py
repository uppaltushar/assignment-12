#1
import datetime 
date=datetime.datetime.now()
print(date.day)

#2

import webbrowser as web
web.open("https://www.youtube.com/watch?v=3OTgce0fY6c&start_radio=1&list=RD3OTgce0fY6c")

#3

import os
os.chdir("E:\tushar")
path =  os.getcwd()
filenames = os.listdir(path)
i=1
print(filenames)
for filename in filenames:
    os.rename(filename,str(i)+'.jpg')
    i=i+1


