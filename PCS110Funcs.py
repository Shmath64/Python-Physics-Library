# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 08:05:04 2023

@author: 64mda
"""
#PCS110 Functions and Constants
import math

class Vector:
    
    def __init__(self, x=0, y=0, z=0):
        #Can take a 3-tuple, or 3 variables
        if type(x) == tuple: 
            self.x, self.y, self.z = x
        else:
            self.x = x
            self.y = y
            self.z = z
    
    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    
    def unit(self):
        mag = self.magnitude()
        unitize = lambda component: component / mag
        return Vector(unitize(self.x), unitize(self.y), unitize(self.z))
    
    @staticmethod
    def componentsFromAngles(thetax, thetay, thetaz):
        return math.cos(thetax), math.cos(thetay), math.cos(thetaz)
        #self.x = math.cos(thetax)
        #self.y = math.cos(thetay)
        #self.z = math.cos(thetaz)
        
    
        
