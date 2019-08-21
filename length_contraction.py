# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:52:54 2019

@author: jedhm
"""

from vpython import *

class spring:
         
    def __init__(self, loc, ax):
        self.m = 0.1
        self.rod = cylinder(pos=loc, axis=ax, radius=0.5, color=color.blue)
        self.spring = helix(pos=loc, axis=vector(5,0,0), radius=1, color=color.white)
    
spring = spring(vector(0,0,0),vector(5,0,0))

t=0
dt = 0.00001
v = 0.0001

spring.p = spring.m*v

F = 0.00000001

posgraph1 = gcurve(color=color.green)

while t < 10000:
    rate(10000)
    
    spring.p += F*t
    spring.spring.pos.x += spring.p*t/spring.m 
    spring.rod.pos = spring.spring.pos
    
    gamma = 1/sqrt(1-(100*spring.p/spring.m)**2)
    
    print(gamma)
    spring.spring.axis.x = spring.spring.axis.x/gamma

    
    posgraph1.plot(pos=(t, abs(spring.spring.pos.x)))
    t+=dt

