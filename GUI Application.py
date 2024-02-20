# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:03:40 2023

@author: 64mda
"""

"""
    In my physics course, PCS110, assignments use a long list of equations and constants. 
I often find myself using the Python IDLE as a calculator: storing relevant constants as variables for 
easy use in calculations and occasionally writing simple functions I’ll need more than once. The goal 
of this project is to create a python module specifically designed for PCS110, as well as a simple 
GUI (made with tkinter) to interact with it.
	This module, named “PCS110Funcs” will have 11 useful constants defined as global variables, 
the default value of these constants will be assigned right away. This module will define a class 
called “Vector”, with 3 instance attributes (x, y, z); useful methods (magnitude, unit); and static 
methods (scalarMultiply, componentsFromAngles). This module will also have its own function for checking 
appropriate value types for its functions and methods (checkNType); as well as several important functions 
in the PCS110 course: (gamma, forceOfGravity, forceOfElectromagnetism, nearEarthForceOfGravity, hookesLaw, 
maxForceOfFriction, youngsModulus, restEnergy, and kinetic Energy) - and docstrings for each one. 
For physics questions that require less (or more) precision of constants (e.g. “let g = 10 N/kg”), 
this module also can read new values for its constants from a a file named "constantsFile.txt"; this acts 
as an "input" file. The program has the ability to overwrite this file with the default constant values.
	The tkinter GUI, named “cps109_a1.py”, provides a very simple interface for interacting with many 
of the functions (and constants) of PCS110Funcs. Any output from calculations performed in the GUI are 
displayed in the GUI itself, saved to a .txt file named “cps109_a1_output.txt”, and sent to a “print” statement.

"""

from tkinter import *
import PCS110Funcs as Pf

root = Tk()
root.title("PCS110 Functions and Constants - Scientific notation (e.g. '7.2e6') is supported")

vector1 = Pf.Vector(0,0,0)

def printOutput(output: str) -> None:
    outputFile = open("OutputLog", "a")
    outputFile.write(output + "\n")
    outputFile.close()
    print(output)

#BP => "Button Pressed"
def BPSaveVector1():
    global vector1
    vector1 = Pf.Vector(float(vector1xEntry.get()),float(vector1yEntry.get()),float(vector1zEntry.get()))
    ans = f"Vector1 = {str(vector1)}"
    vector1AnsLabel["text"] = ans
    printOutput(ans)

def BPGamma():
    v = float(gammavEntry.get())
    ans = str(Pf.gamma(v))
    gammaAnsLabel["text"] = ans
    printOutput("Gamma = " + ans)

def BPFGrav(): #Scalar calculation of force of gravity
    m1 = float(fGravm1Entry.get())
    m2 = float(fGravm2Entry.get())
    r = float(fGravrEntry.get())
    ans = str(Pf.forceOfGravity(m1, m2, r)) + " N"
    fGravAnsLabel["text"] = ans 
    printOutput("Force of Gravity = " + ans)
    
def BPFGravV(): #Vector calculation of force of gravity
    m1 = float(fGravVm1Entry.get())
    m2 = float(fGravVm2Entry.get())
    r = vector1
    ans = str(Pf.forceOfGravity(m1, m2, r)) + " N"
    fGravVAnsLabel["text"] = ans
    printOutput("Force of Gravity = " + ans)

    
def BPFElec(): #Scalar calculation of force of electricity
    q1 = float(fElecq1Entry.get())
    q2 = float(fElecq2Entry.get())
    r = float(fElecrEntry.get())
    ans = str(Pf.forceOfElectromagnetism(q1, q2, r)) + " N"
    fElecAnsLabel["text"] = ans + " N"
    printOutput("Electric Force = " + ans)
    
def BPFElecV(): #Vector calculation of force of electricity
    q1 = float(fElecVq1Entry.get())
    q2 = float(fElecVq2Entry.get())
    r = vector1
    ans = str(Pf.forceOfElectromagnetism(q1, q2, r)) + " N"
    fElecVAnsLabel["text"] = ans
    printOutput("Electric Force = " + ans)
    
def BPUpdateConstants(): #Update constants from file (handled by PCS110Funcs)
    try:
        Pf.updateConstants()
        printOutput("Updated constants from constantsFile.txt")
    except:
        printOutput("Failed to update constants from constantsFile.txt")

def BPRestoreDefaults(): #Restore default constants (handled by PCS110Funcs)
    try:
        Pf.restoreDefaultConstants()
        printOutput("Restored Default constants")
    except:
        printOutput("Failed to restore default constants")


#Constants
reservedRows = 1
standardWidth = 10

#---LABELS---
nullLabel = Label(root, text="") #Used for spacing

#Headings for the columns
introFuncsLabel = Label(root, text="-Functions-") 
introInputsLabel = Label(root, text="-Inputs-")
introOutputsLabel = Label(root, text="-Outputs-")
    
#Vector1 labels
vector1FuncLabel = Label(root, text="Vector 1:") 
vector1xLabel = Label(root, text="x =")
vector1yLabel = Label(root, text="y =")
vector1zLabel = Label(root, text="z =")
vector1AnsLabel = Label(root, text="")

#Gamma func labels
gammaFuncLabel = Label(root, text="Gamma (Lorentz Factor):") 
gammaAnsLabel = Label(root, text="")
gammavLabel = Label(root, text="v =")

#Force of gravity (scalar) labels
fGravFuncLabel = Label(root, text="Force Of Gravity (Scalar):") 
fGravAnsLabel = Label(root, text="")
fGravm1Label = Label(root, text="m1 =")
fGravm2Label = Label(root, text="m2 =")
fGravrLabel = Label(root, text="r =")
fGravAnsLabel = Label(root, text="")

#Force of gravity (Vector) labels
fGravVFuncLabel = Label(root, text="Force Of Gravity (Vector):") 
fGravVAnsLabel = Label(root, text="")
fGravVm1Label = Label(root, text="m1 =")
fGravVm2Label = Label(root, text="m2 =")
fGravVrLabel = Label(root, text="r =")
fGravVAnsLabel = Label(root, text="")

#Force of Electricity (scalar) labels
fElecFuncLabel = Label(root, text="Electric Force (Scalar):") 
fElecAnsLabel = Label(root, text="")
fElecq1Label = Label(root, text="q1 =")
fElecq2Label = Label(root, text="q2 =")
fElecrLabel = Label(root, text="r =")
fElecAnsLabel = Label(root, text="")

#Force of Electricity (Vector) labels
fElecVFuncLabel = Label(root, text="Electric Force (Vector):") 
fElecVAnsLabel = Label(root, text="")
fElecVq1Label = Label(root, text="q1 =")
fElecVq2Label = Label(root, text="q2 =")
fElecVrLabel = Label(root, text="r =")
fElecVAnsLabel = Label(root, text="")


#---BUTTONS---
vector1Button = Button(root, text="Save", command=BPSaveVector1)
gammaButton = Button(root, text="RUN", command=BPGamma)
fGravButton = Button(root, text="RUN", command=BPFGrav)
fGravVButton = Button(root, text="RUN", command=BPFGravV)
fElecButton = Button(root, text="RUN", command=BPFElec)
fElecVButton = Button(root, text="RUN", command=BPFElecV)

restoreDefaultsButton = Button(root, text="Restore Default Constants", command=BPRestoreDefaults)
updateConstantsButton = Button(root, text="Update Constants (from file)", command=BPUpdateConstants)

#---ENTRIES---
vector1xEntry = Entry(root, width=standardWidth) #Vector1 argument entry
vector1yEntry = Entry(root, width=standardWidth)
vector1zEntry = Entry(root, width=standardWidth)

gammavEntry = Entry(root, width=standardWidth) #Gamma argument entry

fGravm1Entry = Entry(root, width=standardWidth) #Force of gravity (scalar) entry
fGravm2Entry = Entry(root, width=standardWidth)
fGravrEntry = Entry(root, width=standardWidth)

fGravVm1Entry = Entry(root, width=standardWidth) #Force of gravity (vector) entry
fGravVm2Entry = Entry(root, width=standardWidth)
fGravVrEntry_Label = Label(root, text="Vector 1") #In entry location, but it is a label because r comes from Vector1

fElecq1Entry = Entry(root, width=standardWidth) #Force of Electricity (scalar) entry
fElecq2Entry = Entry(root, width=standardWidth)
fElecrEntry = Entry(root, width=standardWidth)

fElecVq1Entry = Entry(root, width=standardWidth) #Force of Electricity (vector) entry
fElecVq2Entry = Entry(root, width=standardWidth)
fElecVrEntry_Label = Label(root, text="Vector 1") #In entry location, but it is a label because r comes from Vector1

#---COLLECTIONS---
#introParts = [introFuncsLabel,nullLabel,introInputsLabel]
vector1Parts = [vector1FuncLabel, vector1xLabel,vector1xEntry, vector1yLabel,vector1yEntry, vector1zLabel,vector1zEntry, vector1Button, vector1AnsLabel]
gammaParts = [gammaFuncLabel, gammavLabel, gammavEntry, nullLabel, nullLabel, nullLabel, nullLabel, gammaButton, gammaAnsLabel]
fGravParts = [fGravFuncLabel, fGravm1Label, fGravm1Entry, fGravm2Label, fGravm2Entry, fGravrLabel, fGravrEntry, fGravButton,fGravAnsLabel]
fGravVParts = [fGravVFuncLabel, fGravVm1Label, fGravVm1Entry, fGravVm2Label, fGravVm2Entry, fGravVrLabel, fGravVrEntry_Label, fGravVButton,fGravVAnsLabel]
fElecParts = [fElecFuncLabel, fElecq1Label, fElecq1Entry, fElecq2Label, fElecq2Entry, fElecrLabel, fElecrEntry, fElecButton,fElecAnsLabel]
fElecVParts = [fElecVFuncLabel, fElecVq1Label, fElecVq1Entry, fElecVq2Label, fElecVq2Entry, fElecVrLabel, fElecVrEntry_Label, fElecVButton,fElecVAnsLabel]

allFunctions = [vector1Parts, gammaParts, fGravParts, fGravVParts, fElecParts, fElecVParts]

#PLACEMENTS:

#"Intro" labels; subheadings of the function, input, and output areas
introFuncsLabel.grid(row=0,column=0)
introInputsLabel.grid(row=0,column=2)
introOutputsLabel.grid(row=0,column=8)

numOfRows = len(allFunctions) #total num of functions = numOfRows to display
rowNum = 0 #What row is currently being "placed" onto the GUI

while rowNum < numOfRows: #While there are more rows to display
    for j, part in enumerate(allFunctions[rowNum]): #Display every part of that row
        part.grid(row = rowNum + reservedRows, column=j) #Add to GUI
    rowNum += 1 #Increment rowNum

#Add the "restoreDefaults" and "updateConstants" buttons at the bottom
rowNum += 1
restoreDefaultsButton.grid(row = rowNum, column=0)
rowNum += 1
updateConstantsButton.grid(row = rowNum, column=0)
    
root.mainloop() #tKinter loop 
