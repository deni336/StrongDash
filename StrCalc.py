#!/usr/bin/python3
from ast import Break
import os
import Database as DB


def compute(userNodes, daysToCalculate, coinCompound, rewardRate, amountToRemove):
    b = 0
    c = 0
    day = 0
    buyList = []
    massList = []
    for i in range(0, int(daysToCalculate)):
        c = float(userNodes) * rewardRate
        day = day + 1
        while b >= coinCompound:
            userNodes = userNodes + 1
            buyList.append(day)
            b = b - 10
            b = b - amountToRemove
        b = b + c
        calcRow = [day, c, b, userNodes]
        massList.append(calcRow)
    DB.ItemCreationProcesses.createCalc(massList)

def calDay(days, daysToCalculate, userNodes, rewardRate):
    b = 0
    c = 0
    day = 0
    day1 = 0
    massList = []
    for i in range(0, int(daysToCalculate)):
        c = userNodes * rewardRate
        day = day + 1
        day1 = day1 + 1
        if day1 == days:
            while b >= 10:
                userNodes = userNodes + 1
                b = b - 10
            day1 = 0
        b = b + c
        calcRow = [day, c, b, userNodes]
        massList.append(calcRow)
        if days == daysToCalculate:
            break
    DB.ItemCreationProcesses.createCalc(massList)




    
        
    
