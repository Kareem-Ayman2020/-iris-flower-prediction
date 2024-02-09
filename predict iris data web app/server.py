# -*- coding: utf-8 -*-
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib
import numpy as np
from flask import Flask
from flask_restful import Api, Resource, reqparse
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import joblib
import numpy as np
from flask import Flask
from flask_restful import Api, Resource, reqparse

from flask import Flask, render_template, request


app = Flask(__name__)


IRIS_MODEL = joblib.load('iris.mdl')    
    
@app.route('/')
def home():
    return render_template('requestmodel.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
     
      int_features = [int(x) for x in request.form.values()]
      final_features = np.array(int_features)
      prediction = IRIS_MODEL.predict(final_features.reshape(1,-1))

      return render_template("responsemodel.html",name  = prediction)    

if __name__ == '__main__':
    app.run(debug=True, port='1080')
    