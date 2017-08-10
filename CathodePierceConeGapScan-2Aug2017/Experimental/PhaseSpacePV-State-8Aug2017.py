# state file generated using paraview version 5.4.0-RC3

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Line Chart View'
lineChartView1 = CreateView('XYChartView')
lineChartView1.ViewSize = [1546, 568]
lineChartView1.LeftAxisRangeMaximum = 0.0008
lineChartView1.BottomAxisRangeMaximum = 0.004
lineChartView1.RightAxisRangeMaximum = 6.66
lineChartView1.TopAxisRangeMaximum = 6.66

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1546, 568]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.029542085734647117, 7.719965651631355e-06, -5.465000867843628e-06]
renderView1.StereoType = 0
renderView1.CameraPosition = [0.029542085734647117, 7.719965651631355e-06, 0.11637143294791223]
renderView1.CameraFocalPoint = [0.029542085734647117, 7.719965651631355e-06, -5.465000867843628e-06]
renderView1.CameraParallelScale = 0.030120557599096764
renderView1.Background = [0.32, 0.34, 0.43]
renderView1.EnableOSPRay = 1

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
pythonCalculator2.Expression = 'sqrt(vectors[:,1]**2 + vectors[:,2]**2)'
pythonCalculator2.ArrayName = 'Pr'

# create a new 'Slice'
slice1 = Slice(Input=pythonCalculator2)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'scalars'
scalarsLUT = GetColorTransferFunction('scalars')
scalarsLUT.RGBPoints = [80.0, 0.231373, 0.298039, 0.752941, 9399.585474261134, 0.865003, 0.865003, 0.865003, 18719.170948522267, 0.705882, 0.0156863, 0.14902]
scalarsLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'scalars'
scalarsPWF = GetOpacityTransferFunction('scalars')
scalarsPWF.Points = [80.0, 0.0, 0.5, 0.0, 18719.170948522267, 1.0, 0.5, 0.0]
scalarsPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView1'
# ----------------------------------------------------------------

# show data from slice1
slice1Display = Show(slice1, lineChartView1)
# trace defaults for the display properties.
slice1Display.CompositeDataSetIndex = [0]
slice1Display.UseIndexForXAxis = 0
slice1Display.XArrayName = 'R'
slice1Display.SeriesVisibility = ['Pr']
slice1Display.SeriesLabel = ['Pr', 'Pr', 'R', 'R', 'vectors_X', 'vectors_X', 'vectors_Y', 'vectors_Y', 'vectors_Z', 'vectors_Z', 'vectors_Magnitude', 'vectors_Magnitude', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
slice1Display.SeriesColor = ['Pr', '0', '0', '0', 'R', '0.889998', '0.100008', '0.110002', 'vectors_X', '0.220005', '0.489998', '0.719997', 'vectors_Y', '0.300008', '0.689998', '0.289998', 'vectors_Z', '0.6', '0.310002', '0.639994', 'vectors_Magnitude', '1', '0.500008', '0', 'Points_X', '0.650004', '0.340002', '0.160006', 'Points_Y', '0', '0', '0', 'Points_Z', '0.889998', '0.100008', '0.110002', 'Points_Magnitude', '0.220005', '0.489998', '0.719997']
slice1Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pr', '0', 'R', '0', 'vectors_Magnitude', '0', 'vectors_X', '0', 'vectors_Y', '0', 'vectors_Z', '0']
slice1Display.SeriesLabelPrefix = ''
slice1Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'Pr', '0', 'R', '1', 'vectors_Magnitude', '1', 'vectors_X', '1', 'vectors_Y', '1', 'vectors_Z', '1']
slice1Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'Pr', '2', 'R', '2', 'vectors_Magnitude', '2', 'vectors_X', '2', 'vectors_Y', '2', 'vectors_Z', '2']
slice1Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'Pr', '2', 'R', '0', 'vectors_Magnitude', '0', 'vectors_X', '0', 'vectors_Y', '0', 'vectors_Z', '0']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from slice1
slice1Display_1 = Show(slice1, renderView1)
# trace defaults for the display properties.
slice1Display_1.Representation = 'Surface'
slice1Display_1.ColorArrayName = ['CELLS', 'scalars']
slice1Display_1.LookupTable = scalarsLUT
slice1Display_1.OSPRayScaleArray = 'scalars'
slice1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display_1.SelectOrientationVectors = 'vectors'
slice1Display_1.ScaleFactor = 0.000792966689914465
slice1Display_1.SelectScaleArray = 'scalars'
slice1Display_1.GlyphType = 'Arrow'
slice1Display_1.GlyphTableIndexArray = 'scalars'
slice1Display_1.DataAxesGrid = 'GridAxesRepresentation'
slice1Display_1.PolarAxes = 'PolarAxesRepresentation'
slice1Display_1.GaussianRadius = 0.0003964833449572325
slice1Display_1.SetScaleArray = ['POINTS', 'Pr']
slice1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display_1.OpacityArray = ['POINTS', 'Pr']
slice1Display_1.OpacityTransferFunction = 'PiecewiseFunction'

# show color legend
slice1Display_1.SetScalarBarVisibility(renderView1, True)

# setup the color legend parameters for each legend in this view

# get color legend/bar for scalarsLUT in view renderView1
scalarsLUTColorBar = GetScalarBar(scalarsLUT, renderView1)
scalarsLUTColorBar.Title = 'scalars'
scalarsLUTColorBar.ComponentTitle = 'Magnitude'

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(slice1)
# ----------------------------------------------------------------