# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 18:39:06 2019

@author: Someone in Somewhere
"""
import math as m
from sympy import var, solve
def tiempos(t1,t2,t3,alpha1,delta1,rho1,alpha2,delta2,rho2):
    """
    
    Componentes de los vectores posición del Sol con respecto a la tierra para los tiempos t1,t2,t3
    
    """
    x1_prima_t=
    y1_prima_t=
    z1_prima_t=
    x2_prima_t=
    y2_prima_t=
    z2_prima_t=
    x3_prima_t=
    y3_prima_t=
    z3_prima_t=
    
    xi_prima_t1=rho1*(m.cos alpha1)* m.cos(delta1)
    eta_prima_t1= rho1*m.sin(alpha1)*m.cos(delta1)
    dseta_prima_t1= rho1*m.sin(delta1)
    
    xi_prima_t2=rho2*(m.cos alpha2)* m.cos(delta2)
    eta_prima_t2= rho2*m.sin(alpha2)*m.cos(delta2)
    dseta_prima_t2= rho2*m.sin(delta2)
    
    xi_prima_t3=rho3*(m.cos alpha3)* m.cos(delta3)
    eta_prima_t3= rho3*m.sin(alpha3)*m.cos(delta3)
    dseta_prima_t3= rho3*m.sin(delta3)
    """
            Conversión a coordenadas ecuatoriales heliocéntricas para t1,t2 y t3
    """
    x_prima1=xi_prima_t1-x1_prima_t
    y_prima1=eta_prima_t1-y1_prima_t
    z_prima1=dseta_prima_t1-z1_prima_t


    x_prima2=xi_prima_t2-x2_prima_t
    y_prima2=eta_prima_t2-y2_prima_t
    z_prima2=dseta_prima_t2-z2_prima_t    
    
    x_prima3=xi_prima_t3-x3_prima_t
    y_prima3=eta_prima_t3-y3_prima_t
    z_prima3=dseta_prima_t3-z3_prima_t
    
    """
        Ahora, pasaremos a las coordenadas eclípticas heliocéntricas para t1,t2 y t3
    """
    epsilon=23.43929167  #Constante (Oblicuidad de la eclíptica)
    #Para t1
    x1=x_prima1
    y1=y_prima1*m.cos(epsilon)+z_prima1*m.sin(epsilon)
    z1=z_prima1*m.cos(epsilon)-y_prima1*m.sin(epsilon)
    
    #Para t2
    x2=x_prima2
    y2=y_prima2*m.cos(epsilon)+z_prima2*m.sin(epsilon)
    z2=z_prima2*m.cos(epsilon)-y_prima2*m.sin(epsilon)
    
    #Para t3
    x3=x_prima1
    y3=y_prima3*m.cos(epsilon)+z_prima3*m.sin(epsilon)
    z3=z_prima3*m.cos(epsilon)-y_prima3*m.sin(epsilon)
    
    r1=(x1**2+y1**2+z1**2)**0.5
    r2=(x2**2+y2**2+z2**2)**0.5
    r3=(x3**2+y3**2+z3**2)**0.5
    """"
            Vector h a partir de r1xr2
    """"
    r1xr2_i=y1*z2-y2*z1
    r1xr2_j=x2*z1-x1*z2
    r1xr2_k=x1*y2-x2*y1
    
    r1xr2_norma=(r1xr2_i**2+r1xr2_j**2+r1xr2_k**2)**0.5
    h_i=r1xr2_i/r1xr2_norma
    h_j=r1xr2_j/r1xr2_norma
    h_k=r1xr2_k/r1xr2_norma
    
    i=m.acos(h_k), Omega=m.atan(h_i/-h_j)
    #El vector h
    h_i=m.sin(Omega)*m.sin(i)
    h_j=-m.cos(Omega)*m.sin(i)
    h_k=m.cos(i)
    
    #El vector n
    n_i=m.cos Omega
    n_j=m.sin(Omega)
    
    #El vector m
    m_i=-m.sin(i)
    m_j=m.cos(Omega)*m.cos(i)
    m_k=m.sin(i)
    
    #r1-r2 vector
    r1_dif_r2_i=x1-x2
    r1_dif_r2_j=y1-y2
    r1_dif_r2_k=z1-z2
    
    #r1-r3 vector
    r1_dif_r3_i=x1-x3
    r1_dif_r3_j=y1-y3
    r1_dif_r3_k=z1-z3
    
    #Producto punto entre r1-r2 y r1-r3 con m y n
    r1_dif_r2_punto_n= r1_dif_r2_i*n_i+r1_dif_r3_j*n_j
    r1_dif_r2_punto_m= r1_dif_r2_i*m_i+r1_dif_r2_j*m_j+r1_dif_r2_k*m_k
    r1_dif_r3_punto_n= r1_dif_r3_i*n_i+r1_dif_r3_j*n_j
    r1_dif_r3_punto_m= r1_dif_r3_i*m_i+r1_dif_r3_j*m_j+r1_dif_r3_k*m_k 
    
    #r2-r1 norma
    r2_dif_r1_norma=r2-r1
    r3_dif_r1_norma=r3-r1
    
    H, K = var('H K')

    f1 = (x**2)+(y**2)-2*(4.41*x+2.68*y)+25.59
    f2 = (x**2)+(y**2)-2*(3.23*x+2.1*y)+14.49

    sols = solve((f1, f2), (H, K))
    
    
    
    
    
tiempos()