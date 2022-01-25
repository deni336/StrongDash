import sqlite3
import os
from sqlite3 import Error, Cursor

database = r"C:\\Projects\\StrongDash\\database.db"

def createConnection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

class DatabaseCreationProcess:
    def __init__(self, createCalcDatabase, createMarketDatabase) -> None:
        self.createCalcDatabase = createCalcDatabase
        self.createMarketDatabase = createMarketDatabase

    def createCalcDatabase():
        conn = createConnection(database)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS CALC
                        ( DAY INT NOT NULL,
                          COIN_PER_DAY REAL NOT NULL,
                          TOTAL_COIN REAL NOT NULL,
                          TOTAL_NODES INT NOT NUll);''')
        conn.commit()
        conn.close()
    createCalcDatabase()
    
    def createMarketDatabase():
        conn = createConnection(database)
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS MARKET
                    (COIN TEXT NOT NULL,
                    PRICE REAL NOT NULL,
                    VOLUME REAL NOT NULL,
                    CHANGE REAL NOT NULL);''')
        conn.commit()
        conn.close
    createMarketDatabase()

class ItemCreationProcesses():

    def __init__(self, createCalc) -> None:
        self.createCalc = createCalc

    def createCalc(massList):
        conn = createConnection(database)
        for i in massList: 
            sql = '''INSERT INTO CALC (DAY, COIN_PER_DAY, TOTAL_COIN, TOTAL_NODES)
                    VALUES (?,?,?,?)'''
            cur = conn.cursor()
            cur.execute(sql, i)
        conn.commit()
        conn.close()
        
    def createMarketData(massList):
        conn = createConnection(database)
        for i in massList: 
            sql = '''INSERT INTO CALC (COIN, PRICE, VOLUME, CHANGE)
                    VALUES (?,?,?,?)'''
            cur = conn.cursor()
            cur.execute(sql, i)
        conn.commit()
        conn.close()

class ItemReadProcesses():

    def __init__(self, readCalc) -> None:
        self.readCalc = readCalc
        

    def readCalc(self):
        conn = createConnection(database)
        read = []
        try:
            sql = 'SELECT * FROM CALC'
            cur = conn.cursor()
            reading = cur.execute(sql)
            for i in reading:
                read.append(i)
            conn.close()
        except Error as e:
            print(e)
        return read

class ItemDeleteProcesses():

    def __init__(self, deleteTable) -> None:
        self.deleteTable = deleteTable

    def deleteTable():
        conn = createConnection(database)
        try:
            sql = '''DROP TABLE IF EXISTS CALC'''
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            conn.close()
            
        except Error as e:
            print(e)
        return cur.lastrowid