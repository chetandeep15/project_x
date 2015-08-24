from django.shortcuts import render
from math import *
import adobepredict as adpr
import applepredict as appl
import numpy as np
from math import sqrt
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import LinearLayer
from pybrain.supervised.trainers import BackpropTrainer
from sklearn import preprocessing
from sklearn.metrics import mean_squared_error
import pylab
import pickle

# Create your views here.

from statistics.models import Companies, Market, Currency

def stats(request, c_name):
	if c_name=='adobe' :
		rval=adpr.predict()
		print rval['Error']
		return render(request,'adobe_stats.html')
	else :
		rval=appl.predict()
		print rval['Error'],c_name
		return render(request, 'apple_stats.html',{'error':rval['Error']})