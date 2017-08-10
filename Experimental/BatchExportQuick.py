from paraview.simple import *

def exportquick():
	# state file generated using paraview version 5.4.0

	# ----------------------------------------------------------------
	# setup views used in the visualization
	# ----------------------------------------------------------------
	from timeit import default_timer
	from time import sleep
	#import pdb

	#### import the simple module from the paraview

	# ----------------------------------------------------------------
	# Select file to open
	# ----------------------------------------------------------------
	#pdb.set_trace()
	from win32gui import GetOpenFileNameW, GetSaveFileNameW
	(openFilename,_,_) = GetOpenFileNameW()
	print openFilename

	# ----------------------------------------------------------------
	# setup the data processing pipelines
	# ----------------------------------------------------------------

	# create a new 'Legacy VTK Reader'
	print "\n opening gammaBeta...\n"
	start_time = default_timer()
	gammaBetavtktxt = LegacyVTKReader(FileNames=[openFilename])
	next_time = default_timer()
	print "1. Took " + str(next_time - start_time) + " seconds.\n"
	start_time = next_time

	# get slice bounds

	#(xmin,xmax) = gammaBetavtktxt.GetDataInformation().GetPointArrayInformation().GetComponentRange(0)
	xmax = .0591349005
	xmax = xmax-.00005


	next_time = default_timer()
	print "2. Took " + str(next_time - start_time) + " seconds.\n"
	start_time = next_time

	# create a new 'Slice'
	print "creating slice"
	slice2 = Slice(Input=gammaBetavtktxt)
	slice2.SliceType = 'Plane'
	slice2.SliceOffsetValues = [xmax]


	# export data
	print "saving data\n"
	sleep(5)
	print "dialog\n"
	(saveFilename,_,_) = GetSaveFileNameW()
	sleep(5)
	print "Saving " + saveFilename + "\n"
	SaveData(saveFilename, proxy=slice2, UseScientificNotation=1, FieldAssociation="Points")
	sleep(20)
	print "done\n"

	# export row numbers and visibility stuff.  prob not useful.
	#SetActiveSource(programmableFilter2)
	#spreadSheetView1 = GetActiveViewOrCreate('SpreadSheetView')
	#ExportView('D:\DaveMatthew\UMERgun\Experimental\temp.csv', view=spreadSheetView1)

	""" visualize data
	# ----------------------------------------------------------------
	# setup the visualization in view 'spreadSheetView1'
	# ----------------------------------------------------------------

	# show data from programmableFilter2
	programmableFilter2Display = Show(programmableFilter2, spreadSheetView1)
	# trace defaults for the display properties.
	programmableFilter2Display.FieldAssociation = 'Row Data'

	# ----------------------------------------------------------------
	# finally, restore active source
	SetActiveSource(programmableFilter2)
	# ----------------------------------------------------------------
	"""

if __name__ == "__main__":
	exportquick()