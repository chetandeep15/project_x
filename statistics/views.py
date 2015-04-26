from django.shortcuts import render
from math import *

# Create your views here.

from statistics.models import Companies, Market, Currency

def stats(request, c_name):
	i=0
	m_h=-1
	m_l=float("inf")
	s_o=0
	s_c=0
	d=0
	c=Companies.objects.all().filter(name=c_name)
	for comp in c:
	 	i=i+1
	 	d=d+abs(comp.close-comp.open)
		s_o=s_o+comp.open
		s_c=s_c+comp.close
		if comp.low < m_l:
			m_l=comp.low
		if comp.high > m_h:
			m_h=comp.high
	avg_o=s_o/i
	avg_c=s_c/i
	d=d/i
	var_o=0
	var_c=0
	for comp in c:
		x=avg_o-comp.open
		x=x**2
		var_o=var_o+x
		x=avg_c-comp.close
		x=x**2
		var_c=var_c+x
	var_c=var_c/i
	var_o=var_o/i
	corr=nasdaq_corr(c,avg_o)
	# return HttpResponse(avg)
	return render(request, 'stat.html',{'name':c_name,'avg_op':avg_o,'avg_cl':avg_c,'max':m_h,'min':m_l,'d':d,'var_c':var_c,'var_o':var_o,'corr':corr})

def nasdaq_corr(c,obar):
	m=Market.objects.filter(name='nasdaq_it')
	mbar=0
	i=0
	for mar in m:
		i=i+1
		mbar=mbar+mar.open
	mbar=mbar/i
	a=[]
	b=[]
	n=0
	d1=0
	d2=0
	d=0
	for x in c:
		a.append(x.open-obar)
	for x in m:
		b.append(x.open-mbar)
	l=len(a)
	for i in range(0,l):
		n=n+(a[i]*b[i])
	for i in range(0,l):
		d1=d1+(a[i]*a[i])
		d2=d2+(b[i]*b[i])
	d=d1+d2
	d=d/10
	#d=sqrt(d)
	co=n/d
	print co
	return co