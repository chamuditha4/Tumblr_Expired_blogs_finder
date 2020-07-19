import tkinter as tk
from tkinter import *  
from tkinter import filedialog as fd 
import requests
import datetime
from random import *


root = tk.Tk()
 
root.geometry('300x100')
root.title("Tumblr checker")
root.iconbitmap('img/favicon.ico')
root.resizable('False','False')

pathr ="demofile.txt"
ran = randint(1, 10000)

def msg():
    l.config(text="Finished!.")  
    
def progress():
    l.config(text=())

def check_domain():
    precent = 0
    progressbr = 0;
    
    pathr= fd.askopenfilename() 
    count = len(open(pathr).readlines(  ))
    print(count)
    f = open(pathr, "r")
    c = f.readlines()
    for x in c:
        w = x.strip()

        
        y = requests.get(w)
        z = y.status_code
        if z == 404:
         print(w + " is Available")
         date= datetime.datetime.now()
         digits= date.strftime("%j")
         

         f = open(("Export/list" +"-" + digits +  str(ran) +".txt"), "a")
         f.write(w + "\n")
         f.close()
         precent +=1
         progressbr = (precent*100)/count 
         
         
        else:
         print(w + " is Not Available")
         precent +=1
         progressbr = (precent*100)/count 
                  
           
         
         
    msg()


def callback():
    
    print(pathr)
    check_domain()
    errmsg = 'Error!'


tk.Button(text='Open the text File', bg="black", fg="white" , width=25, height=2, 
       command=callback) .pack(padx=15,pady=15)
l = tk.Label(root, width=20, text='')
l.pack()

tk.mainloop()