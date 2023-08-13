import tkinter
#import tkinter.ttk

#Sample button and styling
myButtonStyle = Style().configure('TButton', font =('calibri', 10, 'bold', 'underline'), foreground = 'red')
myButtonStyle.map('TButton', foreground = [('active', '!disabled', 'green')], background = [('active', 'black')])
myButton = tkinter.Button(MDDI_UI, text="hey", command=intake_data).pack(pady=10)
myButton.grid(row = 0, column = 3, padx = 100)