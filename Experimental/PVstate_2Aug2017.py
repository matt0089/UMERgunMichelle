# state file generated using paraview version 5.4.0

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# Create a new 'Line Chart View'
lineChartView2 = CreateView('XYChartView')
lineChartView2.ViewSize = [737, 269]
lineChartView2.ChartTitle = 'Z = ${TIME} [m]'
lineChartView2.LegendPosition = [673, 227]
lineChartView2.LeftAxisTitle = 'Y'
lineChartView2.LeftAxisUseCustomRange = 1
lineChartView2.LeftAxisRangeMinimum = -0.0045
lineChartView2.LeftAxisRangeMaximum = 0.0045
lineChartView2.BottomAxisTitle = 'Z'
lineChartView2.BottomAxisUseCustomRange = 1
lineChartView2.BottomAxisRangeMinimum = -0.0045
lineChartView2.BottomAxisRangeMaximum = 0.0045
lineChartView2.RightAxisRangeMaximum = 6.66
lineChartView2.TopAxisRangeMaximum = 6.66

# Create a new 'Line Chart View'
lineChartView3 = CreateView('XYChartView')
lineChartView3.ViewSize = [736, 269]
lineChartView3.LegendPosition = [667, 227]
lineChartView3.LeftAxisTitle = 'Py [Ns / mc]'
lineChartView3.LeftAxisUseCustomRange = 1
lineChartView3.LeftAxisRangeMinimum = -1.5e-24
lineChartView3.LeftAxisRangeMaximum = 1.5e-24
lineChartView3.BottomAxisTitle = 'Y'
lineChartView3.BottomAxisUseCustomRange = 1
lineChartView3.BottomAxisRangeMinimum = -0.0045
lineChartView3.BottomAxisRangeMaximum = 0.0045
lineChartView3.RightAxisRangeMaximum = 6.66
lineChartView3.TopAxisRangeMaximum = 6.66

# Create a new 'Line Chart View'
lineChartView4 = CreateView('XYChartView')
lineChartView4.ViewSize = [737, 269]
lineChartView4.LegendPosition = [670, 227]
lineChartView4.LeftAxisTitle = 'Pz [Ns/mc]'
lineChartView4.LeftAxisUseCustomRange = 1
lineChartView4.LeftAxisRangeMinimum = -1.5e-24
lineChartView4.LeftAxisRangeMaximum = 1.5e-24
lineChartView4.BottomAxisTitle = 'Z'
lineChartView4.BottomAxisUseCustomRange = 1
lineChartView4.BottomAxisRangeMinimum = -0.0045
lineChartView4.BottomAxisRangeMaximum = 0.0045
lineChartView4.RightAxisRangeMaximum = 6.66
lineChartView4.TopAxisRangeMaximum = 6.66

# Create a new 'Line Chart View'
lineChartView5 = CreateView('XYChartView')
lineChartView5.ViewSize = [736, 269]
lineChartView5.LegendPosition = [667, 227]
lineChartView5.LeftAxisTitle = 'Py [Ns/mc]'
lineChartView5.LeftAxisUseCustomRange = 1
lineChartView5.LeftAxisRangeMinimum = -1.5e-24
lineChartView5.LeftAxisRangeMaximum = 1.5e-24
lineChartView5.BottomAxisTitle = 'Pz [Ns/mc]'
lineChartView5.BottomAxisUseCustomRange = 1
lineChartView5.BottomAxisRangeMinimum = -1.5e-24
lineChartView5.BottomAxisRangeMaximum = 1.5e-24
lineChartView5.RightAxisUseCustomRange = 1
lineChartView5.RightAxisRangeMaximum = 6.66
lineChartView5.TopAxisUseCustomRange = 1
lineChartView5.TopAxisRangeMaximum = 6.66

# Create a new 'Python View'
pythonView1 = CreateView('PythonView')
pythonView1.ViewSize = [1482, 568]
pythonView1.Script = 'import matplotlib as mpl\nimport numpy as np\n\nfrom paraview import python_view\n\n\ndef setup_data(view):\n    view.EnableAllAttributeArrays()\n\ndef render(view, height, width):\n    modheight = height - 1000\n    modwidth = width  + 400  # this fixes image scale\n    \n    figure = python_view.matplotlib_figure(modwidth, modheight)\n    ax = figure.add_subplot(1,1,1)\n\n    dataObject = view.GetVisibleDataObjectForRendering(0)\n    \n    #print repr(dataObject.GetPoints().GetData())\n    if not dataObject: return\n    \n    x = dataObject.GetPoints().GetData()\n    #print repr(x)\n    \n    from paraview.numpy_support import vtk_to_numpy\n    np_x = vtk_to_numpy(x)\n    #print repr(np_x)\n    \n    # Change colormap with cmap = mpl.cm.get_cmap(<mapname>)\n    mplPolyCollection = ax.scatter(np_x[:,2], np_x[:,1],  s=.2, c=\'#2f7cef\')\n    # print mplPolyCollection.get_clim()\n    # print(doop)    \n\n    #print repr(mplPolyCollection)\n    ax.minorticks_on()\n    ax.set_title("Cross Section")\n    ax.set_xlabel("Z [m]")\n    ax.set_ylabel("Y [m]")\n    ax.set_xlim((-.0045, .0045))\n    ax.set_ylim((-.0045, .0045))\n    \n    \n    return python_view.figure_to_image(figure)'

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1482, 568]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [0.029492083282093517, 2.0973384380340576e-06, -1.4975666999816895e-06]
renderView1.StereoType = 0
renderView1.CameraPosition = [0.023332022462916834, 0.015297873275545533, 0.0758849336032226]
renderView1.CameraFocalPoint = [0.02949208328209354, 2.097338438034391e-06, -1.497566699978239e-06]
renderView1.CameraViewUp = [-0.02614207986596112, 0.9795370437981681, -0.19955894238902816]
renderView1.CameraParallelScale = 0.11174983670864022
renderView1.Background = [0.32, 0.34, 0.43]

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = 'vtkOriginalIndices'
spreadSheetView1.BlockSize = 1024L
# uncomment following to set a specific view size
# spreadSheetView1.ViewSize = [400, 400]

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML Unstructured Grid Reader'
potentialvtu = XMLUnstructuredGridReader(FileName=['D:\\DaveMatthew\\UMERgun\\CathodePierceConeGapScan-2Aug2017\\pt15mm_offset\\Result1\\Potential.vtu'])
potentialvtu.CellArrayStatus = ['scalars']
potentialvtu.PointArrayStatus = ['scalars']

# create a new 'XML PolyData Reader'
gammaBetavtp = XMLPolyDataReader(FileName=['D:\\DaveMatthew\\UMERgun\\CathodePierceConeGapScan-2Aug2017\\pt15mm_offset\\Result1\\GammaBeta.vtp'])
gammaBetavtp.CellArrayStatus = ['scalars']
gammaBetavtp.PointArrayStatus = ['vectors']

# create a new 'Slice'
slice2 = Slice(Input=gammaBetavtp)
slice2.SliceType = 'Plane'
slice2.SliceOffsetValues = [0.0591]

# create a new 'Programmable Filter'
programmableFilter1 = ProgrammableFilter(Input=slice2)
programmableFilter1.OutputDataSetType = 'vtkTable'
programmableFilter1.Script = 'import numpy as np\nimport paraview\n\nm = 9.11e-31\nc = 3e8\n\nmyvectors = inputs[0].GetPointData().GetArray(0)\nmypoints = inputs[0].GetPoints()\n\npy = myvectors[:,1]\nvtk_py = paraview.vtk.vtkFloatArray()\nvtk_py.SetName("Py")\nfor i in py:\n    vtk_py.InsertNextTuple1(float(i*m*c))\noutput.AddColumn(vtk_py)\n\npz = myvectors[:,2]\nvtk_pz = paraview.vtk.vtkFloatArray()\nvtk_pz.SetName("Pz")\nfor i in pz:\n    vtk_pz.InsertNextTuple1(float(i*m*c))\noutput.AddColumn(vtk_pz)\n\ny = mypoints[:,1]\nvtk_y = paraview.vtk.vtkFloatArray()\nvtk_y.SetName("Y")\nfor i in y:\n    vtk_y.InsertNextTuple1(float(i))\noutput.AddColumn(vtk_y)\n\nz = mypoints[:,2]\nvtk_z = paraview.vtk.vtkFloatArray()\nvtk_z.SetName("Z")\nfor i in z:\n    vtk_z.InsertNextTuple1(float(i))\noutput.AddColumn(vtk_z)'
programmableFilter1.RequestInformationScript = ''
programmableFilter1.RequestUpdateExtentScript = ''
programmableFilter1.PythonPath = ''

# create a new 'Slice'
slice1 = Slice(Input=potentialvtu)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get color transfer function/color map for 'scalars'
scalarsLUT = GetColorTransferFunction('scalars')
scalarsLUT.RGBPoints = [-0.20201799273490906, 0.231373, 0.298039, 0.752941, 4999.898991003633, 0.865003, 0.865003, 0.865003, 10000.0, 0.705882, 0.0156863, 0.14902]
scalarsLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'scalars'
scalarsPWF = GetOpacityTransferFunction('scalars')
scalarsPWF.Points = [-0.20201799273490906, 0.0, 0.5, 0.0, 10000.0, 1.0, 0.5, 0.0]
scalarsPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView2'
# ----------------------------------------------------------------

# show data from programmableFilter1
programmableFilter1Display = Show(programmableFilter1, lineChartView2)
# trace defaults for the display properties.
programmableFilter1Display.CompositeDataSetIndex = [0]
programmableFilter1Display.AttributeType = 'Row Data'
programmableFilter1Display.UseIndexForXAxis = 0
programmableFilter1Display.XArrayName = 'Z'
programmableFilter1Display.SeriesVisibility = ['Y']
programmableFilter1Display.SeriesLabel = ['Py', 'Py', 'Pz', 'Pz', 'Y', 'Y', 'Z', 'Z']
programmableFilter1Display.SeriesColor = ['Py', '0', '0', '0', 'Pz', '0.889998', '0.100008', '0.110002', 'Y', '0.220005', '0.489998', '0.719997', 'Z', '0.300008', '0.689998', '0.289998']
programmableFilter1Display.SeriesPlotCorner = ['Py', '0', 'Pz', '0', 'Y', '0', 'Z', '0']
programmableFilter1Display.SeriesLabelPrefix = ''
programmableFilter1Display.SeriesLineStyle = ['Py', '1', 'Pz', '1', 'Y', '0', 'Z', '1']
programmableFilter1Display.SeriesLineThickness = ['Py', '2', 'Pz', '2', 'Y', '1', 'Z', '2']
programmableFilter1Display.SeriesMarkerStyle = ['Py', '0', 'Pz', '0', 'Y', '4', 'Z', '0']

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView3'
# ----------------------------------------------------------------

# show data from programmableFilter1
programmableFilter1Display_1 = Show(programmableFilter1, lineChartView3)
# trace defaults for the display properties.
programmableFilter1Display_1.CompositeDataSetIndex = [0]
programmableFilter1Display_1.AttributeType = 'Row Data'
programmableFilter1Display_1.UseIndexForXAxis = 0
programmableFilter1Display_1.XArrayName = 'Y'
programmableFilter1Display_1.SeriesVisibility = ['Py']
programmableFilter1Display_1.SeriesLabel = ['Py', 'Py', 'Pz', 'Pz', 'Y', 'Y', 'Z', 'Z']
programmableFilter1Display_1.SeriesColor = ['Py', '0', '0', '0', 'Pz', '0.889998', '0.100008', '0.110002', 'Y', '0.220005', '0.489998', '0.719997', 'Z', '0.300008', '0.689998', '0.289998']
programmableFilter1Display_1.SeriesPlotCorner = ['Py', '0', 'Pz', '0', 'Y', '0', 'Z', '0']
programmableFilter1Display_1.SeriesLabelPrefix = ''
programmableFilter1Display_1.SeriesLineStyle = ['Py', '0', 'Pz', '1', 'Y', '0', 'Z', '1']
programmableFilter1Display_1.SeriesLineThickness = ['Py', '2', 'Pz', '2', 'Y', '1', 'Z', '2']
programmableFilter1Display_1.SeriesMarkerStyle = ['Py', '4', 'Pz', '0', 'Y', '4', 'Z', '0']

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView4'
# ----------------------------------------------------------------

# show data from programmableFilter1
programmableFilter1Display_2 = Show(programmableFilter1, lineChartView4)
# trace defaults for the display properties.
programmableFilter1Display_2.CompositeDataSetIndex = [0]
programmableFilter1Display_2.AttributeType = 'Row Data'
programmableFilter1Display_2.UseIndexForXAxis = 0
programmableFilter1Display_2.XArrayName = 'Z'
programmableFilter1Display_2.SeriesVisibility = ['Pz']
programmableFilter1Display_2.SeriesLabel = ['Py', 'Py', 'Pz', 'Pz', 'Y', 'Y', 'Z', 'Z']
programmableFilter1Display_2.SeriesColor = ['Py', '0', '0', '0', 'Pz', '0.889998', '0.100008', '0.110002', 'Y', '0.220005', '0.489998', '0.719997', 'Z', '0.300008', '0.689998', '0.289998']
programmableFilter1Display_2.SeriesPlotCorner = ['Py', '0', 'Pz', '0', 'Y', '0', 'Z', '0']
programmableFilter1Display_2.SeriesLabelPrefix = ''
programmableFilter1Display_2.SeriesLineStyle = ['Py', '1', 'Pz', '0', 'Y', '1', 'Z', '1']
programmableFilter1Display_2.SeriesLineThickness = ['Py', '2', 'Pz', '2', 'Y', '2', 'Z', '2']
programmableFilter1Display_2.SeriesMarkerStyle = ['Py', '0', 'Pz', '4', 'Y', '0', 'Z', '0']

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView5'
# ----------------------------------------------------------------

# show data from programmableFilter1
programmableFilter1Display_3 = Show(programmableFilter1, lineChartView5)
# trace defaults for the display properties.
programmableFilter1Display_3.CompositeDataSetIndex = [0]
programmableFilter1Display_3.AttributeType = 'Row Data'
programmableFilter1Display_3.UseIndexForXAxis = 0
programmableFilter1Display_3.XArrayName = 'Pz'
programmableFilter1Display_3.SeriesVisibility = ['Py']
programmableFilter1Display_3.SeriesLabel = ['Py', 'Py', 'Pz', 'Pz', 'Y', 'Y', 'Z', 'Z']
programmableFilter1Display_3.SeriesColor = ['Py', '0', '0', '0', 'Pz', '0.889998', '0.100008', '0.110002', 'Y', '0.220005', '0.489998', '0.719997', 'Z', '0.300008', '0.689998', '0.289998']
programmableFilter1Display_3.SeriesPlotCorner = ['Py', '0', 'Pz', '0', 'Y', '0', 'Z', '0']
programmableFilter1Display_3.SeriesLabelPrefix = ''
programmableFilter1Display_3.SeriesLineStyle = ['Py', '0', 'Pz', '1', 'Y', '0', 'Z', '1']
programmableFilter1Display_3.SeriesLineThickness = ['Py', '2', 'Pz', '2', 'Y', '2', 'Z', '2']
programmableFilter1Display_3.SeriesMarkerStyle = ['Py', '4', 'Pz', '0', 'Y', '4', 'Z', '0']

# ----------------------------------------------------------------
# setup the visualization in view 'pythonView1'
# ----------------------------------------------------------------

# show data from slice2
slice2Display = Show(slice2, pythonView1)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from gammaBetavtp
gammaBetavtpDisplay = Show(gammaBetavtp, renderView1)
# trace defaults for the display properties.
gammaBetavtpDisplay.Representation = 'Surface'
gammaBetavtpDisplay.AmbientColor = [1.0, 1.0, 0.0]
gammaBetavtpDisplay.ColorArrayName = ['CELLS', 'scalars']
gammaBetavtpDisplay.DiffuseColor = [1.0, 1.0, 0.0]
gammaBetavtpDisplay.LookupTable = scalarsLUT
gammaBetavtpDisplay.OSPRayScaleArray = 'scalars'
gammaBetavtpDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
gammaBetavtpDisplay.SelectOrientationVectors = 'vectors'
gammaBetavtpDisplay.ScaleFactor = 0.005928562057670206
gammaBetavtpDisplay.SelectScaleArray = 'scalars'
gammaBetavtpDisplay.GlyphType = 'Arrow'
gammaBetavtpDisplay.GlyphTableIndexArray = 'scalars'
gammaBetavtpDisplay.DataAxesGrid = 'GridAxesRepresentation'
gammaBetavtpDisplay.PolarAxes = 'PolarAxesRepresentation'
gammaBetavtpDisplay.GaussianRadius = 0.002964281028835103
gammaBetavtpDisplay.SetScaleArray = [None, '']
gammaBetavtpDisplay.ScaleTransferFunction = 'PiecewiseFunction'
gammaBetavtpDisplay.OpacityArray = [None, '']
gammaBetavtpDisplay.OpacityTransferFunction = 'PiecewiseFunction'

# show color legend
gammaBetavtpDisplay.SetScalarBarVisibility(renderView1, True)

# show data from slice1
slice1Display = Show(slice1, renderView1)
# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.AmbientColor = [1.0, 1.0, 0.0]
slice1Display.ColorArrayName = ['POINTS', 'scalars']
slice1Display.DiffuseColor = [1.0, 1.0, 0.0]
slice1Display.LookupTable = scalarsLUT
slice1Display.OSPRayScaleArray = 'scalars'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.ScaleFactor = 0.015237434953451158
slice1Display.SelectScaleArray = 'scalars'
slice1Display.GlyphType = 'Arrow'
slice1Display.GlyphTableIndexArray = 'scalars'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.PolarAxes = 'PolarAxesRepresentation'
slice1Display.GaussianRadius = 0.007618717476725579
slice1Display.SetScaleArray = ['POINTS', 'scalars']
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityArray = ['POINTS', 'scalars']
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'

# show color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# show data from slice2
slice2Display_1 = Show(slice2, renderView1)
# trace defaults for the display properties.
slice2Display_1.Representation = 'Surface'
slice2Display_1.AmbientColor = [1.0, 1.0, 0.0]
slice2Display_1.ColorArrayName = ['POINTS', '']
slice2Display_1.DiffuseColor = [1.0, 1.0, 0.0]
slice2Display_1.OSPRayScaleArray = 'scalars'
slice2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display_1.SelectOrientationVectors = 'None'
slice2Display_1.ScaleFactor = 0.0007755372207611799
slice2Display_1.SelectScaleArray = 'None'
slice2Display_1.GlyphType = 'Arrow'
slice2Display_1.GlyphTableIndexArray = 'None'
slice2Display_1.DataAxesGrid = 'GridAxesRepresentation'
slice2Display_1.PolarAxes = 'PolarAxesRepresentation'
slice2Display_1.GaussianRadius = 0.00038776861038058996
slice2Display_1.SetScaleArray = [None, '']
slice2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display_1.OpacityArray = [None, '']
slice2Display_1.OpacityTransferFunction = 'PiecewiseFunction'

# setup the color legend parameters for each legend in this view

# get color legend/bar for scalarsLUT in view renderView1
scalarsLUTColorBar = GetScalarBar(scalarsLUT, renderView1)
scalarsLUTColorBar.WindowLocation = 'UpperRightCorner'
scalarsLUTColorBar.Title = 'scalars'
scalarsLUTColorBar.ComponentTitle = 'Magnitude'

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(programmableFilter1)
# ----------------------------------------------------------------