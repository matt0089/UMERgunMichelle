# state file generated using paraview version 5.4.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------
from timeit import default_timer
from time import sleep
#import pdb

#### import the simple module from the paraview
from paraview.simple import *

# ----------------------------------------------------------------
# Select file to open
# ----------------------------------------------------------------
#pdb.set_trace()
from win32gui import GetOpenFileNameW, GetSaveFileNameW
(openFilename,_,_) = GetOpenFileNameW()

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Legacy VTK Reader'
print "\n opening gammaBeta...\n"
start_time = default_timer()
gammaBetavtktxt = LegacyVTKReader(FileNames=[openFilename])

next_time = default_timer()
print "1. Took " + str(next_time - start_time) + " seconds.\n"
start_time = next_time

# get slice bounds
print "Fetching"
gammaBetaPolyData = servermanager.Fetch(gammaBetavtktxt)
(xmin,xmax,_,_,_,_) = gammaBetaPolyData.GetPoints().GetBounds()
print type(xmax)
print xmax
xmax = xmax-.00005

next_time = default_timer()
print "2. Took " + str(next_time - start_time) + " seconds.\n"
start_time = next_time

# create a new 'Slice'
print "creating slice"
slice2 = Slice(Input=gammaBetavtktxt)
slice2.SliceType = 'Plane'
slice2.SliceOffsetValues = [xmax]

# create a new 'Programmable Filter'
print "creating table data from poly data"
#pdb.set_trace()
programmableFilter2 = ProgrammableFilter(Input=slice2)

next_time = default_timer()
print "3. Took " + str(next_time - start_time) + " seconds.\n"
start_time = next_time

programmableFilter2.OutputDataSetType = 'vtkTable'

next_time = default_timer()
print "3. Took " + str(next_time - start_time) + " seconds.\n"
start_time = next_time

programmableFilter2.Script = '''
import numpy as np
import paraview

myvectors = inputs[0].GetPointData().GetArray(0)
mypoints = inputs[0].GetPoints()

py = myvectors[:,1]
vtk_py = paraview.vtk.vtkFloatArray()
vtk_py.SetName("Py")
for i in py:
    vtk_py.InsertNextTuple1(float(i))
output.AddColumn(vtk_py)

pz = myvectors[:,2]
vtk_pz = paraview.vtk.vtkFloatArray()
vtk_pz.SetName("Pz")
for i in pz:
    vtk_pz.InsertNextTuple1(float(i))
output.AddColumn(vtk_pz)

y = mypoints[:,1]
vtk_y = paraview.vtk.vtkFloatArray()
vtk_y.SetName("Y")
for i in y:
    vtk_y.InsertNextTuple1(float(i))
output.AddColumn(vtk_y)

z = mypoints[:,2]
vtk_z = paraview.vtk.vtkFloatArray()
vtk_z.SetName("Z")
for i in z:
    vtk_z.InsertNextTuple1(float(i))
output.AddColumn(vtk_z)
'''

next_time = default_timer()
print "2. Took " + str(next_time - start_time) + " seconds.\n"
start_time = next_time

print "display stuff 1"
programmableFilter2.RequestInformationScript = ''
programmableFilter2.RequestUpdateExtentScript = ''
programmableFilter2.PythonPath = ''

# View data
print "Creating view"
lineChartView1 = CreateView('XYChartView')
programmableFilter2Display = Show(programmableFilter2, lineChartView1)
programmableFilter2Display.UseIndexForXAxis = 0
programmableFilter2Display.XArrayName = 'Z'
programmableFilter2Display.SeriesVisibility = ['Y']
programmableFilter2Display.SeriesLineStyle = ['Py', '1', 'Pz', '1', 'Y', '0', 'Z', '1']
programmableFilter2Display.SeriesMarkerStyle = ['Py', '0', 'Pz', '0', 'Y', '2', 'Z', '0']
print "Rendering"
Render()
# export data
print "saving data\n"
sleep(5)
print "dialog\n"
(saveFilename,_,_) = GetSaveFileNameW()
sleep(5)
print "Saving\n"
SaveData(saveFilename, proxy=programmableFilter2, UseScientificNotation=1)
sleep(20)
print "done\n"

# export row numbers and visibility stuff.  prob not useful.
#SetActiveSource(programmableFilter2)
#spreadSheetView1 = GetActiveViewOrCreate('SpreadSheetView')
#ExportView('D:\DaveMatthew\UMERgun\Experimental\temp.csv', view=spreadSheetView1)

""" visualize data
# ----------------------------------------------------------------
# setup the visualization in view 'spreadSheetView1'
# ----------------------------------------------------------------

# show data from programmableFilter2
programmableFilter2Display = Show(programmableFilter2, spreadSheetView1)
# trace defaults for the display properties.
programmableFilter2Display.FieldAssociation = 'Row Data'

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(programmableFilter2)
# ----------------------------------------------------------------
"""