import imp
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Entry
import GUI as G
import StrCalc as SC

frameStyles = {"relief": "groove",
               "bd": 3, "bg": "#4b4b4b",
               "fg": "blue", "font": ("Arial", 12, "bold")}

class CalculatorPage(G.GUI):
    
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