import requests
import datetime


def check_domain():
    f = open("C:/Users/jayas/Documents/prjct/prjct/demofile.txt", "r")
    c = f.readlines() 
    for x in c:
        w = x.strip()

        y = requests.get(w)
        z = y.status_code
        if z == 404:
         print(w + " is Available")
         date= datetime.datetime.now()
         digits= date.strftime("%f")

         f = open(("Export/list" +"-" + digits +".txt"), "a")
         f.write(w + "\n")
         f.close()
        else:
         print(w + " is Not Available")

def http_check():
    f = open("demofile.txt", "r")
    c = f.readlines() 
    for x in c:
        w = x.strip()
        if w[0] == 'h':
         if w[1] == 't':
          if w[2] == 't':
           if w[3] == 'p':
            if w[4] == ':':
             if w[5] == '/':
              if w[6] == '/':
               print("Working")
               
            
check_domain()

