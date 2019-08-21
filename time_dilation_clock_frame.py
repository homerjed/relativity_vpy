# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:38:39 2019

@author: jedhm
"""

from vpython import *

class light_clock:
    
    
    # light clock with photon reflecting      
    
    def __init__(self, loc):
        
        # clock dimension parameters
        s = 0.05
        self.L = 1
        w = 1
        
        # clock parts        
        self.bottom = box(pos=loc+vector(0,-w/2,0),
                     size=vector(self.L,s,w),
                     color = color.blue)
        
        self.top = box(pos=loc+vector(0,+w/2,0),
                  size=vector(self.L,s,w),
                  color = color.blue)
        
        self.pho = sphere(pos=loc,radius=0.05,color=color.yellow,
                                  make_trail=True)
        
        self.obj = [self.bottom,self.top,self.pho]
        
        self.cent_pos = loc
        
# spawn light clock

class observer:
    def __init__(self, loc):
        self.obs = sphere(pos=loc, radius = 0.1, color=color.green)

obs = observer(vector(0,0.2,0))
clock1 = light_clock(vector(0,1,0))
clock2 = light_clock(vector(3,-1,0))
clock3 = light_clock(vector(5,-1,0))

t=0
dt = 0.00001
v = 0.0001
clock_velocity = vector(-2*v,0,0)
observer_velocity = vector(-v,0,0)

# contraction
gamma = 1/sqrt(1.0-0.9**2)

clock1.pho.velocity = vector(0,2*v,0)
clock2.pho.velocity = vector(0,2*v,0)
clock3.pho.velocity = vector(0,2*v,0)
clock1.pho.mass = 0.25
clock2.pho.mass = 0.25
clock3.pho.mass = 0.25

clock1.pho.p = clock1.pho.velocity*clock1.pho.mass
clock2.pho.p = clock2.pho.velocity*clock2.pho.mass
clock3.pho.p = clock3.pho.velocity*clock3.pho.mass

clock2.L = clock2.L*gamma
clock3.L = clock3.L*gamma

while t < 10000:
    rate(10000)

    # moving clock
    clock1.pho.pos += clock1.pho.p*t/clock1.pho.mass
    
    for objekt in clock2.obj:
        objekt.pos += clock_velocity*t
        
    for objekt in clock3.obj:
        objekt.pos += clock_velocity*t
        
    if not (clock1.bottom.pos.y + clock1.pho.radius) < clock1.pho.pos.y < (clock1.top.pos.y - clock1.pho.radius):
        clock1.pho.p.y = -clock1.pho.p.y    

    # stationary clocks
    clock2.pho.pos += clock2.pho.p*t/clock2.pho.mass
    clock2.pho.color = color.magenta
    clock2.pho.make_trail = False
    clock3.pho.pos += clock3.pho.p*t/clock3.pho.mass
    clock3.pho.color = color.magenta

    if not (clock2.bottom.pos.y + clock2.pho.radius) < clock2.pho.pos.y < (clock2.top.pos.y - clock2.pho.radius):
        clock2.pho.p.y = -clock2.pho.p.y  

    if not (clock3.bottom.pos.y + clock3.pho.radius) < clock3.pho.pos.y < (clock3.top.pos.y - clock3.pho.radius):
        clock3.pho.p.y = -clock3.pho.p.y 


    t += dt
