from django.core.management.base import BaseCommand
from legi.models import Chamber
from bs4 import BeautifulSoup
import urllib2
import re

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
			x=0
			table = soup.find('table', cellpadding=3)
			for a in soup.findAll('a',href=True):
				if re.findall('Bills', a['href']):
					l = (site + a['href']+'&Primary=True')
					links.append(str(l))
					x+=1
			chamber_abbr = chamber_abbr[c]
			for link in links:
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
							if not Chamber.objects.filter(legislation=bill):
								s = Chamber(legislator=sponsor, legislation=bill, actions=last_action, dt=last_action_date)
								s.save
							else:
								for o in (Chamber.objects.filter(actions=last_action).exists() == False):
									o.actions=last_action
									o.save()
									o.dt=last_action_date
									o.save()
			c +=1