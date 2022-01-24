import threading
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Entry
import StrCalc as SC
import GUI as G
import CalculatorPage as CP
import SettingsPage as SP




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
        self.showFrame(CP)
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
                              command=lambda: parent.showFrame(CP))
        menu_file.add_command(label="Settings",
                              command=lambda: parent.showFrame(SP))
        menu_file.add_separator()
        menu_file.add_command(label="Exit Application",
                              command=lambda: parent.quitApplication())
        help_file = tk.Menu(self, tearoff=0)
        self.add_cascade(label="Help", menu=help_file)

    
    def __init__(self, parent):

        tk.Frame.__init__(self, parent)
        self.mainFrame = tk.Frame(self, bg="#4b4b4b", height=1920, width=1080)
        # self.mainFrame.pack_propagate(0)
        self.mainFrame.pack(fill="both", expand="true")
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=1)


    def __init__(self, parent):

        G.GUI.__init__(self, parent)

        label1 = tk.Label(self.mainFrame, font=("Arial", 20),
                          text="Calculator", background="#4b4b4b",
                          foreground="blue")
        label1.pack(side="top")

        frame1 = tk.LabelFrame(self.mainFrame, G.frameStyles, text="Calculator Output")
        frame1.place(rely=0.05, relx=0.58, height=800, width=800)
        frame2 = tk.LabelFrame(self.mainFrame, G.frameStyles, text="Calculator Input")
        frame2.place(rely=0.05, relx=0.02, height=400, width=600)
        userNodes = Entry(frame2)
        userNodes.insert(tk.END, "Number of Nodes")
        userNodes.place(rely=0.05, relx=0.01)
        daysToCalculate = Entry(frame2)
        daysToCalculate.insert(tk.END, "Days to Calculate")
        daysToCalculate.place(rely=0.10, relx=0.01)
        writeBtn = ttk.Button(frame2, text="Submit",
                                  command=lambda: SC.compute(userNodes, daysToCalculate))
        writeBtn.place(rely=0.90, relx=0.70)
        closeBtn = ttk.Button(frame2, text="Clear")
        closeBtn.place(rely=0.90, relx=0.85)

        tv1 = ttk.Treeview(frame1)
        columnListAccount = ("Day", "Coin/day", "Total/coin", "Total Nodes", "Nodes Purchased")
        tv1['columns'] = columnListAccount
        tv1['show'] = "headings"
        for column in columnListAccount:
            tv1.heading(column, text=column)
            tv1.column(column, width=50)
        tv1.place(relheight=1, relwidth=.995)
        treeScrollY = tk.Scrollbar(frame1)
        treeScrollY.configure(command=tv1.yview)
        tv1.configure(yscrollcommand=treeScrollY.set)
        treeScrollY.pack(side="right", fill="y")



root = MyApp()
app = FullScreenApp(root)
root.title("Strong Dash")
root.mainloop()

