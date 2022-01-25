#!/usr/bin/python3
import os
import Database as DB


def compute(userNodes, daysToCalculate):
    r = .092
    n = userNodes
    d = daysToCalculate
    b = 0
    c = 0
    day = 0
    buyList = []
    massList = []
    for i in range(0, int(d)):
        c = float(n) * r
        day = day + 1
        while b >= 10:
            n = n + 1
            buyList.append(day)
            b = b - 10
        b = b + c
        calcRow = [day, c, b, n]
        massList.append(calcRow)
    DB.ItemCreationProcesses.createCalc(massList)
        
    
