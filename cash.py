
from bs4 import BeautifulSoup
import urllib2
import re
import os
import csv

money = str()
zips = str()
moneyZips = open('moneyZips.csv', 'wb')
writer = csv.writer(moneyZips)
site = "http://bit.ly/2014ilmoney"
url = urllib2.urlopen(site).read()
soup = BeautifulSoup(url)
table = soup.find('table', {'id': 'tblContributionListPrint'})
for item in table.findAll('tr')[2:]:
    for row in item.findAll('td'):
        for span in row.findAll('span'):
            if re.findall(r'(^\$)', span.text):
                try:
                        if re.findall(r'(\$?[\d,]*\d,\d{3}\.\d{2})', span.text):
                                money = re.findall(r'(\$?[\d,]*\d,\d{3}\.\d{2})', span.text)
                        elif re.findall(r'(\$?[\d{2},]*\d{2},\d{3}\.\d{2})', span.text):
                                money = re.findall(r'(\$?[\d{2},]*\d{2},\d{3}\.\d{2})', span.text)
                        elif re.findall(r'(\$\d\.\d{2})', span.text):
                                money = re.findall(r'(\$\d)\.\d{2}', span.text)
                        elif re.findall(r'(\$\d+\.\d{2})', span.text):
                                money = re.findall(r'(^\$\d+\.\d{2})', span.text)
                except:
                        pass
            elif re.findall(r'(\d{5})', span.text):
                zips =  re.findall(r'(\d{5})', span.text)

        if len(zips) > 1:
                zips.pop(0)
                z = str(zips[0])
                m = str(money[0])
                master = (z,m)
                writer.writerow(master)
        elif len(zips) == 1:
                try:
                        z = str(zips[0])
                        m = str(money[0])
                        master =(z,m)
                        writer.writerow(master)
                except:
                        pass
        else:
                print 'error'

moneyZips.close()
