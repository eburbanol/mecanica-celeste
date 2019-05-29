# -*- coding: utf-8 -*-
"""
Created on Sun May 26 16:24:17 2019

@author: Someone in Somewhere
"""
import math as m
def tiempo(date):
    julian_date_ref=2455200.5  #(Tiempo de referencia t0)
    dif_t=date-julian_date_ref
    return dif_t
        
tiempo(2455275)

def calc_aste(M,n,a,ex,T,E):
    r= a*(1- (ex*m.cos(E)) )
    theta=2* m.tan( ((1+ex)/(1-ex))**(1/2)* m.tan(E/2) )
    print("r=\t",r,"\n theta=\t",theta)
calc_aste(333.59563,0.41236038,1.7876593,0.4289682,161.57683,316.757499648)
    
    