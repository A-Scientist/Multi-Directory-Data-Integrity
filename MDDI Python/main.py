#Owen Voisinet
#11/18/2022
#MDDI Project

#Contains 
"""
Make a sudoDirectory class that holds an array of files and sudoDirectories
main.py will create an array of sudoDirectory objects and then compare them
main.py will also run in background, time automatic checks
make sure this program does not eat memory when not backing up by clearing the sudoDirectory trees after a check is over
"""

import os
import sys
import time

def inputFromGuiOrTui():
	return "C:\Users\Owen\OneDrive\1 - Education\College\NMU\Semester 7 Fall 2022\Final Project\Muti Directory Data Integrity"

directories = []
directories.append(inputFromGuiOrTui())
print(directories)
sudoDirectorieTrees = []

def makeItemList():
	for item in directories:
		#if item is file, record file address, if directory, call get file list on it
		print(os.listdir(item))