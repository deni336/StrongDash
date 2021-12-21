#!/usr/bin/python3
def compute():
    r = .09
    n = int(input("Please input the number of nodes you have: "))
    d = input("Please input the number of days you would like to calculate: ")
    b = 0
    c = 0
    day = 0
    for i in range(0, int(d)):
        c = float(n) * r
        day = day + 1
        while b >= 10:
            n = n + 1
            b = b - 10
        b = b + c
        print("On day", day, "You made", c, "Strong coin today!", "Your total coin is:", b, ".", "You have a total of", n, "nodes.")

compute()