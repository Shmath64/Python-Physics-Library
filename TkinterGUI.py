# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:03:40 2023

@author: 64mda
"""
from tkinter import *
import PCS110Funcs as Pf

root = Tk()
root.title("PCS110 Functions and Constants - Scientific notation (e.g. '7.2e6') is supported")

vector1 = Pf.Vector(0,0,0)

def BPSaveVector1():
    global vector1
    vector1 = Pf.Vector(float(vector1xEntry.get()),float(vector1yEntry.get()),float(vector1zEntry.get()))
    vector1AnsLabel["text"] = f"Vector1 = {str(vector1)}"
    print(vector1)

def BPGamma():
    v = float(gammavEntry.get())
    ans = str(Pf.gamma(v))
    gammaAnsLabel["text"] = ans
    print("Gamma = " + ans)

def BPFGrav(): #Scalar calculation of force of gravity
    m1 = float(fGravm1Entry.get())
    m2 = float(fGravm2Entry.get())
    r = float(fGravrEntry.get())
    ans = str(Pf.forceOfGravity(m1, m2, r))
    fGravAnsLabel["text"] = ans + " N"
    print("Force of Gravity = " + ans)
    
def BPFGravV(): #Vector calculation of force of gravity
    m1 = float(fGravVm1Entry.get())
    m2 = float(fGravVm2Entry.get())
    r = vector1
    ans = str(Pf.forceOfGravity(m1, m2, r)) + " N"
    fGravVAnsLabel["text"] = ans
    print("Force of Gravity = " + ans)
    


#Constants
reservedRows = 1
standardWidth = 10

#LABELS:
nullLabel = Label(root, text="") #Used for spacing

introFuncsLabel = Label(root, text="-Functions-") #Headings for the columns
introInputsLabel = Label(root, text="-Inputs-")
introOutputsLabel = Label(root, text="-Outputs-")
    
vector1FuncLabel = Label(root, text="Vector 1:") #Vector1 labels
vector1xLabel = Label(root, text="x =")
vector1yLabel = Label(root, text="y =")
vector1zLabel = Label(root, text="z =")
vector1AnsLabel = Label(root, text="")

gammaFuncLabel = Label(root, text="Gamma (Lorentz Factor):") #Gamma func labels
gammaAnsLabel = Label(root, text="")
gammavLabel = Label(root, text="v =")

fGravFuncLabel = Label(root, text="Force Of Gravity (Scalar):") #Force of gravity (scalar) labels
fGravAnsLabel = Label(root, text="")
fGravm1Label = Label(root, text="m1 =")
fGravm2Label = Label(root, text="m2 =")
fGravrLabel = Label(root, text="r =")
fGravAnsLabel = Label(root, text="")

fGravVFuncLabel = Label(root, text="Force Of Gravity (Vector):") #Force of gravity (Vector) labels
fGravVAnsLabel = Label(root, text="")
fGravVm1Label = Label(root, text="m1 =")
fGravVm2Label = Label(root, text="m2 =")
fGravVrLabel = Label(root, text="r =")
fGravVAnsLabel = Label(root, text="")


#BUTTONS:
vector1Button = Button(root, text="Save", command=BPSaveVector1)
gammaButton = Button(root, text="RUN", command=BPGamma)
fGravButton = Button(root, text="RUN", command=BPFGrav)
fGravVButton = Button(root, text="RUN", command=BPFGravV)


#Entry:
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

#COLLECTIONS:
#introParts = [introFuncsLabel,nullLabel,introInputsLabel]
vector1Parts = [vector1FuncLabel, vector1xLabel,vector1xEntry, vector1yLabel,vector1yEntry, vector1zLabel,vector1zEntry, vector1Button, vector1AnsLabel]
gammaParts = [gammaFuncLabel, gammavLabel, gammavEntry, gammaButton, gammaAnsLabel]
fGravParts = [fGravFuncLabel, fGravm1Label, fGravm1Entry, fGravm2Label, fGravm2Entry, fGravrLabel, fGravrEntry, fGravButton,fGravAnsLabel]
fGravVParts = [fGravVFuncLabel, fGravVm1Label, fGravVm1Entry, fGravVm2Label, fGravVm2Entry, fGravVrLabel, fGravVrEntry_Label, fGravVButton,fGravVAnsLabel]
allFunctions = [vector1Parts, gammaParts, fGravParts, fGravVParts]

#PLACEMENTS:

'''
gammaFuncLabel.grid(row=gammaRow, column=0)
gammavLabel.grid(row=gammaRow, column=1)
gammavEntry.grid(row=gammaRow, column=2)
gammaButton.grid(row=gammaRow, column=3)
gammaAnsLabel.grid(row=gammaRow,column=4)
'''

introFuncsLabel.grid(row=0,column=0)
introInputsLabel.grid(row=0,column=2)
introOutputsLabel.grid(row=0,column=8)

for i, collection in enumerate(allFunctions):
    for j, part in enumerate(collection):
        part.grid(row=i+reservedRows,column=j)

'''
for i, part in enumerate(gammaParts):
    part.grid(row=gammaRow,column=i)

for i, part in enumerate(fGravParts):
    part.grid(row=fGravRow,column=i)
'''

root.mainloop()
