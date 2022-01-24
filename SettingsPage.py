import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Entry
import GUI as G

class SettingsPage(G.GUI):
    
    def __init__(self, parent, controller):

        G.GUI.__init__(self, parent)

        label1 = tk.Label(self.mainFrame, font=("Arial", 20),
                        text="Settings", background="#4b4b4b",
                        foreground="blue")
        label1.pack(side="top")
