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

def BPGamma():
    v = float(gammavEntry.get())
    ans = str(Pf.gamma(v))
    gammaAnsLabel["text"] = ans
    print(ans)

def BPFGrav():
    m1 = float(fGravm1Entry.get())
    m2 = float(fGravm2Entry.get())
    r = float(fGravrEntry.get())
    fGravAnsLabel["text"] = str(Pf.forceOfGravity(m1, m2, r)) + " N"
    
def BPSaveVector1():
    global vector1
    vector1 = Pf.Vector(float(vector1xEntry.get()),float(vector1yEntry.get()),float(vector1zEntry.get()))
    vector1AnsLabel["text"] = f"Vector: '{str(vector1)}' Saved!"
    print(vector1)
    


#Constants
gammaRow = 1 #Lorentz Factor
fGravRow = 2 #Force of gravity

standardWidth = 10

#LABELS:

vector1Label = Label(root, text="Vector 1:")    
vector1xLabel = Label(root, text="x =")
vector1yLabel = Label(root, text="y =")
vector1zLabel = Label(root, text="z =")
vector1AnsLabel = Label(root, text="")

gammaFuncLabel = Label(root, text="Gamma (Lorentz Factor):")
gammaAnsLabel = Label(root, text="")
gammavLabel = Label(root, text="v =")

fGravm1Label = Label(root, text="m1 =")
fGravm2Label = Label(root, text="m2 =")
fGravrLabel = Label(root, text="r =")
fGravAnsLabel = Label(root, text="")

fGravFuncLabel = Label(root, text="Force Of Gravity (Scalar):")
fGravAnsLabel = Label(root, text="")

#BUTTONS:
gammaButton = Button(root, text="RUN", command=BPGamma)
fGravButton = Button(root, text="RUN", command=BPFGrav)
vector1Button = Button(root, text="Save", command=BPSaveVector1)

#Entry:
vector1xEntry = Entry(root, width=standardWidth)
vector1yEntry = Entry(root, width=standardWidth)
vector1zEntry = Entry(root, width=standardWidth)

gammavEntry = Entry(root, width=standardWidth)

fGravm1Entry = Entry(root, width=standardWidth)
fGravm2Entry = Entry(root, width=standardWidth)
fGravrEntry = Entry(root, width=standardWidth)

#COLLECTIONS:
vector1Parts = [vector1Label, vector1xLabel,vector1xEntry, vector1yLabel,vector1yEntry, vector1zLabel,vector1zEntry, vector1Button, vector1AnsLabel]
gammaParts = [gammaFuncLabel, gammavLabel, gammavEntry, gammaButton, gammaAnsLabel]
fGravParts = [fGravFuncLabel, fGravm1Label, fGravm1Entry, fGravm2Label, fGravm2Entry, fGravrLabel, fGravrEntry, fGravButton,fGravAnsLabel]

allFunctions = [vector1Parts, gammaParts, fGravParts]

#PLACEMENTS:

'''
gammaFuncLabel.grid(row=gammaRow, column=0)
gammavLabel.grid(row=gammaRow, column=1)
gammavEntry.grid(row=gammaRow, column=2)
gammaButton.grid(row=gammaRow, column=3)
gammaAnsLabel.grid(row=gammaRow,column=4)
'''

for i, collection in enumerate(allFunctions):
    for j, part in enumerate(collection):
        part.grid(row=i,column=j)

'''
for i, part in enumerate(gammaParts):
    part.grid(row=gammaRow,column=i)

for i, part in enumerate(fGravParts):
    part.grid(row=fGravRow,column=i)
'''

root.mainloop()
