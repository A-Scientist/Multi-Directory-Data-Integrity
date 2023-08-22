#Owen Voisinet
#11/06/2023

import os
from sys import platform
from eRBI import *

scripts = []
plat=platform
print(plat)
if plat == "linux" or plat == "linux2":
	directorySlash = "/"
elif plat == "win32" or plat == "win64":
	directorySlash = "\\"
scriptsPath = f"{os.getcwd()}{directorySlash}MDDI_Scripts"

def onStartup():
	print(f"Location of my MDDI Scripts: {scriptsPath}")
	if os.path.exists(scriptsPath): #find the folder with the script files in it and remember them
		global scripts
		scripts = os.listdir(scriptsPath)
		print(scripts)
	else: #if it doesn't exist, make one
		os.mkdir(scriptsPath)
	
	#TODO
	#Create the tkinter window for displaying information

def onNewScipt():

	def makeScript():
		name = newScriptWindow.getInputs()["Name"]
		if(f"{name}.txt" in scripts): #bark at the user if a script with that name already exists
			newScriptWindow.changeSubmitStatus("enabled","A script with that name already exists!!!")
		else: #creates a script text file with the given name
			with open(os.path.join(scriptsPath, f"{name}.txt"), 'w'):
				pass
			scripts.append(f"{name}.txt")
			newScriptWindow.destroy()

	newScriptWindow = eRBI("Create New Script",400)
	newScriptWindow.createLimitedEntryRow("Name","Name:",40)
	newScriptWindow.setSubmit(makeScript)
	newScriptWindow.startWindow()


def onChangeScript(argLocations, argTime):
	pass
	#write time and locations to a sync file
	#for each in argLocations:

#TESTING
onStartup()
onNewScipt()
print("\n")