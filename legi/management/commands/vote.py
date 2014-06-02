import scraperwiki
from bs4 import BeautifulSoup
import urllib2
import lxml.etree
import re
from django.core.management.base import BaseCommand
from legi.models import Votes

class Command(BaseCommand):
	def handle(self, *args, **options):
		chmbrs =['http://www.ilga.gov/house/', 'http://www.ilga.gov/senate/']
		for chmbr in chmbrs:
			site = chmbr	
			url = urllib2.urlopen(site)
			content = url.read()
			soup = BeautifulSoup(content)
			links = []
			linkStats = []
			x=0
			y=0
			table = soup.find('table', cellpadding=3)
			for a in soup.findAll('a',href=True):
				if re.findall('Bills', a['href']):
					l = (site + a['href']+'&Primary=True')
					links.append(str(l))
					x+=1
					print x
			for link in links:
				url = urllib2.urlopen(link)
				content = url.read()
				soup = BeautifulSoup(content)
				table = soup.find('table', cellpadding=3)
				for a in table.findAll('a',href=True):
					if re.findall('BillStatus', a['href']):
						linkStats.append(str('http://ilga.gov'+a['href']))
			for linkStat in linkStats:
				url = urllib2.urlopen(linkStat)
				content = url.read()
				soup = BeautifulSoup(content)
				for a in soup.findAll('a',href=True):
					if re.findall('votehistory', a['href']):
						vl = 'http://ilga.gov/legislation/'+a['href']
						url = urllib2.urlopen(vl)
						content = url.read()
						soup = BeautifulSoup(content)
						for b in soup.findAll('a',href=True):
							if re.findall('votehistory', b['href']):
								llink = 'http://ilga.gov'+b['href']
								try:
									u = urllib2.urlopen(llink)
									x = scraperwiki.pdftoxml(u.read())
									root = lxml.etree.fromstring(x)
									pages = list(root)
									chamber = str()
									for page in pages:
										print "working_1"
										for el in page:
											print "working_2"
											if el.tag == 'text':
												if int(el.attrib['top']) == 168:
													chamber = el.text
												if re.findall("Senate Vote", chamber):
													if int(el.attrib['top']) >= 203 and int(el.attrib['top']) < 231:
														title = el.text
														if (re.findall('House', title)):
															title = (re.findall('[0-9]+', title))
															title = "HB"+title[0]
														elif (re.findall('Senate', title)):
															title = (re.findall('[0-9]+', title))
															title = "SB"+title[0]
													if int(el.attrib['top']) >350 and int(el.attrib['top']) <650:
														r = el.text
														names = re.findall(r'[A-z-\u00F1]{3,}',r)
														vs = re.findall(r'[A-Z]{1,2}\s',r)
														for name in names:
															legi = name
															for vote in vs:
																v = vote
															if Votes.objects.filter(legislation=title).exists() == False:
																c = Votes(legislation=title, legislator=legi, vote=v)
																c.save()	
																print 'saved'
															else:
																print 'not saved'														
												elif int(el.attrib['top']) == 189:
													chamber = el.text
												if re.findall("HOUSE ROLL CALL", chamber):
													if int(el.attrib['top']) > 200 and int(el.attrib['top']) <215:
														title = el.text
														if (re.findall('HOUSE', title)):
															title = (re.findall('[0-9]+', title))
															title = "HB"+title[0]
														elif (re.findall('SENATE', title)):
															title = (re.findall('[0-9]+', title))
															title = "SB"+title[0]
													if int(el.attrib['top']) >385 and int(el.attrib['top']) <1000:
														r = el.text
														names = re.findall(r'[A-z-\u00F1]{3,}',r)
														votes = re.findall(r'[A-Z]{1,2}\s',r)
														for name in names:
															legi = name
															for vote in votes:
																v = vote
															if Votes.objects.filter(legislation=title).exists() == False:
																c = Votes(legislation=title, legislator=legi, vote=v)
																c.save()
																print 'saved'
															else:
																print 'not saved'
																																		
								except:
									pass
							
