import numpy as np
n=3
stored=[]
class Box:
    def __init__:
        self.values=np.array([[1,1,1],[-1,1,1],[1,1,-1],[-1,1,-1],[1,-1,1],[-1,-1,1],[1,-1,-1],[-1,-1,-1]])
        #self.tfr=np.array([1,1,1])
        #self.tfl=np.array([-1,1,1])
        #self.tbr=np.array([1,1,-1])
        #self.tbl=np.array([-1,1,-1])
        #self.bfr=np.array([1,-1,1])
        #self.bfl=np.array([-1,-1,1])
        #self.bbr=np.array([1,-1,-1])
        #self.bbl=np.array([-1,-1,-1])
        color=0
    def copy(x):
        self.values=x.values.copy()
    def transform(x,y,z):
        #takes an np array and adds to all points on box
        t=np.array([x,y,z])
        for i in self.values:
            i+=y
    def scale(x,y,z):
        s=np.array([x,y,z])
        for i in self.values:
            i*=s
    def rotX(deg):
        rad=deg*np.pi/180
        M=np.array([[1,0,0],[0,np.cos(rad),-np.sin(rad)],[0,np.sin(rad),np.cos(rad)]])
        self.values=(M@self.values.T).T
    def rotY(deg):
        rad=deg*np.pi/180
        M=np.array([[np.cos(rad),0,np.sin(rad)],[0,1,0],[-np.sin(rad),0,np.cos(rad)]])
        self.values=(M@self.values.T).T
    def rotZ(deg):
        rad=deg*np.pi/180
        M=np.array([[np.cos(rad),-np.sin(rad),0],[np.sin(rad),np.cos(rad),0],[0,0,1]])
        self.values=(M@self.values.T).T
    def out():
        #returns the values of the box
        self.color=np.random.randint(n)
        stored.append(self)
def R1(b,c):
    if(c<16):
        d=Box()
        d.copy(b)
        c+=1
        r=np.random.randint(4)
        if(r==0):
            dbox(d,c)
            d.transform(0,0,0.6)
            d.rotX(5)
            R1(d,c)
        if(r==1):
            dbox(d,c)
            d.transform(0,0,0.5)
            d.rotX(-90)
            R1(d,c)
        if(r==2):
            dbox(d,c)
            d.transform(0,0,0.6)
            d.rotZ(90)
            R1(d,c)
        if(r==3):
            dbox(d,c)
            d.transform(0,0,0.6)
            d.rotZ(-90)
            R1(d,c)
def dbox(b,c):
    if(c<16):
        d=Box()
        d.copy(b)
        c+=1
        r=np.random.randint(2)
        if(r==0):
            d.out()
        if(r==1):
            s=np.random.randint(2)
            if(s==0):
                d.rotY(90)
                d.scale(0.5,1,1)
                R1(d,c)
            if(s==1):
                d.rotX(90)
                d.scale(0.5,2,1)
                R1(d,c)
main=Box()
c=0
main.rotY(-90)
R1(main,c)
for i in stored:
    f =open(r"c"+stored.color+".obj","w")
