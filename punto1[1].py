# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:41:45 2019

@author: Someone in Somewhere
"""

G=6.674e-11*(1/149596870700**3)*(86400**2)       #constant G en unidades de UA^3/(dia^2 kg^2 )
m1=0.
m2=2.0e30
def datos(x,y,z,dx,dy,dz):
    r=(x*x+y*y+z*z)**(1/2)
        
    u=G*(m1+m2)
    """
    Para hallar h1,h2,h3
    """
    h1= y*dz-z*dy
    h2= z*dx-x*dz
    h3=x*dy-y*dx
    hcontrol= h1*x+h2*y+h3*z
    """
    Para hallar e1,e2,e3
    """
    e1=((-1./u)*(h2*dz-h3*dy))-(x/r)
    e2=((-1./u)*(h3*dx-h1*dz))-(y/r)
    e3=((-1./u)*(h1*dy-h2*dx))-(z/r)
    e_h_control=e1*h1+e2*h2+e3*h3
    
    E_prima=((dx**2+dy**2+dz**2)*(1/2))-(u/r) 
    
    print ("\n\n h1= \t",h1,"\n h2= \t",h2,"\n h3= \t",h3,"\n hcontrol=\t ",hcontrol,"\n\n\n e1= \t",e1, "\n e2= \t",e2,"\n e3= \t",e3,"\n\n E prima=\t",E_prima,"\n e1 h1 control=\t",e_h_control)
    r_punto=(x*dx+y*dy+z*dz)/(r)
    if r_punto>0:
        print("'\n El objeto se està alejando del sol ya que r_punto es mayor que cero\n \n r_punto=\t",r_punto)
    else:
        print("'\n El objeto se està acercando al sol, ya que r_punto es mayor que cero\n\n r_punto=\t",r_punto)
      
    e1_const=(-e2*h2-e3*h3)/h1
    h1_const=(-e2*h2-e3*h3)/e1
    if "{0:.9f}".format(e1)=="{0:.9f}".format(e1_const):
        print("\nLa constante e1 es dependiente de las demàs\ne1=\t",e1,e1_const)
    else:
        print("\nLa constante e1 no es dependiente de las demàs\ne1=\t",e1,e1_const)
    
datos(-0.578828596,0.423986599,0.039220299,-0.0120306723,-0.0164182347,0.0004689794)
