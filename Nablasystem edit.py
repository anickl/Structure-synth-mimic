import numpy as np
n=3
stored=[]
class Box:
    def __init__(self):
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
    def copy(self,x):
        self.values=x.values.copy()
    def transform(self,x,y,z):
        #takes an np array and adds to all points on box
        t=np.array([x,y,z])
        for i in self.values:
            i+=y
    def scale(self,x,y,z):
        s=np.array([x,y,z])
        for i in self.values:
            i*=s
    def rotX(self,deg):
        rad=deg*np.pi/180
        M=np.array([[1,0,0],[0,np.cos(rad),-np.sin(rad)],[0,np.sin(rad),np.cos(rad)]])
        self.values=(M@self.values.T).T
    def rotY(self,deg):
        rad=deg*np.pi/180
        M=np.array([[np.cos(rad),0,np.sin(rad)],[0,1,0],[-np.sin(rad),0,np.cos(rad)]])
        self.values=(M@self.values.T).T
    def rotZ(self,deg):
        rad=deg*np.pi/180
        M=np.array([[np.cos(rad),-np.sin(rad),0],[np.sin(rad),np.cos(rad),0],[0,0,1]])
        self.values=(M@self.values.T).T
    def out(self):
        #returns the values of the box
        self.color=np.random.randint(n)
        stored.append(self)
def R1(b,c):
    if(c<30):
        d=Box()
        d.copy(b)
        c+=1
        r=np.random.rand()*4.01
        if(r<1):
            dbox(d,c)
            d.transform(0,0,0.6)
            d.rotX(5)
            R1(d,c)
        elif(r<2):
            dbox(d,c)
            d.transform(0,0,0.5)
            d.rotX(-90)
            R1(d,c)
        elif(r<3):
            dbox(d,c)
            d.transform(0,0,0.6)
            d.rotZ(90)
            R1(d,c)
        elif(r<4):
            dbox(d,c)
            d.transform(0,0,0.6)
            d.rotZ(-90)
            R1(d,c)
def dbox(b,c):
    if(c<30):
        d=Box()
        d.copy(b)
        c+=1
        r=np.random.rand()*2
        if(r<1):
            d.out()
        elif(r<1.5):
            d.rotY(90)
            d.scale(0.5,1,1)
            R1(d,c)
        else:
            d.rotX(90)
            d.scale(0.5,2,1)
            R1(d,c)
main=Box()
c=0
main.rotY(-90)
R1(main,c)
v=[]
f=[]
qq=[1]*n

for i in range(n):
    v.append([])
    f.append([])
for i in stored:
    for j in range(8):
        v[i.color].append(i.values[j])
    q=qq[i.color]
    '''
    f[i.color].append([q,q+2,q+5,q+4])
    f[i.color].append([q+5,q+7,q+3,q+2])
    f[i.color].append([q+2,q+3,q+1,q])
    f[i.color].append([q+3,q+7,q+5,q+1])
    f[i.color].append([q+7,q+6,q+4,q+5])
    f[i.color].append([q+6,q+2,q,q+4])
    
    '''
    f[i.color].append([q,q+4,q+2])
    f[i.color].append([q+2,q+4,q+6])
    f[i.color].append([q,q+2,q+1])
    f[i.color].append([q+1,q+2,q+3])
    f[i.color].append([q,q+1,q+4])
    f[i.color].append([q+4,q+1,q+5])
    f[i.color].append([q+2,q+6,q+3])
    f[i.color].append([q+3,q+6,q+7])
    f[i.color].append([q+1,q+3,q+5])
    f[i.color].append([q+5,q+3,q+7])
    f[i.color].append([q+2,q+6,q+3])
    f[i.color].append([q+5,q+7,q+4])
    f[i.color].append([q+4,q+7,q+6])
    qq[i.color]+=8

for i in range(n):
    textfile=open("out"+str(i)+".obj","w+")
    textfile.write("#obj write -Alex Nickl" + "\n")
    for j in v[i]:
        textfile.write("v "+str(j[0])+' '+str(j[1])+' '+str(j[2])+"\n")
    textfile.write("\n")
    for j in f[i]:
        textfile.write("f "+str(j[0])+' '+str(j[1])+' '+str(j[2])+"\n")
    textfile.close()

                       
    
    
