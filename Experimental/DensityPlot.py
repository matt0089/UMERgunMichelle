import matplotlib as mpl
import numpy as np

from paraview import python_view


def setup_data(view):
    view.EnableAllAttributeArrays()

def render(view, height, width):
    modheight = height # -800
    modwidth = width # +400  # this fixes image scale
    
    figure = python_view.matplotlib_figure(modwidth, modheight)
    ax = figure.add_subplot(111, aspect="equal")

    dataObject = view.GetVisibleDataObjectForRendering(0)
    
    #print repr(dataObject.GetPoints().GetData())
    if not dataObject: return
    
    x = dataObject.GetPoints().GetData()
    #print repr(x)
    
    from paraview.numpy_support import vtk_to_numpy
    np_x = vtk_to_numpy(x)
    #print repr(np_x)
    
    # Change colormap with cmap = mpl.cm.get_cmap(<mapname>)
    mplPolyCollection = ax.hexbin(np_x[:,2], np_x[:,1], gridsize=50, vmin=0, vmax=70, cmap=mpl.cm.get_cmap('YlGn'))
    # print mplPolyCollection.get_clim()
    doop = figure.colorbar(mplPolyCollection, ax=ax, drawedges=True, boundaries=xrange(0,70,5), shrink=.8)
    # print(doop)    

    #print repr(mplPolyCollection)
    ax.minorticks_on()
    ax.set_title("Number of Particles per Grid Cell")
    ax.set_xlabel("Z [m]")
    ax.set_ylabel("Y [m]")
    ax.set_xlim((-.0045, .0045))
    ax.set_ylim((-.0045, .0045))
    
    
    return python_view.figure_to_image(figure)