import numpy as np
import paraview

m = 9.11e-31
c = 3e8

myvectors = inputs[0].GetPointData().GetArray(0)
mypoints = inputs[0].GetPoints()

py = myvectors[:,1]
vtk_py = paraview.vtk.vtkFloatArray()
vtk_py.SetName("Py")
for i in py:
    vtk_py.InsertNextTuple1(float(i*m*c))
output.AddColumn(vtk_py)

pz = myvectors[:,2]
vtk_pz = paraview.vtk.vtkFloatArray()
vtk_pz.SetName("Pz")
for i in pz:
    vtk_pz.InsertNextTuple1(float(i*m*c))
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