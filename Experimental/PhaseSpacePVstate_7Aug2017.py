# state file generated using paraview version 5.4.0-RC3

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
spreadSheetView1.ColumnVisibility = ['0', '__vtkIsSelected__', '0']
# uncomment following to set a specific view size
# spreadSheetView1.ViewSize = [400, 400]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML PolyData Reader'
gammaBetavtp = XMLPolyDataReader(FileName=['C:\\Users\\Dave\\UMER group\\UMERgun\\Michelle\\CathodePierceConeGapScan-2Aug2017\\pt05mm_offset\\Result2\\GammaBeta.vtp'])
gammaBetavtp.CellArrayStatus = ['scalars']
gammaBetavtp.PointArrayStatus = ['vectors']

# create a new 'Python Calculator'
pythonCalculator1 = PythonCalculator(Input=gammaBetavtp)
pythonCalculator1.Expression = 'sqrt(inputs[0].Points[:,1]**2 + inputs[0].Points[:,2]**2)'
pythonCalculator1.ArrayName = 'R'

# create a new 'Python Calculator'
pythonCalculator2 = PythonCalculator(Input=pythonCalculator1)
pythonCalculator2.Expression = 'sqrt(vectors[:,1]**2 + vectors[:,2]**2)*9.11e-31*3e8'
pythonCalculator2.ArrayName = 'Pr'

# ----------------------------------------------------------------
# setup the visualization in view 'spreadSheetView1'
# ----------------------------------------------------------------

# show data from pythonCalculator2
pythonCalculator2Display = Show(pythonCalculator2, spreadSheetView1)

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(pythonCalculator2)
# ----------------------------------------------------------------