# -*- coding: utf-8 -*-
"""
Created on Wed May 29 23:57:48 2019

@author: Someone in Somewhere
"""
import math as m
def bisiesto(ano):
    if ano%4==0:
        if ano%100!=0 or ano%400==0:
            print("Año bisiesto")
        else:
            print ("Año NO bisiesto")
    else:
        print ("Año NO bisiesto")
bisiesto(2000)                              # <-------Introducir año para saber si es bisiesto
                          

def posi_geo_ecuat(año_miles,año_cientos,meses,dias,i1,Omega1,w_raya1,a1,n1,e1,L1,i2,Omega2,w_ray2, a2, n2, e2, L2):
    
    """
            año_miles:      Equiv miles deaño JC
            año_cientostos: Equiv cientos de años CJ
            meses:          Equi meses CJ
            dias:           Equiv días CJ
            i:              Inclinación                     [°]
            Omega:          Longitud del nodo ascendente    [°]
            w_raya:         Longitud del perihelio          [°]
            a:              Semieje mayor                   [UA]
            n:              Movimiento díaro                [°]
            e:              Excentricidad 
            L:              Longitud media                  [°]
    """
    julian_date=año_miles+año_cientos+meses+dias
    
    t=julian_date
    print(t)
    w1=w_raya1-Omega1
    w2=w_ray2-Omega2
    tr1=2457151.5
    tr2=2457165.5
    dif1_t=t-tr1
    dif2_t=t-tr2
    M1_ref=L1-w_raya1                     #M1_ref: Anomalía media de referencia para el cuerpo 1
    M2_ref=L2-w_ray2                  #M2_ref: Anomalía media de referencia para el cuerpo 2
    
    M1=M1_ref+n1*dif1_t                   #Anomalia media praa cuerpo 1
    M2=M2_ref+n2*dif2_t                   #Anomalia MEdia para el cuerpo2
    print(M1,M2)
    E1=104.5905197919317
    E2=164.9341109022997
    
    r1=a1*(1-e1*m.cos(E1))
    r2=a2*(1-e2*m.cos(E2))
    theta1=2* m.tan( ((1+e1)/(1-e1))**(1/2)* m.tan(E1/2) )
    theta2=2* m.tan( ((1+e2)/(1-e2))**(1/2)* m.tan(E2/2) )
    x1=r1*(m.cos(theta1+w1)*m.cos(Omega1)-m.sin(theta1+w1)*m.cos(i1)*m.sin(Omega1))
    y1=r1*(m.cos(theta1+w1)*m.sin(Omega1)+m.sin(theta1+w1)*m.cos(i1)*m.sin(Omega1))
    z1=r1*m.sin(theta1+w1)*m.sin(i1)
    
    x2=r2*(m.cos(theta2+w2)*m.cos(Omega2)-m.sin(theta2+w2)*m.cos(i2)*m.sin(Omega2))
    y2=r2*(m.cos(theta2+w2)*m.sin(Omega2)+m.sin(theta2+w2)*m.cos(i2)*m.sin(Omega2))
    z2=r2*m.sin(theta2+w2)*m.sin(i2)
    """
    Vectores geocéntricos eclípticos:
        
    """
    xhi=x1-x2               #E curva triple
    eta=y1-y2               #n larga
    dseta=z1-z2             #Z alargada
    
    epsilon=23.43927944         #Constante 
    xhi_prima= xhi
    eta_prima= eta*m.cos(epsilon)-dseta*m.sin(epsilon)
    dseta_prima= eta*m.sin(epsilon)+dseta*m.cos(epsilon)
    
    alpha=m.atan(xhi_prima/eta_prima)
    delta=m.asin(dseta_prima/((dseta_prima**2+eta_prima**2+dseta_prima**2)**(1/2)))
    rho=((dseta_prima**2+eta_prima**2+dseta_prima**2)**(1/2))
    
    if eta_prima*dseta_prima<0 and dseta_prima<0:
        alpha=alpha+180
    if eta_prima*dseta_prima<0 and dseta_prima>0:
        alpha=alpha+360
    if eta_prima+dseta_prima<0:
        alpha=alpha+180
    print ("\nLa posición geocéntrica ecuatorial del planeta Marte es:\n\nalpha(Ascención recta:\t",alpha,"°\ndelta (Inclinación):\t",delta,"°\nrho (Distancia):\t",rho,"UA")
    print ("\nLa posición geocéntrica ecuatorial del planeta Sol es:\n\nalpha(Ascención recta:\t",-alpha,"°\ndelta (Inclinación):\t",-delta,"°\nrho (Distancia):\t",-rho,"UA")
    
    
    

posi_geo_ecuat(2451544.5,5478,151,20,1.84842,49.5127, 336.0414, 1.5235812,0.5240913,0.0934555,53.44285,0.00191,174.4,102.9900,0.9999984,0.9856129,0.0167026,240.07820)
    
