from django.shortcuts import render
from legi.models import Chamber
import time

def billcount(request):
	d = time.strftime("%-m/%d/%Y")
	d = d.encode('utf-8')
	latest_count = Chamber.objects.filter(dt=(d)).count()
	context = {'latest_count': latest_count}
	return render(request, 'legi/billcount.html', context)

