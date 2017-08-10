import vtk
from os.path import splitext
from OpenFiles import open_multiple

def ConvertFiles(openFilename):
    print("File to read: " + openFilename)

    testreader = vtk.vtkDataReader()
    testreader.SetFileName(openFilename)

    if testreader.IsFileUnstructuredGrid():
        print("Filetype: Unstructured Grid.")
        file_extension = ".vtu"
        myreader = vtk.vtkUnstructuredGridReader()
        mywriter = vtk.vtkXMLUnstructuredGridWriter()
    elif testreader.IsFilePolyData():
        print("Filetype: PolyData.")
        file_extension = ".vtp"
        myreader = vtk.vtkPolyDataReader()
        mywriter = vtk.vtkXMLPolyDataWriter()
        
    saveFilename = splitext(openFilename)[0] + file_extension
    print("File to write: " + saveFilename)

    myreader.SetFileName(openFilename)
    print("\nProcessing input data.  For 360MB file, normally takes ~35 sec.")
    myreader.Update()
    print("Processing complete")
    mydata = myreader.GetOutput()


    mywriter.SetFileName(saveFilename)
    mywriter.SetInputData(mydata)
    mywriter.SetDataModeToBinary()
    print("\n Saving data.  For 360MB file, normally takes ~10 sec.")
    mywriter.Write()

openFilenames = open_multiple()

for (i,elt) in enumerate(openFilenames):
    print("FILE {} %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n".format(i))
    ConvertFiles(elt)
    print("END FILE {} %%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n".format(i))

