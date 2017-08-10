from paraview import python_view

def setup_data(view):
    view.EnableAllAttributeArrays()

def render(view, height, width):
    modheight = height - 100# -800
    modwidth = width # +400  # this fixes image scale
    
    figure = python_view.matplotlib_figure(modwidth, modheight)
    ax = figure.add_subplot(1,1,1)

    dataObject = view.GetVisibleDataObjectForRendering(0)
    
    #print repr(dataObject.GetPoints().GetData())
    if not dataObject: return
    
    #print dataObject
    z = dataObject.GetColumnByName("Z")
    # print z
    y = dataObject.GetColumnByName("Y")
    pz = dataObject.GetColumnByName("Pz")
    py = dataObject.GetColumnByName("Py")

    from paraview.numpy_support import vtk_to_numpy
    np_z = vtk_to_numpy(z)
    np_y = vtk_to_numpy(y)
    np_pz = vtk_to_numpy(pz)
    np_py = vtk_to_numpy(py)
    #print repr(np_x)
    
    # Change colormap with cmap = mpl.cm.get_cmap(<mapname>)
    mplPolyCollection = ax.quiver(np_z,np_y,np_pz,np_py,color='#2f7cef', headwidth=4)
    # print mplPolyCollection.get_clim()
    # print(doop)    

    #print repr(mplPolyCollection)
    ax.minorticks_on()
    ax.set_title("Vectors")
    ax.set_xlabel("Z [m]")
    ax.set_ylabel("Y [m]")
    #ax.set_xlim((-.0045, .0045))
    #ax.set_ylim((-.0045, .0045))
    
    
    return python_view.figure_to_image(figure)
