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
def predict():
	predict_file='/home/srai/project_x/Resources/csv/adobe_predict.csv'
	f=open('nn_model','rb')
	net=pickle.load(f)
	print "model loaded"
	val = np.loadtxt( predict_file, delimiter = ',' )
	print "file loaded"
	x_val = val[:,:]
	y_val = val[:,1]
	y_val = y_val.reshape( -1, 1 )
	min_max_scaler = preprocessing.MinMaxScaler()
	X_val=min_max_scaler.fit_transform(x_val)
	Y_val=min_max_scaler.fit_transform(y_val)
	print "file scaled"
	l=[]
	for x in X_val:
		l.append(net.activate(x))
	pylab.plot([i for i in range(len(X_val))],
	           [x  for x in l ], linewidth = 2,
	           color = 'blue', label = 'NN output')
	print "predictions done"
	pylab.plot([i for i in range(len(X_val))],
	           Y_val , linewidth = 2, color = 'red', label = 'Target Value')
	pylab.xlabel('Index')
	pylab.ylabel('Stock Price')
	pylab.grid()
	pylab.legend()
	pylab.savefig('adobe_predictions_scaled.jpeg')
	print "evaluating"
	rms = sqrt(mean_squared_error(Y_val, l))
	return {'Error':rms,'image':'adobe_predictions_scaled.jpeg'}

if __name__ == '__main__':
	predict()