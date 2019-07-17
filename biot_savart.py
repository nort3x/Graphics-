# -*- coding: utf-8 -*-
"""
Written and tested with python 3.7

"""
import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt


mu0 = (np.pi*4)*(10**(-7))
current = 100000
const = (mu0/(4*np.pi))*current

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]
    return c

def dervative(func,x,eps=10**(-9)):
    return (( func(x+eps)-func(x))/eps)



def integrand(t,path,position):
    return const*(cross(dervative(path,t),path(t) - position)/(np.sqrt( np.dot((path(t)-position),(path(t)-position)))**(3/2)))
    
    
def path1(t):
    n = 20
    l = 2
    #return np.array([np.cos(2*np.pi*t),np.sin(2*np.pi*t),0])   #loop
    #return np.array([0,0,l*t])                                 #straight wire
    return np.array([l*t*(np.cos(2*np.pi*t*n)),l*t*np.sin(2*n*np.pi*t),0])  #spiral
    #return np.array([np.cos(2*n*np.pi*t),np.sin(2*n*np.pi*t),-l/2 + l*t ])           #solenoid
    #return (np.array([np.cos(2*np.pi*t),np.sin(2*np.pi*t),1]) + np.array([np.cos(2*np.pi*t),np.sin(2*np.pi*t),-1])) #repaling loops
# biot savart
    
def B_S(path,position,N):
    t = np.linspace(0,1,N)
    bx = [];by =[];bz=[];
    for i in t:
        [bx0,by0,bz0] = integrand(i,path,position)
        bx.append(bx0);by.append(by0);bz.append(bz0)
    
    BX = np.sum(bx)/N; BY = np.sum(by)/N;BZ = np.sum(bz)/N
    return np.array([BX,BY,BZ])
        
    #return np.array([Bx,by,bz])


[bx,by,bz]= B_S(path1,np.array([0,0,0]),100)


# plot mag field

fig = plt.figure()
ax = fig.gca(projection='3d')
Bx = []; By=[];Bz=[]
for x in np.linspace(-2,2,8):
    for y in np.linspace(-2,2,8):
        for z in np.linspace(-2,2,8):
            [bx,by,bz]= B_S(path1,np.array([x,y,z]),100)
            q = ax.quiver(x,y,z,bx,by,bz,length= 1, cmap='Reds', lw=2,normalize=False)
            
            
#Draw path
            
X=[];Y=[];Z=[]        
for t in np.linspace(0,1,1000):
    [x,y,z] = path1(t)
    X.append(x);Y.append(y);Z.append(z)
    
X= np.array(X);Y= np.array(Y);Z= np.array(Z)


ax.plot(X,Y,Z,color='red',linewidth=1.0)