from lxml import etree
import csv
import re

moneyZips = open('moneyZips.csv', 'wb')
writer = csv.writer(moneyZips)

x=0
xml =('Receipts.xml')
tree = etree.parse(xml)
root = tree.getroot()
master = []
z = str()
m = str()
for child in root:
        gc =[]
        for grandchild in child:
                if grandchild.tag == 'State':
                        z = grandchild.text
                if grandchild.tag == 'Amount':
                        m = grandchild.text
                combo = (z,m)
        writer.writerow(combo)









