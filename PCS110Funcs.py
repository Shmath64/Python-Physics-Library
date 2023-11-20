# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 08:05:04 2023

@author: 64mda
"""
#PCS110 Functions and Constants
import math
from typing import Union

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

degToRad = lambda x: x*(math.pi/180)
radToDeg = lambda x: x*(180/math.pi)

class Vector:
    
    def __init__(self, x=0, y=0, z=0):
        #Can take a 3-tuple, or 3 variables
        if type(x) == tuple: 
            self.__init__(*x) #Separate tuple into three elements
        
        elif type(x) in nTypes and type(y) in nTypes and type(z) in nTypes:
            self.x = x
            self.y = y
            self.z = z
        else:
            raise TypeError("Only floats and integers can be used to create a vector")
    
    def __str__(self):
        return f"<{self.x}, {self.y}, {self.z}>"
    
    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)
    def mag(self) -> float: #Short alternative for magnitude
        return self.magnitude()
    
    def unit(self) -> object:
        mag = self.magnitude()
        unitize = lambda component: component / mag
        return Vector(unitize(self.x), unitize(self.y), unitize(self.z))
        raise ZeroDivisionError("Cannot find unit vector of a zero vector")
    
    @staticmethod
    def scalarMultiply(vector, scalar):
        checkNType(scalar)
        vector.x *= scalar
        vector.y *= scalar
        vector.z *= scalar
        return vector
        
    
    @staticmethod
    def componentsFromAngles(thetax, thetay, thetaz, usingRads=False): 
        """

        Parameters
        ----------
        thetax : numerical type
            DESCRIPTION.
        thetay : numerical type
            DESCRIPTION.
        thetaz : numerical type
            DESCRIPTION.
        usingRads : bool, optional
            DESCRIPTION. The default is False.

        Returns
        -------
        Vector
            DESCRIPTION.

        """
        if usingRads: return math.cos(thetax), math.cos(thetay), math.cos(thetaz)
        return math.cos(degToRad(thetax)), math.cos(degToRad(thetay)), math.cos(degToRad(thetaz))
        

def checkNType(*args): #Any number of arguments
    for arg in args:
        if type(arg) not in nTypes:
            raise TypeError(f"Must be a numerical value (float or integer)\n{arg} is not a float or an integer")
    return True

def checkNTypeTuple(t):
    for x in t:
        if type(x) not in nTypes:
            raise TypeError("The tuple must only contain numerical values (floats or integers)")
            
def gamma(v): #Lorentz Factor
    checkNType(v)
    return 1 / math.sqrt(1-(v**2 / c**2))

def forceOfGravity(m1, m2, r) -> Union[Vector, float]: #Checked, Works!
    if isinstance(r, Vector):                        #If it's a vector
        fMag = -(G * m1 * m2) / (r.magnitude()**2)   #Get magnitude of force
        return Vector.scalarMultiply(r.unit(), fMag) #Return vector value
    
    elif checkNType(r):                 #If not a vector
        return -(G * m1 * m2) / (r**2)  #Return scalar value
    
def nearEarthForceOfGravity(m):
    checkNType(m)
    return m * g
    
def hookesLaw(ks, L, Lr): #Checked, Works!
    """
    
    Parameters
    ----------
    ks : Float | Int
        "Spring Stiffness" (N/m)
    L : Vector | Float | Int 
        Vector from base of spring to end of spring (will return Vector)
            OR
        Distance from base of spring to end of spring (will return scalar)
    Lr : Float | Int
        "Relaxed Length" (m) 

    Returns
    -------
    Force done by spring (Vector)

    """
    if type(L) == Vector:    
        checkNType(ks, Lr)
        stretch = L.magnitude()-Lr
        return Vector.scalarMultiply(L.unit(), -ks*stretch) #F = stiffness x stretch in direction of L.
    else:
        checkNType(ks, L, Lr)
        stretch = L - Lr
        return -ks*stretch


def maxForceOfFriction(mu, Fn):
    """
    

    Parameters
    ----------
    mu : Coefficent of friction
        DESCRIPTION.
    Fn : Normal Force
        DESCRIPTION.

    Returns
    -------
    Float

    """
    checkNType(mu, Fn)
    return mu * Fn #Product of coefficent of friction and the normal force

def youngsModulus(Ft, A, dL, Lr):
    """
    

    Parameters
    ----------
    Ft : Force of Tension
        DESCRIPTION.
    A : Area
        DESCRIPTION.
    dL : Stretch
        DESCRIPTION.
    Lr : Relaxed Length
        DESCRIPTION.

    Returns
    -------
    Float
        Young's Modulus.

    """
    
    checkNType(Ft, A, dL, Lr)
    return (Ft / A) / (dL/ Lr)
    
    


"""
if __name__ == "__main__":
    running = True
    print("PCS110 Functions and Constants")
    #while loop with inputs and checking things and stuff
    while running:
        inputString = input()
        try:
            if inputString.lower().strip() == "exit":
                running = False
            exec(inputString)
        except:
            print("Not a valid Input")
"""
    
        
