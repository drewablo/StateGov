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
	public = Chamber.objects.filter(actions__startswith='Public ').exclude(dt='1/7/2014').count()
	context = {'latest_count': latest_count, 'pbh': pbh, 'sttg': sttg, 'purg': purg, 'public': public}
	return render(request, 'legi/billcount.html', context)
