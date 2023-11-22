# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:03:40 2023

@author: 64mda
"""
from tkinter import *
import PCS110Funcs as Pf

root = Tk()
root.title("PCS110 Functions and Constants - Scientific notation (e.g. '7.2e6') is supported")

def BPGamma():
    v = float(gammavEntry.get())
    gammaAnsLabel["text"] = str(Pf.gamma(v))

def BPFGrav():
    pass


#Constants
gammaRow = 1 #Lorentz Factor
fGravRow = 2 #Force of gravity

standardWidth = 10

#LABELS:
    #   titleLabel = Label(root, text="PCS110 Functions and Constants - Scientific notation (e.g. '7.2e6') is supported")

gammaFuncLabel = Label(root, text="Gamma (Lorentz Factor):")
gammaAnsLabel = Label(root, text="")
gammavLabel = Label(root, text="v =")

fGravm1Label = Label(root, text="m1 =")
fGravm2Label = Label(root, text="m2 =")
fGravrLabel = Label(root, text="r =")

fGravFuncLabel = Label(root, text="Force Of Gravity:")
fGravAnsLabel = Label(root, text="")

#BUTTONS:
gammaButton = Button(root, text="RUN", command=BPGamma)
fGravButton = Button(root, text="RUN", command=BPFGrav)

#Entry:
gammavEntry = Entry(root, width=standardWidth)

fGravm1Entry = Entry(root, width=standardWidth)
fGravm2Entry = Entry(root, width=standardWidth)
fGravrEntry = Entry(root, width=standardWidth)

#COLLECTIONS:
gammaParts = [gammaFuncLabel, gammavLabel, gammavEntry, gammaButton, gammaAnsLabel]
fGravParts = [fGravFuncLabel, fGravm1Label, fGravm1Entry, fGravm2Label, fGravm2Entry, fGravrLabel, fGravrEntry]

#PLACEMENTS:

'''
gammaFuncLabel.grid(row=gammaRow, column=0)
gammavLabel.grid(row=gammaRow, column=1)
gammavEntry.grid(row=gammaRow, column=2)
gammaButton.grid(row=gammaRow, column=3)
gammaAnsLabel.grid(row=gammaRow,column=4)
'''
for i, part in enumerate(gammaParts):
    part.grid(row=gammaRow,column=i)

for i, part in enumerate(fGravParts):
    part.grid(row=fGravRow,column=i)


root.mainloop()
