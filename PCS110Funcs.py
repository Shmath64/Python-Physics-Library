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
consts = {"c":c,"G":G, "g":g,"me":me,"mp":mp,"mn":mn,"EC":EC,"e":e,"Na":Na,"h":h,"relativisticThreshold":relativisticThreshold}

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
    def scalarMultiply(vector: object, scalar: nTypes) -> object:
        """
        

        Parameters
        ----------
        vector : Vector
            Vector to be "scaled".
        scalar : numerical (int | float)
            "Scalar" that will multiply each component of the vector.

        Returns
        -------
        Vector
            The vector after scaling

        """
        checkNType(scalar)
        vector.x *= scalar
        vector.y *= scalar
        vector.z *= scalar
        return vector
        
    
    @staticmethod
    def componentsFromAngles(thetax: nTypes, thetay: nTypes, thetaz: nTypes, usingRads: bool = False) -> object: 
        """

        Parameters
        ----------
        thetax : numerical (int | float)
            Angle from the positive x-axis.
        thetay : numerical (int | float)
            Angle from the positive y-axis.
        thetaz : numerical (int | float)
            Angle from the positive z-axis..
        usingRads : bool, optional
            If true, calculate components with radians, if false, use degrees. The default is False.

        Returns
        -------
        Vector
            The vector defined by each component being the cosine of theta; each component will be in the range [-1, 1].
            This function does not account for impossible combinations of angles (e.g. if all angles are zero, <1,1,1> will be returned)

        """
        if usingRads: return math.cos(thetax), math.cos(thetay), math.cos(thetaz)
        return Vector(math.cos(degToRad(thetax)), math.cos(degToRad(thetay)), math.cos(degToRad(thetaz)))
        

def checkNType(*args) -> bool:
    """


    Parameters
    ----------
    *args : any type, any number of arguments
        Arguments to test if they're 'numerical'; that is, integer or float.

    Raises
    ------
    TypeError
        Raise a type error if ANY of the arguments are not integers or floats.

    Returns
    -------
    bool
        True, if all arguments are 'numerical'.

    """
    
    for arg in args: #For each argument
        if type(arg) not in nTypes: #If not integer or float,
            raise TypeError(f"Must be a numerical value (float or integer)\n{arg} is not a float or an integer")
    return True

def checkNTypeTuple(t: tuple) -> bool:
    """
    

    Parameters
    ----------
    t : Tuple
        Tuple of elements to check if EACH element is 'numerical'; that is, integer or float

    Raises
    ------
    TypeError
        Raise a type error if ANY of the elements in the tuple are not an integer or float.

    Returns
    -------
        True, if all elements are 'numerical.

    """
    return checkNType(*t) #CheckNType for each element in the tuple
            

def gamma(v: nTypes) -> float:
    """
    

    Parameters
    ----------
    v : numerical (int | float)
        Speed (scalar) in m/s.

    Returns
    -------
    float
        The lorentz Factor (gamma) of a particle moving at that speed.
        Equation: Gamma = 1 / math.sqrt(1-(v**2 / c**2))
    """
    checkNType(v)
    return 1 / math.sqrt(1-(v**2 / c**2))


def forceOfGravity(m1: nTypes, m2: nTypes, r: Union[int, float, Vector]) -> Uniton[float, Vector]:
    """
    

    Parameters
    ----------
    m1 : numerical (int | float)
        mass of body 1 (body exerting force) (kg).
    m2 : numerical (int | float)
        mass of body 2 (body on which force is exerted) (kg).
    r : numerical (int | float) OR Vector
        If int | float, the distance between center of masses of bodies one and two (m).
        If Vector, the vector pointing from body 2 to body 1. (m) (Reciprocity theorem)

    Returns
    -------
    float | Vector
        If r is an int | float, the magnitude of the force of gravity. (N)
        If r is a Vector, the force of gravity on body 2 by body 1. (N)
        Uses Newton's law of universal gravitation

    """
    if isinstance(r, Vector):                        #If it's a vector
        fMag = -(G * m1 * m2) / (r.magnitude()**2)   #Get magnitude of force
        return Vector.scalarMultiply(r.unit(), fMag) #Return vector value
    
    elif checkNType(r):                 #If not a vector
        return (G * m1 * m2) / (r**2)  #Return scalar value
    
def forceOfElectromagnetism(q1: nTypes, q2: nTypes, r: Union[int, float, Vector]) -> Union[float, Vector]:
    """
    

    Parameters
    ----------
    q1 : numerical (int | float)
        Charge of body 1 (body exerting force) (C).
    q2 : numerical (int | float)
        Charge of body 2 (body on which force is exerted (C).
    r : TYPE
        If int | float, the distance between bodies one and two (m).
        If Vector, the vector pointing from body 2 to body 1. (Reciprocity theorem) (m).

    Returns
    -------
    float | Vector
        If r is an int | float, the magnitude of the force of electromagnetism. (N)
        If r is a Vector, the force of gravity on body 2 by body 1. (N)
        Uses Newton's law of universal gravitation

    """
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
        
def updateConstantsFromFile(file):
    global g
    lines = file.readlines()
    for line in lines:
        varName = line.split()[0]
        value = line.split()[2]
        print(varName, value)
        globals()[varName] = float(value)
        
            
def updateConstants():
    file = open("constantsFile.txt", "r")
    updateConstantsFromFile(file)
    file.close()

def restoreDefaultConstants():
    open('constantsFile.txt', 'w').close() #Clears content of file
    file = open("constantsFile.txt", "w")
    for c in defaultConstants: #Writes each constant to file
        file.write(f"{c} : {defaultConstants[c]}\n") 
    file.close()
    f = open("constantsFile.txt", "r")
    updateConstantsFromFile(f)
    f.close()
    
    
if __name__ == "__main__":
    try:
        constFile = open("constantsFile.txt", "r")
        updateConstantsFromFile(constFile)
        constFile.close()
    except FileNotFoundError:
        constFile = open("constantsFile.txt", "w")
        restoreDefaultConstants(constFile)
        constFile.close()
        
        