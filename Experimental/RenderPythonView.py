from paraview.simple import Render, GetActiveView
from functools import reduce

from Tkinter import Tk
from tkFileDialog import askopenfilename

Tk().withdraw() # no full gui
viewfilename = askopenfilename()
print type(viewfilename)
print viewfilename

# viewfilename = "D:/DaveMatthew/UMERgun/Experimental/DensityPlot.py"

#####
# CODE
#####

filehandle = open(viewfilename, 'r')
script = reduce( lambda x,y: x+y,   filehandle.readlines() )

view = GetActiveView()
view.Script = script

source = GetActiveSource()

Show(source, view)