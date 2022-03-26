import tkinter as tk
from tkinter import OptionMenu, ttk
from tkinter import *
from tkinter.ttk import Entry
import GUI as G
import StrCalc as SC
import Database as DB

frameStyles = {"relief": "groove",
               "bd": 3, "bg": "#4b4b4b",
               "fg": "blue", "font": ("Arial", 12, "bold")}


class CalculatorPage(G.GUI):
    
    def __init__(self, parent, controller):

        G.GUI.__init__(self, parent)

        label1 = tk.Label(self.mainFrame, font=("Arial", 20),
                          text="Calculator", background="#4b4b4b",
                          foreground="blue")
        label1.pack(side="top")

        frame1 = tk.LabelFrame(self.mainFrame, G.frameStyles, text="Calculator Output")
        frame1.place(rely=0.05, relx=0.01, height=820, width=800)
        frame2 = tk.LabelFrame(self.mainFrame, G.frameStyles, text="Calculator Input")
        frame2.place(rely=0.05, relx=0.45, height=500, width=200)
        userNodes = Entry(frame2)
        userNodes.insert(tk.END, "Number of Nodes")
        userNodes.place(rely=0.05, relx=0.01)
        daysToCalculate = Entry(frame2)
        daysToCalculate.insert(tk.END, "Days to Calculate")
        daysToCalculate.place(rely=0.10, relx=0.01)
        coinCompound = Entry(frame2)
        coinCompound.insert(tk.END, "Total Coin at collection")
        coinCompound.place(rely=0.15, relx=0.01)
        rewardRate = Entry(frame2)
        rewardRate.insert(tk.END, "Reward Rate")
        rewardRate.place(rely=0.20, relx=0.01)
        amountToRemove = Entry(frame2)
        amountToRemove.insert(tk.END, "Profits to Remove")
        amountToRemove.place(rely=0.25, relx=0.01)
        userNodes1 = Entry(frame2)
        userNodes1.insert(tk.END, "Number of Nodes")
        userNodes1.place(rely=0.60, relx=0.01)
        days = Entry(frame2)
        days.insert(tk.END, "Days to collect at")
        days.place(rely=0.65, relx=0.01)
        daysToCalculate1 = Entry(frame2)
        daysToCalculate1.insert(tk.END, "Days to Calculate")
        daysToCalculate1.place(rely=0.70, relx=0.01)
        rewardRate1 = Entry(frame2)
        rewardRate1.insert(tk.END, "Reward Rate")
        rewardRate1.place(rely=0.75, relx=0.01)
        

        def calcEntryFunc():
            deleteTablefunc()
            nodes = userNodes.get()
            days = daysToCalculate.get()
            coin = coinCompound.get()
            reward = rewardRate.get()
            amount = amountToRemove.get()
            SC.compute(int(nodes), int(days), float(coin), float(reward), float(amount))
            tv1LoadData()

        def deleteTablefunc():
            DB.ItemDeleteProcesses.deleteTable()
            tv1.delete(*tv1.get_children())
            DB.DatabaseCreationProcess.createCalcDatabase()

        writeBtn = ttk.Button(frame2, text="Submit",
                                  command=lambda: calcEntryFunc())
        writeBtn.place(rely=0.35, relx=0.50)
        clearBtn = ttk.Button(frame2, text="Clear", command=lambda: deleteTablefunc())
        clearBtn.place(rely=0.40, relx=0.50)

        def calEntryFunc():
            deleteTablefunc()
            nodes = userNodes1.get()
            days1 = days.get()
            calcdays = daysToCalculate1.get()
            reward = rewardRate1.get()
            SC.calDay(int(days1), int(calcdays), int(nodes), float(reward))
            tv1LoadData()

        writeBtn = ttk.Button(frame2, text="Submit",
                                  command=lambda: calEntryFunc())
        writeBtn.place(rely=0.90, relx=0.50)
        clearBtn = ttk.Button(frame2, text="Clear", command=lambda: deleteTablefunc())
        clearBtn.place(rely=0.95, relx=0.50)

        tv1 = ttk.Treeview(frame1)
        columnListAccount = ("Day", "Coin/day", "Total/coin", "Total Nodes")
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

        def tv1LoadData():
            calcTable = DB.ItemReadProcesses.readCalc(self)
            for row in calcTable:
                tv1.insert("", "end", values=row)
        
        
        
        
        
            
            
        
