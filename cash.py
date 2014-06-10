
from bs4 import BeautifulSoup
import urllib2
import re
import os

money = str()
zips = str()

site = "http://www.elections.il.gov/campaigndisclosure/ContribListPrint.aspx?LastOnlyNameSearchType=Starts+with&LastOnlyName=&FirstNameSearchType=Starts+with&FirstName=&AddressSearchType=Sta$
url = urllib2.urlopen(site).read()
soup = BeautifulSoup(url)
table = soup.find('table', {'id': 'tblContributionListPrint'})
for item in table.findAll('tr')[2:]:
    for row in item.findAll('td'):
        for span in row.findAll('span'):
                if re.findall(r'(\$[0-9]+[,]?[0-9]+\.d{2})', span.text):
                        money = re.findall(r'(\$[0-9]+[,]?[0-9]+\.d{2})', span.text)
                        date = re.findall(r'(^[0-9]+\\[0-9]+\\\d{4}
                elif re.findall(r'(\$[0-9]+.\d{2})', span.text):
                        money = re.findall(r'(\$\d\.\d{2})', span.text)
                elif re.findall(r'(^\d+)', span.text):
                        zips = re.findall(r'(\d{5})', span.text)

        if len(zips) > 1:
                zips.pop(0)
                z = str(zips[0])
                m = str(money[0])
                master =(z,m)
                print master
        elif len(zips) == 1:
                try:
                        z = str(zips[0])
                        m = str(money[0])
                        master =(z,m)
                        print master
                except:
                        z = zips[0]
                        m = money
                        master = (z,m)
                        print master

                else:
                        print 'error'


