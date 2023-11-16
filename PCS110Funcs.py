# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 08:05:04 2023

@author: 64mda
"""
#PCS110 Functions and Constants
import math

#CONSTANTS:  (!!Maybe read/write this from a text file?)
nTypes = (float, int) #Numerical types; used for checking data types
c = 3e8         #m/s - speed of light
G = 6.7e-11     #N*m**2 - Gravitational Constant
g = 9.8         #N/kg - Approx. gravitational field near Earth's surface
me = 9e-31      #kg - Electron mass
mp = 1.7e-27    #kg - Proton mass
mn = 1.7e-27    #kg - Neutron mass
EC = 9e9        #N*m**2/C**2 - Electric constant
e = 1.6e-19     #C - Proton Charge
Na = 6.02e23    #Atoms/mol - Avogadro's Number
h = 6.6e-34     #J*s - Plank's Constant

def checkNType(x):
    if type(x) not in nTypes:
        raise TypeError("must be a numerical value (float or integer)")

def checkNTypeTuple(t):
    for x in t:
        if type(x) not in nTypes:
            raise TypeError("The tuple must only contain numerical values (floats or integers)")
            
def gamma(v): #Lorentz Factor
    checkNType(v)
    return 1 / math.sqrt(1-(v**2 / c**2))

class Vector:
    
    def __init__(self, x=0, y=0, z=0):
        #Can take a 3-tuple, or 3 variables
        if type(x) == tuple: 
            checkNTypeTuple(x)
            if len(x) != 3: raise Exception("The Tuple must have 3 elements")
            self.x, self.y, self.z = x
        elif type(x) in nTypes and type(y) in nTypes and type(z) in nTypes:
            self.x = x
            self.y = y
            self.z = z
        else:
            raise TypeError("Only floats and integers can be used to create a vector")
    
    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"
    
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def mag(self): #Short alternative for magnitude
        return self.magnitude()
    
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
        

if __name__ == "__main__":
    running = True
    print("PCS110 Functions and Constants")
    #while loop with inputs and checking things and stuff
    
        
