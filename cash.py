from bs4 import BeautifulSoup
import urllib2
import re
import os

site = "http://www.elections.il.gov/campaigndisclosure/ContribListPrint.aspx?LastOnlyNameSearchType=Starts+with&LastOnlyName=&FirstNameSearchType=Starts+with&FirstName=&AddressSearchType=Starts+with&Address=&CitySearchType=Starts+with&City=&State=&Zip=&ZipThru=&ContributionType=All+Types&OccupationSearchType=Starts+with&Occupation=&EmployerSearchType=Starts+with&Employer=&VendorLastOnlyNameSearchType=Starts+with&VendorLastOnlyName=&VendorFirstNameSearchType=Starts+with&VendorFirstName=&VendorAddressSearchType=Starts+with&VendorAddress=&VendorCitySearchType=Starts+with&VendorCity=&VendorState=&VendorZip=&VendorZipThru=&OtherReceiptsDescriptionSearchType=&OtherReceiptsDescription=&PurposeState=Starts+with&Purpose=&Amount=&AmountThru=&RcvDate=1%2f1%2f2014&RcvDateThru=11%2f10%2f2014&Archived=false&QueryType=Contrib&LinkedQuery=false&OrderBy=Last+or+Only+Name+-+A+to+Z"

url = urllib2.urlopen(site).read()
soup = BeautifulSoup(url)
for e in soup.findAll('br'):
    e.extract()
table = soup.find('table', {'id': 'tblContributionListPrint'})
for item in table.findAll('tr')[2:]:
    for row in item.findAll('td'):
        for span in row.findAll('span'):
            if re.findall(r'(\d{5})', span.text):
                print str(re.findall(r'(\d{5})', span.text))       
            if re.findall(r'(^\$\d+)', span.text):
                print str(re.findall(r'(^\$\d+)', span.text))
