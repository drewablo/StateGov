from lxml import etree
import csv
import re

moneyZips = open('moneyZips.csv', 'wb')
writer = csv.writer(moneyZips)

xml = ('Receipts.xml')
context = etree.iterparse(xml, tag='RECEIPTLIST')
for action, elem in context:
        zips = elem.xpath('RECEIPT/Zip/text()')
        money = elem.xpath('RECEIPT/Amount/text()')
        if re.findall(r'(-)', zips):
                zips = re.findall(r'(^\d{5})', zips)
        writer.writerow(zips,money)







