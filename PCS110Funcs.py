# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 08:05:04 2023

@author: 64mda
"""
#PCS110 Functions and Constants
import math
from typing import Union

#CONSTANTS (default values - can be overwritten by constants.txt)
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
relativisticThreshold = 0.1 #At what velocity should relativistic effects be considered (in terms of c)
defaultConstants ={"c":c,"G":G, "g":g,"me":me,"mp":mp,"mn":mn,"EC":EC,"e":e,"Na":Na,"h":h,"relativisticThreshold":relativisticThreshold}

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
    
def forceOfElectromagnetism(q1, q2, r) -> Union[Vector, float]:
    if isinstance(r, Vector):                        #If it's a vector
        fMag = -(EC * q1 * q2) / (r.magnitude()**2)   #Get magnitude of force
        return Vector.scalarMultiply(r.unit(), fMag) #Return vector value
    
    elif checkNType(r):                 #If not a vector
        return -(EC * q1 * q2) / (r**2)  #Return scalar value

    
def nearEarthForceOfGravity(m): #Simply mg for near-Earth approximations
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

def youngsModulus(Ft, A, dL, Lr): #Checked, Works!
    """
    

    Parameters
    ----------
    Ft : Force of Tension (N)
        DESCRIPTION.
    A : Area (m**2)
        DESCRIPTION.
    dL : Stretch (m)
        DESCRIPTION.
    Lr : Relaxed Length (m)
        DESCRIPTION.

    Returns
    -------
    Float (N/m**2) or Pa
        Young's Modulus;
        The "stretchiness" of a material regardless of size/shape
        Always a pull force; "You can't push a rope"

    """
    
    checkNType(Ft, A, dL, Lr)
    return (Ft / A) / (dL / Lr) #Formula: stress (Ft/A) / strain (dL/Lr)
    
def restEnergy(m): #mc**2
    checkNType(m)
    return m * (c**2)

def kineticEnergy(v, m): #gamma(mc**2) - mc**2 OR 1/2 mv**2
    checkNType(v, m)
    #The "relativisticThreshold" determines which equation for kinetic energy should be used
    if v >= relativisticThreshold*c:
        return gamma(v)*restEnergy(m) - restEnergy(m)
    else:
        return 0.5 * m * (v**2)


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
    
def restoreDefaultConstants():
    open('constantsFile.txt', 'w').close() #Clears content of file
    file = open("constantsFile.txt", "w")
    for c in defaultConstants: #Writes each constant to file
        file.write(f"{c} : {defaultConstants[c]}\n")
        
    file.close()
    f = open("constantsFile.txt", "r")
    updateConstantsFromFile(f)
        
def updateConstantsFromFile(file):
    fLines = file.readlines()
    for line in fLines: #For each line
        item = line.split()[0] 
        value = line.split()[2]
        print(item, value)
        globals()[item] = float(value) #Set the variable of the line to the value of the line.

if __name__ == "__main__":
    try:
        f = open("constantsFile.txt", "r")
        updateConstantsFromFile(f)
    except FileNotFoundError:
        f = open("constantsFile.txt", "w")
        restoreDefaultConstants()
    f.close()
        
        
