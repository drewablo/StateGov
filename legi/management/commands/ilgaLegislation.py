from django.core.management.base import BaseCommand
from legi.models import Chamber
from bs4 import BeautifulSoup
import urllib2
import re
import os

class Command(BaseCommand):
	def handle(self, *args, **options):
		chmbrs =['http://www.ilga.gov/house/', 'http://www.ilga.gov/senate/']
		chamber_abbr = ['HB','SB']
		c = 0
		
		for chmbr in chmbrs:
			site = chmbr	
			url = urllib2.urlopen(site)
			content = url.read()
			soup = BeautifulSoup(content)
			links = []
			partyAffil =[]
			x=0
			y=-1
			table = soup.find('table', cellpadding=3)
			for a in soup.findAll('a',href=True):
				if re.findall('Bills', a['href']):
					l = (site + a['href']+'&Primary=True')
					links.append(str(l))
					x+=1
			for p in table.findAll('tr')[2:]:
				col = p.findAll('td')
				party = col[4].string
				partyAffil.append(party)
			chamber_abbr = chamber_abbr[c]
			if chamber_abbr == "HB":
				partyAffil.append('D')
				partyAffil.append('D')
				partyAffil.append('R')
				partyAffil.append('R')
			for link in links:
				y+=1
				url = urllib2.urlopen(link)
				content = url.read()
				soup = BeautifulSoup(content)
				table = soup.find('table', cellpadding=3)
				for item in table.findAll('tr')[0:]:
					col = item.findAll('td')
					bill = col[0].string
					sponsor = col[1].string
					sponsor = sponsor.encode('ascii','replace')
					last_action = col[4].string
					last_action_date = col[5].string
					for z in re.findall('2014', last_action_date):
						for q in re.findall(chamber_abbr, bill):
							if Chamber.objects.filter(legislation=bill).exists() == False:
								s = Chamber(legislator=sponsor, legislation=bill, actions=last_action, dt=last_action_date, party=partyAffil[y])
								s.save()
							elif Chamber.objects.filter(legislation=bill).exists() == True:
								s = Chamber.objects.get(legislation=bill)
								s.party=partyAffil[y]
								s.save()
								if s.actions.encode('ascii')!=last_action:
									s.actions=last_action
									s.save()
									s.dt=last_action_date
									s.save()


			print chamber_abbr+" done"
			c +=1
			
