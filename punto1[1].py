# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:41:45 2019

@author: Someone in Somewhere
"""

G=6.674e-11*(149596870700**3)       #constant G en unidades de UA^3/s^2kg^2 )
m1=0.
m2=2.0e30
def datos(x,y,z,dx,dy,dz):
    r=(x*x+y*y+z*z)**(1/2)
    dr_vector=dx+dy+dz
    v_cuad=dx*dx+dy*dy+dz*dz
    
    u=G*(m1+m2)
    d2x=u*x/(r**3)*-1.
    d2y=u*y/(r**3)*-1.
    d2z=u*z/(r**3)*-1.


    h1= y*dz-z*dy
    h2= z*dx-x*dz
    h3=x*dy-y*dx
    hcontrol= h1*x+h2*y+h3*z
    

    e1=((-1./u)*(h2*dz-h3*dy))-(x/r)
    e2=((-1./u)*(h3*dx-h1*dz))-(y/r)
    e3=((-1./u)*(h1*dy-h2*dx))-(z/r)
    e_h_control=e1*h1+e2*h2+e3*h3
    
    E_prima=(dr_vector*dr_vector*(1/2))-(u/r) 
    
    print ("\n e1= \t",e1, "\n e2= \t",e2,"\n e3= \t",e3,"\n\n\n h1= \t",h1,"\n h2= \t",h2,"\n h3= \t",h3,"\n hcontrol=\t ",hcontrol,"\n E prima=\t",E_prima,"\n e1 h1 control=\t",e_h_control)
    if r*dr_vector>0:
        print("\t El objeto se está alejando del sol\n",r*dr_vector)
    else:
        print("\t El objeto se está acercando al sol",r*dr_vector)
        
    e1_const=(-e2*h2-e3*h3)/h1
    if e1_const==e1:
        print("la constante e1 es depediente de las demás",e1,e1_const)
    else:
        print("la constante e1 no es depediente de las demás",e1,e1_const)
    h1_const=(-e2*h2-e3*h3)/e1
    if h1_const==h1:
        print("la constante h1 es depediente de las demás:",h1,h1_const)
    else:
        print("la constante h1 no es depediente de las demás:",h1,h1_const)
        
    h=(h1**2+h2**2+h3**2)**(1/2)
    dr_cuad=(dx+dy+dz)**2
    dtheta_cuad=(h/r**2)**2        
    v_cuad2=dr_vector**2+r**2*dtheta_cuad
    if v_cuad==v_cuad2:
        print ("dr^2+r^2*dtheta^2=dx^2+dy^2+dz^2", v_cuad, v_cuad2)
        
datos(-0.578828596,0.423986599,0.039220299,-0.0120306723,-0.0164182347,0.0004689794)
