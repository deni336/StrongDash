import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Entry
import StrCalc as SC
import GUI as G
import CalculatorPage as CP
import SettingsPage as SP
import Database as DB



class FullScreenApp(object):
    def __init__(self, master):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

class MyApp(tk.Tk):
    
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        mainFrame = tk.Frame(self, bg="#4b4b4b", height=1920, width=1080)
        mainFrame.pack_propagate(0)
        mainFrame.pack(fill="both", expand="true")
        mainFrame.grid_rowconfigure(0, weight=1)
        mainFrame.grid_columnconfigure(0, weight=1)
        self.geometry("1024x600")
        self.frames = {}
        pages = (CP.CalculatorPage, SP.SettingsPage)
        for F in pages:
            frame = F(mainFrame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showFrame(CP.CalculatorPage)
        menuBar = MenuBar(self)
        tk.Tk.config(self, menu=menuBar)

    def showFrame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def quitApplication(self):
        self.destroy()

class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        menu_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Menu", menu=menu_file)
        menu_file.add_command(label="Calculator",
                              command=lambda: parent.showFrame(CP.CalculatorPage))
        # menu_file.add_command(label="Settings",
        #                       command=lambda: parent.showFrame(SP.SettingsPage))
        menu_file.add_separator()
        menu_file.add_command(label="Exit Application",
                              command=lambda: parent.quitApplication())
        # help_file = tk.Menu(self, tearoff=0)
        # self.add_cascade(label="Help", menu=help_file)



root = MyApp()
app = FullScreenApp(root)
root.title("Strong Dash")
root.mainloop()

