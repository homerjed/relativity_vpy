# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 11:09:50 2019

@author: jedhm
"""

from vpython import *

# axes 

scene = canvas(background = color.blue)

class axes:
    
    def __init__(self, loc, vel):
        
        L = 2
        dt = 0.01
        gamma = 1/sqrt(1-vel**2)
        
        def gamma(self):
            return 1/sqrt(1-vel**2)
        
        
        
        # def axis_length(self):
        #     return L/gamma
        
        # def tick_length(self):
        #     return dt*gamma
        
        self.L_v = L/gamma(self)
        
        self.dt_v = dt*gamma(self)
        
        self.x_ax = arrow(pos=loc,axis=vector(self.L_v,0,0), shaftwidth=0.1,
                          color=color.yellow)
        self.y_ax = arrow(pos=loc,axis=vector(0,L,0), shaftwidth=0.1,
                          color=color.yellow)
        self.z_ax = arrow(pos=loc,axis=vector(0,0,L), shaftwidth=0.1,
                          color=color.yellow)
        
        self.ball = sphere(pos=loc+vector(self.L_v,1.5,0),radius=0.2,
                           color=color.green)
        
        self.spring = helix(pos=loc, axis=vector(self.L_v,0,0), radius=0.5)
        
        self.axes = [self.x_ax,self.y_ax,self.z_ax,self.spring,self.ball]
        
    
O_axes = axes(vector(0,0,0),0)

S_axes = axes(vector(0,1,0),0.9)

v=0.9
t_O=0
t_S=0
dt_O=0.01
dt_S=S_axes.dt_v

while t_O < 1000:
    rate(100)
    
    if 100*t_O//2%2 == 0:
        O_axes.ball.color = color.green
    elif 100*t_O//2%2 != 0:
        O_axes.ball.color = color.yellow
    
    if 100*t_S//2%2 == 0:
        S_axes.ball.color = color.green
    elif 100*t_S//2%2 != 0:
        S_axes.ball.color = color.yellow
        
    for axis in S_axes.axes:
        axis.pos.x += 0.1*v*dt_O
    
    t_O+=dt_O
    t_S+=dt_S
    