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
a = str() #address
cy = str() #city
s = str() #street
z = str() #zipcode
m = str() #amount of donations
n = str() #last name
f = str() #first name
d = str() #date received
c = str() #name of person getting donation
for child in root:
        gc =[]
        for grandchild in child:
                if grandchild.tag == 'LastOnlyName':
                        n = grandchild.text
                        n = n.encode('ascii','ignore')
                if grandchild.tag == 'FirstName':
                        f = grandchild.text
                        try:
                                f = f.encode('ascii','ignore')
                        except:
                                pass
                if grandchild.tag == 'Address1':
                        a = grandchild.text
                        try:
                                a = a.encode('ascii','ignore')
                        except:
                                pass
                if grandchild.tag == 'City':
                        cy = grandchild.text
                if grandchild.tag == 'State':
                        s = grandchild.text						
                if grandchild.tag == 'RcvDate':
                        d = grandchild.text
                if grandchild.tag == 'CmteName':
                        c = grandchild.text
                        try:
                                c = c.encode('ascii','ignore')
                        except:
                                pass
                if grandchild.tag == 'Zip':
                        z = grandchild.text
                if grandchild.tag == 'Amount':
                        m = grandchild.text
                combo = (a,cy,s,z,f,n,m,d,c)
        writer.writerow(combo)
