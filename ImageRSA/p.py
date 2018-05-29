import Tkinter as tk
from Tkinter import Tk
from tkFileDialog import askopenfilename
import random
import os,sys
import numpy 
from PIL import Image
import time

def Mainproject(jpgfile):
    #jpgfile = Image.open("a.jpg")
    jpgfile.show()
    print (jpgfile.bits, jpgfile.size, jpgfile.format)
    row,col = jpgfile.size
    pixels = jpgfile.load()

    row1 = 1000003
    phi = [0 for x1 in range(row1)]
    occ = [0 for x1 in range(row1)]
    primes = [] 
    phi[1] = 1
    #phi[2] = 1
    #print (phi)
    for i in range(2,1000001):
        #print (i)
        if(phi[i] == 0):
            phi[i] = i-1
            #print (i)
            primes.append(i)
            #j = 2*i
            for j in range (2*i,1000001,i):
                #print("j ",j)
                #print(j)
                if(occ[j] == 0):
                    #print ("inside if2")
                    occ[j] = 1
                    phi[j] = j
                    #print (phi[j])
                    #print ((i-1)//i)
                phi[j] = (phi[j]*(i-1))//i
                #print(phi[j])
                #j = j + i
    #print (primes)
    p = primes[random.randrange(1,167)]
    q = primes[random.randrange(1,167)]
    print p," ", q
    n = p*q
    mod = n
    phin1 = phi[n]
    phin2 = phi[phin1]
    e = primes[random.randrange(1,9000)]
    mod1 = phin1
    def power1(x,y,m):
        ans=1
        while(y>0):
            if(y%2==1):
                ans=(ans*x)%m
            y=y//2
            x=(x*x)%m
        return ans
    d = power1(e,phin2-1,mod1)

    enc = [[0 for x in range(row)] for y in range(col)]
    dec = [[0 for x in range(row)] for y in range(col)]

    for i in range(col):
        for j in range(row):
            r,g,b = pixels[j,i]
            r1 = power1(r+(j*i)%255,e,mod)
            g1 = power1(g+(j*2*i)%255,e,mod)
            b1 = power1(b+(j*i)%255,e,mod)
            enc[i][j] = [r1,g1,b1]
    print pixels[row-1,col-1]

    img = numpy.array(enc,dtype = numpy.uint8)
    img1 = Image.fromarray(img,"RGB")
    #pixels2 = img1.load()
    time.sleep(3)
    img1.show()

    for i in range(col):
        for j in range(row):
            r,g,b = enc[i][j]
            r1 = power1(r,d,mod)-(j*i)%255
            g1 = power1(g,d,mod)-(j*2*i)%255
            b1 = power1(b,d,mod)-(j*i)%255
            dec[i][j] = [r1,g1,b1]
            
    img2 = numpy.array(dec,dtype = numpy.uint8)
    img3 = Image.fromarray(img2,"RGB")
    time.sleep(3)
    img3.show()
    img3.save('out.bmp')
    j = Image.open("out.bmp")
    img = j.save("out.jpg")
    

    
def action():
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    name = os.path.split(filename)
    jpgfile = Image.open(filename)
    label.config(text=str(name[1]))
    Mainproject(jpgfile)
    
def close():
    root.destroy
    sys.exit(0)
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Image RSA")
    root.geometry("500x200") 
    label = tk.Label(root, fg="red")
    label.config(text="Upload Image")
    label.pack()

    button = tk.Button(root, text='Upload', width=25, command= lambda: action())
    button1 = tk.Button(root, text='abort', width=25, command=lambda: close())
    button.pack()
    button1.pack()
    root.mainloop()



