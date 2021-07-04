import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from math import sqrt
import array as arr
from math import pi
import math
from operator import truediv

#Initialize variables
#Pr,Pt in mW 
#c is speed of light (m/s)
#f in MHz
#R in Km
Pr = 2*10**-14
Pt = 25
c = 3*10**8
f = 868*10**6
L = 10
N = 1000
C1 = 5470
C2 = 3125
C3 = 1760
C4 = 980
C5 = 440
C6 = 250
Cap_Tot = C1+C2+C3+C4+C5+C6
CAP = [C1,C2,C3,C4,C5,C6]
Radius = []
N_Devices = []
N_Devices1 = []
N_Devices2 = []
Area = []
S_tot = []
S_tot1 = []
S_tot2 = []
size = L*8
Pck = 1/100
G = 0.5
sim_time = 100
Pc = [0.454,0.714,0.86,0.94,0.976,0.997]
#Using Friis free space equation
#Pr = Pt* (c/4*pi*f)**2 * (1/R)**alpha
#On rearranging the equation
#R = ((Pt/Pr * (c/(4*pi*f))**2) **(1/alpha))

loss_exponent =  [3,3.5,4,4.5,5]
Area2 = []
N = []
D = 0

for alpha in [3]:
        R = ((Pt/Pr*(c/(4*math.pi*f))**2) **(1/alpha))/1000  #To get the value in Km
        A = pi * (R)**2
        Area.append(round(A,3))
        Radius.append(round(R,3))
        N = [G/(Pck * size) * b for b in (CAP)]
        N_Devices = sum(N)
        D = round(N_Devices / Area[0], 3)

              
def throughput(alpha):
    R = ((Pt/Pr*(c/(4*math.pi*f))**2) **(1/alpha))/1000  #To get the value in Km
    A = pi * (R)**2
    Area1 = []
    new_A = 0
    for n in Pc:
        An = n * A - new_A
        new_A = new_A + An
        Area1.append(round(An,3)) 
    N_Devices1 = [D * a for a in (Area1)]
    res = list(map(truediv, N_Devices1, CAP))
    G_SF = [Pck * size * b for b in (res)]
    S = []
    for i in range(0,len(G_SF)):
        S.append(CAP[i]*G_SF[i]*math.exp(-2*G_SF[i]))
    print(N_Devices1)
  
   
    
    
throughput(3)
throughput(3.5)
throughput(4)
throughput(4.5)
throughput(5)


