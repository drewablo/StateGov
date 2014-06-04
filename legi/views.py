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
    	queryset = Chamber.objects.filter(actions__startswith='Public Act')
    	bills =[]
    	for b in queryset:
    		bb = str(b.billNumber())
    		bills.append(bb)
    	context = {'bills': bills}
    	return render(self, 'legi/billnumbers.html', context)
 
def billwait(self):
    	queryset = Chamber.objects.filter(actions__startswith='Sent to the Governor')
    	bills =[]
    	for b in queryset:
    		bb = str(b.billNumber())
    		bills.append(bb)
    	context = {'bills': bills}
    	return render(self, 'legi/billnumbers.html', context)
    	
def billlegi(self):
    	queryset = Chamber.objects.filter(actions__startswith='Passed Both Houses')
    	bills =[]
    	for b in queryset:
    		bb = str(b.billNumber())
    		bills.append(bb)
    	context = {'bills': bills}
    	return render(self, 'legi/billnumbers.html', context)


	
