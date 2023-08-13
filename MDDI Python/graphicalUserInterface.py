#Owen Voisinet
#11/18/2022
#MDDI Project

import sys
import tkinter

#==declare starting data==
directories = ["test"]
MDDI_Interface = tkinter.Tk() #initates the UI window
directory_list = []

#==declare data functions==
def intake_data():
	print("a")
	#temp=input("tell me")
	#print(temp)

#==declare UI functions==
def add_directory_entry():
	newFrame = tkinter.Frame().pack()
	tkinter.Button(newFrame, text="-", command=remove_directory_entry).grid(column=0,row=0)
	tkinter.Entry(newFrame).grid(column=1,row=0)
	
	directory_list.append(newFrame)
	print(directory_list)


def remove_directory_entry():
	print()
	#print(class_)
	#directory_list[aa].grid_forget()
	#directory_list[aa].destroy()

#==run==
print(directories)

#changes UI features
MDDI_Interface.title("Multi Directory Data Integrity")
MDDI_Interface.geometry("400x400")


myButton = tkinter.Button(MDDI_Interface, text="+", command=add_directory_entry)
myButton.pack(anchor="nw")

#renders/shows the UI window
MDDI_Interface.mainloop()
