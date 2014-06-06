from django.shortcuts import render
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
    	Tqueryset = Chamber.objects.filter(actions__startswith='Public Act')
    	Tcount = Tqueryset.count()
    	Dcount = Dqueryset.count()
    	Rcount = Rqueryset.count()
    	dPercent = 25*Dcount/Tcount 
    	rPercent = 25*Rcount/Tcount
    	Rbills =[]
    	Dbills =[]
    	for d in Dqueryset:
    		dd= str(d.billNumber())
    		Dbills.append(dd)
    	for r in Rqueryset:
    		rr= str(r.billNumber())
    		Rbills.append(rr)
    	context = {'Dbills': Dbills, 'Rbills': Rbills, 'Dcount': Dcount, 'Rcount': Rcount, 'dPercent': dPercent, 'rPercent': rPercent}
    	return render(self, 'legi/billnumbers.html', context)
 
def billwait(self):
    	Dqueryset = Chamber.objects.filter(actions__startswith='Sent to the Governor', party='D')
    	Rqueryset = Chamber.objects.filter(actions__startswith='Sent to the Governor', party='R')
    	Tqueryset = Chamber.objects.filter(actions__startswith='Sent to the Governor')
    	Tcount = Tqueryset.count()
    	Dcount = Dqueryset.count()
    	Rcount = Rqueryset.count() 
    	dPercent = 25*Dcount/Tcount 
    	rPercent = 25*Rcount/Tcount
    	Rbills =[]
    	Dbills =[]
    	for d in Dqueryset:
    		dd= str(d.billNumber())
    		Dbills.append(dd)
    	for r in Rqueryset:
    		rr= str(r.billNumber())
    		Rbills.append(rr)
    	context = {'Dbills': Dbills, 'Rbills': Rbills, 'Dcount': Dcount, 'Rcount': Rcount, 'dPercent': dPercent, 'rPercent': rPercent}
    	return render(self, 'legi/billnumbers.html', context)

def billlegi(self):
    	Dqueryset = Chamber.objects.filter(actions__startswith='Passed Both Houses', party='D')
    	Rqueryset = Chamber.objects.filter(actions__startswith='Passed Both Houses', party='R')
    	Tqueryset = Chamber.objects.filter(actions__startswith='Passed Both Houses')
    	Tcount = Tqueryset.count()
    	Dcount = Dqueryset.count()
    	Rcount = Rqueryset.count() 
    	dPercent = 25*Dcount/Tcount 
    	rPercent = 25*Rcount/Tcount
    	Rbills =[]
    	Dbills =[]
    	for d in Dqueryset:
    		dd= str(d.billNumber())
    		Dbills.append(dd)
    	for r in Rqueryset:
    		rr= str(r.billNumber())
    		Rbills.append(rr)
    	context = {'Dbills': Dbills, 'Rbills': Rbills, 'Dcount': Dcount, 'Rcount': Rcount, 'dPercent': dPercent, 'rPercent': rPercent}
    	return render(self, 'legi/billnumbers.html', context)
