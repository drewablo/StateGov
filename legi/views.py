from django.shortcuts import render
from django.db.models import Q
from legi.models import Chamber
import time

def billcount(request):
	latest_count = Chamber.objects.filter(dt=(time.strftime("%-m/%d/%Y"))).count()
	pbh = Chamber.objects.filter(actions="Passed Both Houses").count()
	sttg = Chamber.objects.filter(actions="Sent to the Governor").count()
	a = Chamber.objects.filter(actions__startswith='Referred to Assignments').count()
	b = Chamber.objects.filter(actions__startswith='Rule 19').count()
	purg = a+b
	public = Chamber.objects.filter(actions__startswith='Public Act').count()
	context = {'latest_count': latest_count, 'pbh': pbh, 'sttg': sttg, 'purg': purg, 'public': public}
	return render(request, 'legi/billcount.html', context)

def billnum(self):
    	Dqueryset = Chamber.objects.filter(actions__startswith='Public Act', party='D')
    	Rqueryset = Chamber.objects.filter(actions__startswith='Public Act', party='R')
    	Total = Chamber.objects.filter(actions__startswith='Public Act')
    	Dcount = Dqueryset.count()
    	Dbills =[]
    	for d in Dqueryset:
    		Dbills.append(str(d.billNumber()))
	Dpercent = Dcount/Total.count()
    	Rcount = Rqueryset.count()	
    	Rbills =[]
    	for r in Rqueryset:
    		Rbills.append(str(r.billNumber()))
    	Rpercent = Rcount/Total.count()
    	context = {'Dbills': Dbills, 'Rbills': Rbills, 'Dcount': Dcount, 'Rcount': Rcount, 'Dpercnet': Dpercnet, 'Rpercent': Rpercent}
    	return render(self, 'legi/billnumbers.html', context)
 
def billwait(self):
    	Dqueryset = Chamber.objects.filter(actions__startswith='Sent to the Governor', party='D')
    	Rqueryset = Chamber.objects.filter(actions__startswith='Sent to the Governor', party='R')
    	Total = Chamber.objects.filter(actions__startswith='Public Act')
    	Dcount = Dqueryset.count()
    	Dbills =[]
    	for d in Dqueryset:
    		Dbills.append(str(d.billNumber()))
	Dpercent = Dcount/Total.count()
    	Rcount = Rqueryset.count()	
    	Rbills =[]
    	for r in Rqueryset:
    		Rbills.append(str(r.billNumber()))
    	Rpercent = Rcount/Total.count()
    	context = {'Dbills': Dbills, 'Rbills': Rbills, 'Dcount': Dcount, 'Rcount': Rcount, 'Dpercnet': Dpercnet, 'Rpercent': Rpercent}
    	return render(self, 'legi/billnumbers.html', context)
 
def billlegi(self):
    	Dqueryset = Chamber.objects.filter(actions__startswith='Passed Both Houses', party='D')
    	Rqueryset = Chamber.objects.filter(actions__startswith='Passed Both Houses', party='R')
    	Total = Chamber.objects.filter(actions__startswith='Public Act')
    	Dcount = Dqueryset.count()
    	Dbills =[]
    	for d in Dqueryset:
    		Dbills.append(str(d.billNumber()))
	Dpercent = Dcount/Total.count()
    	Rcount = Rqueryset.count()	
    	Rbills =[]
    	for r in Rqueryset:
    		Rbills.append(str(r.billNumber()))
    	Rpercent = Rcount/Total.count()
    	context = {'Dbills': Dbills, 'Rbills': Rbills, 'Dcount': Dcount, 'Rcount': Rcount, 'Dpercnet': Dpercnet, 'Rpercent': Rpercent}
    	return render(self, 'legi/billnumbers.html', context)
 
