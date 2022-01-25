#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 19:37:45 2018
@author: kogito
"""
import csv
import requests
from bs4 import BeautifulSoup


class Scraper():
    @classmethod
    def process(self, url):
        
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        data = []
        table = soup.find('table', id='')
        for row in table.find_all('tr'):
            para = soup.has_attr('class') and row['class'][0] == 'sc-1eb5slv-0'
            print(para)
            f = open('ScrapedData.csv', 'w')
            with f:
                writer = csv.writer(f)
                writer.writerow(row)
            cells = row.findChildren('td')
            values = []
            for cell in cells:
                value = cell.string
                values.append(value)
                print(cell)
        
            try:
                Bitcoin = values[0]
                #Price = values[1]
                High = values[2]
                Price =  values[3]
                Close = values[4]
                Volume = values[5]
                MarketCap = values[6]
            except IndexError as e:
                print(e)
                continue
            data.append([Bitcoin, Price, High, Price, Close, Volume, MarketCap])
        # Print data
        # for item in data:
        #     print(item)
        return data
        