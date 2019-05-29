# -*- coding: utf-8 -*-
"""
Created on Sun May 26 19:13:03 2019

@author: Someone in Somewhere
"""

import math as m
G=6.674e-11*(149596870700**3)       #constant G en unidades de UA^3/s^2kg^2 )
m1=0.00000001
m2=2.0e30

def calc_anomalias(a,ex,t,r):   #t: tiempo t
    K=0.01720209908             #en UA^(3/2)/d
    #K=(G*m1)**(1/2)
    n1=K*(180/m.pi)/(a**(3/2))
    T1=360/n1
    theta1_rad=m.acos((1/ex)*(((a*(1-ex**2)/r)-1)))
    theta1=theta1_rad*(180/m.pi)
    
    T=2*m.pi/(K*(1+(m2/m1)**(1/2)))
    n=360/T    
    E=m.acos((r-a)/(a*ex))
    M=E-ex*m.sin(E)
    t0=t-(M/n)  
    theta=2* m.tan( ((1+ex)/(1-ex))**(1/2)* m.tan(E/2) )
    print(n1,"°/día\n",T1,"días\n",theta1,"°\n")
    print("Anomalía verdadera theta= ",theta,"\nAnomalía exéntrica E=\t",E,"\nAnomalía media M=\t",M, "\nTiempo de paso por el perihelio to=\t",t0)
    
calc_anomalias(2.56743,0.75355,2454272,2.325364)