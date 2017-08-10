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
lineChartView1.ViewSize = [769, 291]
lineChartView1.LegendPosition = [667, 249]
lineChartView1.LeftAxisUseCustomRange = 1
lineChartView1.LeftAxisRangeMinimum = -0.0045
lineChartView1.LeftAxisRangeMaximum = 0.0045
lineChartView1.BottomAxisUseCustomRange = 1
lineChartView1.BottomAxisRangeMinimum = -0.0045
lineChartView1.BottomAxisRangeMaximum = 0.0045
lineChartView1.RightAxisUseCustomRange = 1
lineChartView1.RightAxisRangeMaximum = 6.66
lineChartView1.TopAxisUseCustomRange = 1
lineChartView1.TopAxisRangeMaximum = 6.66

# Create a new 'Line Chart View'
lineChartView2 = CreateView('XYChartView')
lineChartView2.ViewSize = [768, 291]
lineChartView2.LegendPosition = [666, 249]
lineChartView2.LeftAxisUseCustomRange = 1
lineChartView2.LeftAxisRangeMinimum = -0.0045
lineChartView2.LeftAxisRangeMaximum = 0.0045
lineChartView2.BottomAxisUseCustomRange = 1
lineChartView2.BottomAxisRangeMinimum = -0.0045
lineChartView2.BottomAxisRangeMaximum = 0.0045
lineChartView2.RightAxisUseCustomRange = 1
lineChartView2.RightAxisRangeMaximum = 6.66
lineChartView2.TopAxisUseCustomRange = 1
lineChartView2.TopAxisRangeMaximum = 6.66

# Create a new 'Line Chart View'
lineChartView3 = CreateView('XYChartView')
lineChartView3.ViewSize = [769, 290]
lineChartView3.LegendPosition = [656, 248]
lineChartView3.LeftAxisUseCustomRange = 1
lineChartView3.LeftAxisRangeMinimum = -0.0045
lineChartView3.LeftAxisRangeMaximum = 0.0045
lineChartView3.BottomAxisUseCustomRange = 1
lineChartView3.BottomAxisRangeMinimum = -0.0045
lineChartView3.BottomAxisRangeMaximum = 0.0045
lineChartView3.RightAxisUseCustomRange = 1
lineChartView3.RightAxisRangeMaximum = 6.66
lineChartView3.TopAxisUseCustomRange = 1
lineChartView3.TopAxisRangeMaximum = 6.66

# Create a new 'Line Chart View'
lineChartView4 = CreateView('XYChartView')
lineChartView4.ViewSize = [768, 290]
lineChartView4.LegendPosition = [655, 248]
lineChartView4.LeftAxisUseCustomRange = 1
lineChartView4.LeftAxisRangeMinimum = -0.0045
lineChartView4.LeftAxisRangeMaximum = 0.0045
lineChartView4.BottomAxisUseCustomRange = 1
lineChartView4.BottomAxisRangeMinimum = -0.0045
lineChartView4.BottomAxisRangeMaximum = 0.0045
lineChartView4.RightAxisUseCustomRange = 1
lineChartView4.RightAxisRangeMaximum = 6.66
lineChartView4.TopAxisUseCustomRange = 1
lineChartView4.TopAxisRangeMaximum = 6.66

# Create a new 'Plot Matrix View'
plotMatrixView1 = CreateView('PlotMatrixView')
plotMatrixView1.ViewSize = [1546, 611]

# Create a new 'Python View'
pythonView1 = CreateView('PythonView')
pythonView1.ViewSize = [1546, 611]
pythonView1.Script = 'import matplotlib as mpl\nimport numpy as np\n\nfrom paraview import python_view\n\n\ndef setup_data(view):\n    view.EnableAllAttributeArrays()\n\ndef render(view, height, width):\n    modheight = height  -800\n    modwidth = width  +800  # this fixes image scale\n    \n    figure = python_view.matplotlib_figure(modwidth, modheight)\n    ax = figure.add_subplot(1,1,1)\n\n    dataObject = view.GetVisibleDataObjectForRendering(0)\n    \n    #print repr(dataObject.GetPoints().GetData())\n    if not dataObject: return\n    \n    x = dataObject.GetPoints().GetData()\n    #print repr(x)\n    \n    from paraview.numpy_support import vtk_to_numpy\n    np_x = vtk_to_numpy(x)\n    #print repr(np_x)\n    \n    # Change colormap with cmap = mpl.cm.get_cmap(<mapname>)\n    mplPolyCollection = ax.scatter(np_x[:,2], np_x[:,1],  s=.2, c=\'#2f7cef\')\n    # print mplPolyCollection.get_clim()\n    # print(doop)    \n\n    #print repr(mplPolyCollection)\n    ax.minorticks_on()\n    ax.set_title("Cross Section")\n    ax.set_xlabel("Z [m]")\n    ax.set_ylabel("Y [m]")\n    ax.set_xlim((-.0045, .0045))\n    ax.set_ylim((-.0045, .0045))\n    \n    \n    return python_view.figure_to_image(figure)'

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'XML PolyData Reader'
gammaBetavtp = XMLPolyDataReader(FileName=['C:\\Users\\Dave\\UMER group\\UMERgun\\Michelle\\CathodePierceConeGapScan-2Aug2017\\pt05mm_offset\\Result2\\GammaBeta.vtp'])
gammaBetavtp.CellArrayStatus = ['scalars']
gammaBetavtp.PointArrayStatus = ['vectors']

# create a new 'Slice'
slice1 = Slice(Input=gammaBetavtp)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.01666923076923077]

# create a new 'Scatter Plot'
scatterPlot1 = ScatterPlot(Input=slice1)

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView1'
# ----------------------------------------------------------------

# show data from scatterPlot1
scatterPlot1Display = Show(scatterPlot1, lineChartView1)
# trace defaults for the display properties.
scatterPlot1Display.CompositeDataSetIndex = [0]
scatterPlot1Display.UseIndexForXAxis = 0
scatterPlot1Display.XArrayName = 'Points_Z'
scatterPlot1Display.SeriesVisibility = ['Points_Y']
scatterPlot1Display.SeriesLabel = ['vectors_X', 'vectors_X', 'vectors_Y', 'vectors_Y', 'vectors_Z', 'vectors_Z', 'vectors_Magnitude', 'vectors_Magnitude', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
scatterPlot1Display.SeriesColor = ['vectors_X', '0', '0', '0', 'vectors_Y', '0.889998', '0.100008', '0.110002', 'vectors_Z', '0.220005', '0.489998', '0.719997', 'vectors_Magnitude', '0.300008', '0.689998', '0.289998', 'Points_X', '0.6', '0.310002', '0.639994', 'Points_Y', '1', '0.500008', '0', 'Points_Z', '0.650004', '0.340002', '0.160006', 'Points_Magnitude', '0', '0', '0']
scatterPlot1Display.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'vectors_Magnitude', '0', 'vectors_X', '0', 'vectors_Y', '0', 'vectors_Z', '0']
scatterPlot1Display.SeriesLabelPrefix = ''
scatterPlot1Display.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '0', 'Points_Z', '1', 'vectors_Magnitude', '1', 'vectors_X', '1', 'vectors_Y', '1', 'vectors_Z', '1']
scatterPlot1Display.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'vectors_Magnitude', '2', 'vectors_X', '2', 'vectors_Y', '2', 'vectors_Z', '2']
scatterPlot1Display.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '1', 'Points_Z', '0', 'vectors_Magnitude', '0', 'vectors_X', '0', 'vectors_Y', '0', 'vectors_Z', '0']

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView2'
# ----------------------------------------------------------------

# show data from scatterPlot1
scatterPlot1Display_1 = Show(scatterPlot1, lineChartView2)
# trace defaults for the display properties.
scatterPlot1Display_1.CompositeDataSetIndex = [0]
scatterPlot1Display_1.UseIndexForXAxis = 0
scatterPlot1Display_1.XArrayName = 'vectors_Z'
scatterPlot1Display_1.SeriesVisibility = ['Points_Y']
scatterPlot1Display_1.SeriesLabel = ['vectors_X', 'vectors_X', 'vectors_Y', 'vectors_Y', 'vectors_Z', 'vectors_Z', 'vectors_Magnitude', 'vectors_Magnitude', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
scatterPlot1Display_1.SeriesColor = ['vectors_X', '0', '0', '0', 'vectors_Y', '0.889998', '0.100008', '0.110002', 'vectors_Z', '0.220005', '0.489998', '0.719997', 'vectors_Magnitude', '0.300008', '0.689998', '0.289998', 'Points_X', '0.6', '0.310002', '0.639994', 'Points_Y', '1', '0.500008', '0', 'Points_Z', '0.650004', '0.340002', '0.160006', 'Points_Magnitude', '0', '0', '0']
scatterPlot1Display_1.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'vectors_Magnitude', '0', 'vectors_X', '0', 'vectors_Y', '0', 'vectors_Z', '0']
scatterPlot1Display_1.SeriesLabelPrefix = ''
scatterPlot1Display_1.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '0', 'Points_Z', '1', 'vectors_Magnitude', '1', 'vectors_X', '1', 'vectors_Y', '1', 'vectors_Z', '1']
scatterPlot1Display_1.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'vectors_Magnitude', '2', 'vectors_X', '2', 'vectors_Y', '2', 'vectors_Z', '2']
scatterPlot1Display_1.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '2', 'Points_Z', '0', 'vectors_Magnitude', '0', 'vectors_X', '0', 'vectors_Y', '0', 'vectors_Z', '0']

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView3'
# ----------------------------------------------------------------

# show data from scatterPlot1
scatterPlot1Display_2 = Show(scatterPlot1, lineChartView3)
# trace defaults for the display properties.
scatterPlot1Display_2.CompositeDataSetIndex = [0]
scatterPlot1Display_2.UseIndexForXAxis = 0
scatterPlot1Display_2.XArrayName = 'Points_Z'
scatterPlot1Display_2.SeriesVisibility = ['vectors_Y']
scatterPlot1Display_2.SeriesLabel = ['vectors_X', 'vectors_X', 'vectors_Y', 'vectors_Y', 'vectors_Z', 'vectors_Z', 'vectors_Magnitude', 'vectors_Magnitude', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
scatterPlot1Display_2.SeriesColor = ['vectors_X', '0', '0', '0', 'vectors_Y', '0.889998', '0.100008', '0.110002', 'vectors_Z', '0.220005', '0.489998', '0.719997', 'vectors_Magnitude', '0.300008', '0.689998', '0.289998', 'Points_X', '0.6', '0.310002', '0.639994', 'Points_Y', '1', '0.500008', '0', 'Points_Z', '0.650004', '0.340002', '0.160006', 'Points_Magnitude', '0', '0', '0']
scatterPlot1Display_2.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'vectors_Magnitude', '0', 'vectors_X', '0', 'vectors_Y', '0', 'vectors_Z', '0']
scatterPlot1Display_2.SeriesLabelPrefix = ''
scatterPlot1Display_2.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'vectors_Magnitude', '1', 'vectors_X', '1', 'vectors_Y', '0', 'vectors_Z', '1']
scatterPlot1Display_2.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'vectors_Magnitude', '2', 'vectors_X', '2', 'vectors_Y', '2', 'vectors_Z', '2']
scatterPlot1Display_2.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'vectors_Magnitude', '0', 'vectors_X', '0', 'vectors_Y', '2', 'vectors_Z', '0']

# ----------------------------------------------------------------
# setup the visualization in view 'lineChartView4'
# ----------------------------------------------------------------

# show data from scatterPlot1
scatterPlot1Display_3 = Show(scatterPlot1, lineChartView4)
# trace defaults for the display properties.
scatterPlot1Display_3.CompositeDataSetIndex = [0]
scatterPlot1Display_3.UseIndexForXAxis = 0
scatterPlot1Display_3.XArrayName = 'vectors_Z'
scatterPlot1Display_3.SeriesVisibility = ['vectors_Y']
scatterPlot1Display_3.SeriesLabel = ['vectors_X', 'vectors_X', 'vectors_Y', 'vectors_Y', 'vectors_Z', 'vectors_Z', 'vectors_Magnitude', 'vectors_Magnitude', 'Points_X', 'Points_X', 'Points_Y', 'Points_Y', 'Points_Z', 'Points_Z', 'Points_Magnitude', 'Points_Magnitude']
scatterPlot1Display_3.SeriesColor = ['vectors_X', '0', '0', '0', 'vectors_Y', '0.889998', '0.100008', '0.110002', 'vectors_Z', '0.220005', '0.489998', '0.719997', 'vectors_Magnitude', '0.300008', '0.689998', '0.289998', 'Points_X', '0.6', '0.310002', '0.639994', 'Points_Y', '1', '0.500008', '0', 'Points_Z', '0.650004', '0.340002', '0.160006', 'Points_Magnitude', '0', '0', '0']
scatterPlot1Display_3.SeriesPlotCorner = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'vectors_Magnitude', '0', 'vectors_X', '0', 'vectors_Y', '0', 'vectors_Z', '0']
scatterPlot1Display_3.SeriesLabelPrefix = ''
scatterPlot1Display_3.SeriesLineStyle = ['Points_Magnitude', '1', 'Points_X', '1', 'Points_Y', '1', 'Points_Z', '1', 'vectors_Magnitude', '1', 'vectors_X', '1', 'vectors_Y', '0', 'vectors_Z', '1']
scatterPlot1Display_3.SeriesLineThickness = ['Points_Magnitude', '2', 'Points_X', '2', 'Points_Y', '2', 'Points_Z', '2', 'vectors_Magnitude', '2', 'vectors_X', '2', 'vectors_Y', '2', 'vectors_Z', '2']
scatterPlot1Display_3.SeriesMarkerStyle = ['Points_Magnitude', '0', 'Points_X', '0', 'Points_Y', '0', 'Points_Z', '0', 'vectors_Magnitude', '0', 'vectors_X', '0', 'vectors_Y', '2', 'vectors_Z', '0']

# ----------------------------------------------------------------
# setup the visualization in view 'plotMatrixView1'
# ----------------------------------------------------------------

# show data from slice1
slice1Display = Show(slice1, plotMatrixView1)
# trace defaults for the display properties.
slice1Display.CompositeDataSetIndex = 0
slice1Display.SeriesVisibility = ['vectors_Y', 'vectors_Z', 'Points_Y', 'Points_Z']

# ----------------------------------------------------------------
# setup the visualization in view 'pythonView1'
# ----------------------------------------------------------------

# show data from slice1
slice1Display_1 = Show(slice1, pythonView1)

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(scatterPlot1)
# ----------------------------------------------------------------