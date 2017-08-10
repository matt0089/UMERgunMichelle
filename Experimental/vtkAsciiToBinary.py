from paraview.simple import LegacyVTKReader, SaveData
from win32gui import GetOpenFileNameW
from os.path import splitext

(openFilename,_,_) = GetOpenFileNameW()
print openFilename

dataToConvert = LegacyVTKReader(FileNames=[openFilename])

saveFilename = splitext(openFilename)[0] + ".pvd"
SaveData(saveFilename, proxy=dataToConvert, DataMode='Binary')