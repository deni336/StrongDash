import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Entry
import GUI as G
import StrCalc as SC
import Database as DB
import Scraper as SP

frameStyles = {"relief": "groove",
               "bd": 3, "bg": "#4b4b4b",
               "fg": "blue", "font": ("Arial", 12, "bold")}

bitUrl = "https://coinmarketcap.com/currencies/bitcoin"
ethUrl = "https://coinmarketcap.com/currencies/ethereum/"
strUrl = "https://coinmarketcap.com/currencies/strong/"
bnbUrl = "https://coinmarketcap.com/currencies/bnb/"
tthUrl = "https://coinmarketcap.com/currencies/tether/"
dogUrl = "https://coinmarketcap.com/currencies/dogecoin/"
polUrl = "https://coinmarketcap.com/currencies/polygon/"
shiUrl = "https://coinmarketcap.com/currencies/shiba-inu/"
lteUrl = "https://coinmarketcap.com/currencies/litecoin/"
algUrl = "https://coinmarketcap.com/currencies/algorand/"

urlList = [bitUrl, ethUrl, strUrl, bnbUrl, tthUrl, dogUrl, polUrl, shiUrl, lteUrl, algUrl]


class CalculatorPage(G.GUI):
    
    def __init__(self, parent, controller):

        G.GUI.__init__(self, parent)

        label1 = tk.Label(self.mainFrame, font=("Arial", 20),
                          text="Calculator", background="#4b4b4b",
                          foreground="blue")
        label1.pack(side="top")

        frame1 = tk.LabelFrame(self.mainFrame, G.frameStyles, text="Calculator Output")
        frame1.place(rely=0.05, relx=0.58, height=820, width=800)
        frame2 = tk.LabelFrame(self.mainFrame, G.frameStyles, text="Calculator Input")
        frame2.place(rely=0.05, relx=0.02, height=400, width=600)
        userNodes = Entry(frame2)
        userNodes.insert(tk.END, "Number of Nodes")
        userNodes.place(rely=0.05, relx=0.01)
        daysToCalculate = Entry(frame2)
        daysToCalculate.insert(tk.END, "Days to Calculate")
        daysToCalculate.place(rely=0.10, relx=0.01)

        def calcEntryFunc():
            deleteTablefunc()
            nodes = userNodes.get()
            days = daysToCalculate.get()
            SC.compute(int(nodes), int(days))
            tv1LoadData()

        def deleteTablefunc():
            DB.ItemDeleteProcesses.deleteTable()
            tv1.delete(*tv1.get_children())
            DB.DatabaseCreationProcess.createDatabase()

        writeBtn = ttk.Button(frame2, text="Submit",
                                  command=lambda: calcEntryFunc())
        writeBtn.place(rely=0.90, relx=0.70)
        clearBtn = ttk.Button(frame2, text="Clear", command=lambda: deleteTablefunc())
        clearBtn.place(rely=0.90, relx=0.85)

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
                
        frame3 = tk.LabelFrame(self.mainFrame, G.frameStyles, text="Market Data")
        frame3.place(rely=0.45, relx=0.02, height=400, width=600)
        
        tv2 = ttk.Treeview(frame3)
        columnListAccount = ("Coin", "Price", "High", "Low", "Close", "Volume", "MarketCap")
        tv2['columns'] = columnListAccount
        tv2['show'] = "headings"
        for column in columnListAccount:
            tv2.heading(column, text=column)
            tv2.column(column, width=50)
        tv2.place(relheight=1, relwidth=.995)
        treeScrollY = tk.Scrollbar(frame3)
        treeScrollY.configure(command=tv2.yview)
        tv2.configure(yscrollcommand=treeScrollY.set)
        treeScrollY.pack(side="right", fill="y")
        
        def invokeScrape():
            for url in urlList:
                data = SP.Scraper.process(url)
                for row in data:
                    tv2.insert("", "end", values=row)
        invokeScrape()
        
        
            
            
        
