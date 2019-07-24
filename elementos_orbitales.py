# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 05:30:56 2019

@author: Someone in Somewhere
"""
import math as m
def elementos_orbitales(x,y,z,dx,dy,dz,fj):
    m2=0.000000000001 #kg
    m1=1.998e30          #kg             #Masa variable
    #ua=1.32712442099e20 #m**3 s**-2
    G=6.674e-11*(149596870700**3)               #constant G en unidades de UA^3/s^2kg^2 )  Confirmar valor
    #Magnitudes del vector posicion y velocidad
    r=(x**2+y**2+z**2)**0.5
    v=(dx**2+dy**2+dz**2)**0.5
    m2_under_m1=m2/m1
    K=(G*m1)**0.5               #Usualmente en ua**(3/2)/día**-1
    u=K**2*(1+m2_under_m1)
    a=r/(2-((1/u)*r*v**2))
    D=(r*v**2)/u
    if D<2:
        print ("a>0\tOrbita elíptica\n")
    if D>2:
        print ("a<0\tOrbita hiperbólica\n")
    if D==2:
        print ("a=infinite\tOrbita parabólica\n")
    print("\na=\t",a,"ua")
    e1=(1/u)*(x*(dx**2+dz**2)-dx*(y*dy+z*dz))-(x/r)
    e2=(1/u)*(y*(dx**2+dz**2)-dy*(z*dz+x*dx))-(y/r)
    e3=(1/u)*(z*(dx**2+dy**2)-dz*(x*dx+y*dy))-(z/r)
    
    h1=y*dz-z*dy
    h2=z*dx-x*dz
    h3=x*dy+y*dx
    
    e=(e1**2+e2**2+e3**2)**0.5
    h=(h1**2+h2**2+h3**2)**0.5
    
    dr=(x*dx+y*dy*z*dz)/r
    if dr>0:
        print("El objeto está en el 1 o 2 cuadrante\n")
    else:
        print("El objeto se encuentra en tercer o cuarto cuarante\n")
        
    """
    Calcular theta de forma manual
    """
    #theta=106.4
    theta=m.acos((1)*(a*(0)-r)/r)                    #Para órbita elíptica
    """
    Fin de cálculo manual
    """
    E=2*m.atan((((1-e)/(1+e))**0.5)*m.tan(theta/2))
    print("\nE=\t",E,"\ne=\t",e)
    n=(180/m.pi*K*(1+(m2/m1)**0.5))/(a**(3/2))
    
    #                               Calcular E de forma manual
  
    Mr=E-e*(180/m.pi)*m.sin(E)
    to=fj-(Mr/n)
    
    h_control=h1*e1+h2*e2+h3*e3
    
    i=m.acos(h3/h)
    Omega=m.atan(h1/(-h2))
    if h1*h<0 and h<0:
        Omega=Omega+180
    if h1*h<0 and h>0:
        Omega=Omega+360
    if h1+h<0:
        Omega=Omega+180
    w=m.atan(e3*h/(-e1*h2+e2*h1))
    if (e3*h)*(-e1*h2+e2*h1)<0 and (-e1*h2+e2*h1)<0:
        w=w+180
    if (e3*h)*(-e1*h2+e2*h1)<0 and (-e1*h2+e2*h1)>0:
        w=w+360
    if (e3*h)+(-e1*h2+e2*h1)<0:
        w=w+180
    
    print ("\ntheta=\t",theta,"\nh_control=\t",h_control,"\ni=\t",i,"\nOmega=\t",Omega,"\nw=\t",w,"\nt0=\t",to)   
    
    
elementos_orbitales(2.2757204,0.9292219,-0.3046801,-0.0032701,0.0101454,0.00000944,2458665.5) #¡La fecha debe ser Juliana!