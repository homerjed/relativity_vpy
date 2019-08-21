# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 22:00:23 2019

@author: jedhm
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:08:12 2019

@author: jedhm
"""

"""
    animation to depict the relativistic variance
    of simultaneity.
"""

from vpython import *
import numpy as np

L = 2.5 

class car:
          
    def __init__(self, loc):
        
        # box dimension parameters
        s = 0.05
        L = 2.5
        w = 1.0
        
        # box faces 
        self.rod = box(pos=loc-vector(0,w/4,0),
                  size=vector(s,w,s),
                  color = color.green)
        
        self.bottom = box(pos=loc-vector(0,w/2,0),
                     size=vector(L,s,w),
                     color = color.blue)
        
        self.top = box(pos=loc+vector(0,w/2,0),
                  size=vector(L,s,w),
                  color = color.blue)
        
        self.facing = box(pos=loc-vector(0,0,w/2),
                     size=vector(L,w,s),
                     color = color.blue)
    
        self.left = box(pos=loc-vector(L/2,0,0),
                   size=vector(s,w+0.025,w),
                   color = color.yellow)
        
        self.right = box(pos=loc+vector(L/2,0,0), 
                    size=vector(s,w+0.025,w),
                    color = color.yellow)

        self.faces = [self.rod,self.bottom,self.top,
                      self.facing,self.left,self.right]
        
        self.cent_pos = loc
        
carriage = car(vector(-0.5,0,0))
bulb = sphere(pos=vector(0,-1.0,0),radius= 0.1,color=color.magenta)
flash1 = sphere(pos=vector(0,-1.0,0),radius= 0.05,color=color.yellow)
flash2 = sphere(pos=vector(0,-1.0,0),radius= 0.05,color=color.yellow)

t=0
v = 0.005

posgraph1 = gcurve(color=color.green)
posgraph2 = gcurve(color=color.red)
posgraph3 = gcurve(color=color.blue)
posgraph4 = gcurve(color=color.magenta)

while t < 10000:
    rate(1000)
    
    for face in carriage.faces:
        face.pos += vector(v*t,0,0)
    
    if carriage.facing.pos.x > 0:
        
        flash1.pos += vector(+3.0*v*t,0,0)    
        flash2.pos += vector(-3.0*v*t,0,0)    
        
        posgraph1.plot(pos=(t, abs(flash1.pos.x)))
        posgraph2.plot(pos=(t, abs(carriage.right.pos.x)))
        posgraph3.plot(pos=(t, abs(carriage.left.pos.x)))
        
        if abs((carriage.right.pos.x) - flash1.pos.x) < 0.0005:
            flash1.color = color.green
            carriage.right.color = color.green
            
        if abs((carriage.left.pos.x) - flash2.pos.x) < 0.0005:
            flash2.color = color.green
            carriage.left.color = color.green
    
        if flash1.pos.x > 3:
            break
    
    t+=0.00001
    
