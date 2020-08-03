import hey
from flask import Flask,render_template,jsonify 
import smartIndiahackathon
import torch
import numpy as np
from torch.utils.data import DataLoader
from SpeechDataGenerator import SpeechDataGenerator
import torch.nn as nn
import os
import numpy as np
from torch import optim
import argparse
from models.x_vector_Indian_LID import X_vector
from sklearn.metrics import accuracy_score
from utils.utils import speech_collate
import torch.nn.functional as F
import librosa
import numpy as np
import sox
torch.multiprocessing.set_sharing_strategy('file_system')
from smartIndiahackathon import inference
import feature_extraction
import datasets

app=Flask(__name__,template_folder='templates')

@app.route("/pred")
def pred():
	return render_template('pyth.html')
@app.route("/")
def home():
	return render_template('index.html')
@app.route("/ownrec")
def record1():
    return render_template('ownrec.html') 
@app.route("/record")
def record():
    return render_template('record.html')
def predict():
    return exec(open("smartIndiahackathon.py").read())
       
predict()
@app.route('/_get_data/', methods=['POST'])

def _get_data():

    myList = [predict]
    return jsonify({'data': render_template('response.html', myList=myList)})

@app.route('/index1')

def index():

    return render_template('index1.html')
if __name__ == '__main__':
    app.run(debug=True)





    
