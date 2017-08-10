import vtk
from os.path import splitext
from OpenFiles import open_multiple

openFilenames = open_multiple()
print "Files to read: " + openFilenames

def ConvertFiles(openFilename):
    testreader = vtk.vtkDataReader()
    testreader.SetFileName(openFilename)

    if testreader.IsFileUnstructuredGrid():
        print "Filetype: Unstructured Grid."
        file_extension = ".vtu"
        myreader = vtk.vtkUnstructuredGridReader()
        mywriter = vtk.vtkXMLUnstructuredGridWriter()
    elif testreader.IsFilePolyData():
        print "Filetype: PolyData."
        file_extension = ".vtp"
        myreader = vtk.vtkPolyDataReader()
        mywriter = vtk.vtkXMLPolyDataWriter()
        
    saveFilename = splitext(openFilename)[0] + file_extension
    print "File to write: " + saveFilename

    myreader.SetFileName(openFilename)
    print "\nProcessing input data.  For 360MB file, normally takes ~35 sec."
    myreader.Update()
    print "Processing complete"
    mydata = myreader.GetOutput()


    mywriter.SetFileName(saveFilename)
    mywriter.SetInputData(mydata)
    mywriter.SetDataModeToBinary()
    print "\n Saving data.  For 360MB file, normally takes ~10 sec."
    mywriter.Write()

for elt in openFilenames:
    ConvertFiles(elt)

