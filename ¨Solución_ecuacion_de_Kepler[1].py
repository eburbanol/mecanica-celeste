# -*- coding: utf-8 -*-
#! /usr/bin/python

# initialise cos-sin look-up table
from math import pi, cos, sin, floor
divtwopi = 1 / (2*pi)
acs = [(a, cos(a), sin(a)) for a in \
        [pi/2**i for i in range(1,60)]]

def calc_E(M, e, n=29):
   '''
   Compute the eccentric anomaly.
   
   Parameters
   ----------
   M : float
      Mean anomaly.
   e : float
      Eccentricity.
   n : integer
      Number of iterations.
   
   Example
   -------
   >>> Ecs(2-sin(2), 1)
   (1.99999999538762, -0.4161468323531165, 0.9092974287451092)
   '''
   E = 2 * pi * floor(M*divtwopi+0.5)
   cosE, sinE = 1., 0.
   for a,cosa,sina in acs[:n]:
      if E-e*sinE > M:
         a, sina = -a, -sina
      E += a
      cosE, sinE = cosE*cosa - sinE*sina,\
                   cosE*sina + sinE*cosa
   print ("     E=\t",E)
    

calc_E(28.51089478, 0.08714317)



