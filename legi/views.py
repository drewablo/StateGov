from django.shortcuts import render
from legi.models import Chamber
import time

def get_bill_count(self):
	latest_count = Chamber.objects.filter(dt=(time.strftime("%-m/%d/%Y"))).count()
	context = {'latest_count': latest_count}
	return render(self, 'legi/billcount.html', context)

