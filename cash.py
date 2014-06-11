from xlml import etree
import csv
import re

moneyZips = open('moneyZips.csv', 'wb')
writer = csv.writer(moneyZips)

xml = (/Recipts.xml)
context = etree.interparse(xml, tag='RECEIPTLIST')
for c in context: 
	zips = str(c.xpath('RECEIPT/Zip/text()'))
	money = str(c.xpath('RECEIPT/Amount.text()'))
	if re.findall(r'(-)', zips):
		zips = re.findall(r'(^\d{5})', zips)
	writer.writerow(zips,money)
