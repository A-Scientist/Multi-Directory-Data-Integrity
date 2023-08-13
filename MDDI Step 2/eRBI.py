
#from contextlib import nullcontext
import tkinter
#import re
import os.path

### NOTES
#Frames are important for packing items in the correct places.
#Frames are stacked from top to bottom.TkinterInputs
#Items inside are packed from left to right.
#Each input from create entry row is added is argv to be used later

#easy Row Based Interface
class eRBI:

	VerticalFrames = 0
	HorizontalSize = 0
	doOnSubmit = None
	Interface = tkinter.Tk()

	# A 2d dictionary with the rows as names of inputs and columms as 'entry' and 'valid'
	TkinterInputs = {}
	TkinterSubmits = []
	
#------------------------------------------------
#Entries

	#limits the number of characters that can be given in an entry
	def __characterLimit(self, entryText, inputSize):
		if len(entryText.get()) > inputSize:
			entryText.set(entryText.get()[:inputSize])

	# Creates a box to insert large amounts of text
	def createEntryRow(self, name, text, prefill=""):
		frame = tkinter.Frame()
		tkinter.Label(frame,text=text).pack(side="left")

		entryText = tkinter.StringVar()

		entry = tkinter.Entry(frame,width=self.HorizontalSize,textvariable=entryText,justify="left")
		entry.insert(tkinter.END, prefill)
		entry.pack(side="left",fill="x")
		#entryText.trace("w",lambda *args: self.__checkFile())

		self.TkinterInputs[name] = {
			"entry":entry,
			"value":entryText,
			"valid":True
		}

		frame.pack(fill="x")
		self.VerticalFrames +=1
		return frame
	
	# Creates a box specifically for file paths, allows for a list of extentions
	# tkinter input is always filePath
	def createPathEntryRow(self, name, extentionList, prefill=""):
		
		frame = tkinter.Frame()
		tkinter.Label(frame,text="File Path").pack(side="left")

		entryText = tkinter.StringVar()

		entry = tkinter.Entry(frame,width=self.HorizontalSize,textvariable=entryText,justify="left")
		entry.insert(tkinter.END, prefill)
		entry.pack(side="left",fill="x")
		entryText.trace("w",lambda *args: self.__checkFile(name, extentionList))

		self.TkinterInputs[name] = {
			"entry":entry,
			"value":entryText,
			"valid":False
		}

		frame.pack(fill="x")
		self.VerticalFrames +=1
		return frame

	# Creates a box for a limited amount of text
	def createLimitedEntryRow(self, name, text, inputSize, prefill=""):
		frame = tkinter.Frame()
		tkinter.Label(frame,text=text).pack(side="left")

		entryText = tkinter.StringVar()

		entry = tkinter.Entry(frame,width=inputSize+2,textvariable=entryText,justify="center")
		entry.insert(tkinter.END, prefill)
		entry.pack(side="left",fill="x")
		entryText.trace("w",lambda *args: self.__characterLimit(entryText,inputSize))

		self.TkinterInputs[name] = {
			"entry":entry,
			"value":entryText,
			"valid":True
		}

		frame.pack(fill="x")
		self.VerticalFrames +=1
		return frame

	# Creates a label
	def createLableRow(self, text):
		frame = tkinter.Frame()
		tkinter.Label(frame,text=text).pack(side="left")

		frame.pack(fill="x")
		self.VerticalFrames +=1
		return frame
#------------------------------------------------

#------------------------------------------------
#Submit

	def __createSubmitRow(self):
		frame = tkinter.Frame()

		#makes button, checks if the function passed to it is valid
		submit = tkinter.Button(frame, text="Submit", state="active")
		self.__errorCheck(not self.doOnSubmit, "ERROR: doOnSubmit is None")
		submit.configure(command=self.doOnSubmit)
		submit.pack(side="left")

		#make a status label
		status = tkinter.Label(frame,text="")
		frame.pack(fill="x")

		#increase height counter and return button and status to change later
		self.VerticalFrames +=1
		self.TkinterSubmits = [submit,status]

	# For path entries
	def __checkFile(self, name, extentionList=None):
		path = self.TkinterInputs[name]["value"].get()

		# disable and red if i don't like the path
		# (if the path does not exist at all)
		# (if want something that isn't a directory, indicated by having an extention list set)
		if not os.path.exists(path) or (extentionList is not None and os.path.isdir(path)):
			self.TkinterInputs[name]["valid"] = False
			self.__changeBackgroundColor(self.TkinterInputs[name]["entry"],'#eda59a') #red
			return
		
		# enable and green if i like (or really like) the path
		self.TkinterInputs[name]["valid"] = True
		extention = path[path.rindex(".")+1:]
		if extention not in extentionList:
			self.__changeBackgroundColor(self.TkinterInputs[name]["entry"],'#f5e57d') #yellow
		else:
			self.__changeBackgroundColor(self.TkinterInputs[name]["entry"],'#9aedb1') #green

		#Make sure all inputs are valid so submit code is good to run
		self.changeSubmitStatus("normal","Everything looks good, continue?")
		for item in self.TkinterInputs:
			if self.TkinterInputs[item]["valid"] == False:
				self.changeSubmitStatus("disabled","One or more inputs are not accepted.")
				break

	# The function passed will be used every time the submit button is pressed
	def setSubmit(self, function):
		self.doOnSubmit = function

	
#------------------------------------------------

#------------------------------------------------
#Startup and Return
	# Initalises the gui window with a horizontal size and name
	def __init__(self, name, HorizontalSize):
		self.HorizontalSize = HorizontalSize
		self.Interface.title(name)
	
	# Call to start the GUI after the rows have been set up
	def startWindow(self): 
		self.__createSubmitRow()
		self.Interface.geometry(f"{self.HorizontalSize}x{self.VerticalFrames*25}") # widthxheight+x+y
		self.Interface.mainloop()

	# Returns a dictionary of inputs with a name as the key
	# Goes inside of the function that is called when you hit the submit button 
	def getInputs(self):
		#i can't read this thing that is recomended by sourcery so i put the translation below
		#return {item[0]: item[1].get() for item in self.TkinterInputs.items()}
		inputs = {}
		for item in self.TkinterInputs:
			inputs[item] = self.TkinterInputs[item]["value"].get()
		return inputs
	
	def destroy(self):
		self.Interface.destroy()
#------------------------------------------------

#------------------------------------------------
#Utility
	def __errorCheck(self, condition, message):
		if(condition):
			print(message)
			exit()

	def __changeBackgroundColor(self, item, color):
		item.pack_forget()
		item.configure(bg=color)
		item.pack(side="left",fill="x")

	#Changes the status of the submit entry
	def changeSubmitStatus(self, pushState, message):
		self.TkinterSubmits[0].pack_forget()
		self.TkinterSubmits[1].pack_forget()
		self.TkinterSubmits[0]['state'] = pushState #not sure why changing button state is different than changing any other properity of any other item in tkinter
		self.TkinterSubmits[1].config(text=message)
		self.TkinterSubmits[0].pack(side="left")
		self.TkinterSubmits[1].pack(side="left")
