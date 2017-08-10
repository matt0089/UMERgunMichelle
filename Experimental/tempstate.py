# state file generated using paraview version 5.4.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024L
# uncomment following to set a specific view size
# spreadSheetView1.ViewSize = [400, 400]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'Legacy VTK Reader'
gammaBetavtktxt = LegacyVTKReader(FileNames=['D:\\DaveMatthew\\UMERgun\\Model1\\Mesh3\\Result1\\gammaBeta.vtk.txt'])

# create a new 'Slice'
slice2 = Slice(Input=gammaBetavtktxt)
slice2.SliceType = 'Plane'
slice2.SliceOffsetValues = [0.0]

# create a new 'Programmable Filter'
programmableFilter2 = ProgrammableFilter(Input=slice2)
programmableFilter2.OutputDataSetType = 'vtkTable'
programmableFilter2.Script = 'import numpy as np\nimport paraview\n\n\nmyvectors = inputs[0].GetPointData().GetArray(0)\nmypoints = inputs[0].GetPoints()\n\npy = myvectors[:,1]\nvtk_py = paraview.vtk.vtkFloatArray()\nvtk_py.SetName("Py")\nfor i in py:\n    vtk_py.InsertNextTuple1(float(i))\noutput.AddColumn(vtk_py)\n\npz = myvectors[:,2]\nvtk_pz = paraview.vtk.vtkFloatArray()\nvtk_pz.SetName("Pz")\nfor i in pz:\n    vtk_pz.InsertNextTuple1(float(i))\noutput.AddColumn(vtk_pz)\n\ny = mypoints[:,1]\nvtk_y = paraview.vtk.vtkFloatArray()\nvtk_y.SetName("Y")\nfor i in y:\n    vtk_y.InsertNextTuple1(float(i))\noutput.AddColumn(vtk_y)\n\nz = mypoints[:,2]\nvtk_z = paraview.vtk.vtkFloatArray()\nvtk_z.SetName("Z")\nfor i in z:\n    vtk_z.InsertNextTuple1(float(i))\noutput.AddColumn(vtk_z)'
programmableFilter2.RequestInformationScript = ''
programmableFilter2.RequestUpdateExtentScript = ''
programmableFilter2.PythonPath = ''

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