import matplotlib as mpl
import numpy as np

from paraview import python_view


def setup_data(view):
    view.EnableAllAttributeArrays()

def render(view, height, width):
    modheight = height # -800
    modwidth = width # +400  # this fixes image scale
    
    figure = python_view.matplotlib_figure(modwidth, modheight)
    ax = figure.add_subplot(1,1,1)

    dataObject = view.GetVisibleDataObjectForRendering(0)
    
    #print repr(dataObject.GetPoints().GetData())
    if not dataObject: return
    
    x = dataObject.GetPoints().GetData()
    #print repr(x)
    
    from paraview.numpy_support import vtk_to_numpy
    np_x = vtk_to_numpy(x)
    #print repr(np_x)
    
    # Change colormap with cmap = mpl.cm.get_cmap(<mapname>)
    mplPolyCollection = ax.scatter(np_x[:,2], np_x[:,1],  s=.2, c='#2f7cef')
    # print mplPolyCollection.get_clim()
    # print(doop)    

    #print repr(mplPolyCollection)
    ax.minorticks_on()
    ax.set_title("Cross Section")
    ax.set_xlabel("Z [m]")
    ax.set_ylabel("Y [m]")
    ax.set_xlim((-.0045, .0045))
    ax.set_ylim((-.0045, .0045))
    
    
    return python_view.figure_to_image(figure)