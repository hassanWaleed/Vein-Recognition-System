from flask import Flask, render_template, url_for, request
from flask import jsonify
import flask
import pandas as pd
from sklearn.preprocessing import FunctionTransformer
import os
import tensorflow as tf
from tensorflow import keras
import numpy as np
import os


import streamlit as st
import streamlit.components.v1 as components

    
app = flask.Flask('your_flask_env')
app = Flask(__name__)

loaded_model = keras.models.load_model('model.h5')

label_to_id = {'person_001': 0,
 'person_002': 1,
 'person_003': 2,
 'person_004': 3,
 'person_005': 4,
 'person_006': 5,
 'person_007': 6,
 'person_008': 7,
 'person_009': 8,
 'person_010': 9,
 'person_011': 10,
 'person_012': 11,
 'person_013': 12,
 'person_014': 13,
 'person_015': 14,
 'person_016': 15,
 'person_017': 16,
 'person_018': 17,
 'person_019': 18,
 'person_020': 19,
 'person_021': 20,
 'person_022': 21,
 'person_023': 22,
 'person_024': 23,
 'person_025': 24,
 'person_026': 25,
 'person_027': 26,
 'person_028': 27,
 'person_029': 28,
 'person_030': 29,
 'person_031': 30,
 'person_032': 31,
 'person_033': 32,
 'person_034': 33,
 'person_035': 34,
 'person_036': 35,
 'person_037': 36,
 'person_038': 37,
 'person_039': 38,
 'person_040': 39,
 'person_041': 40,
 'person_042': 41,
 'person_043': 42,
 'person_044': 43,
 'person_045': 44,
 'person_046': 45,
 'person_047': 46,
 'person_048': 47,
 'person_049': 48,
 'person_050': 49,
 'person_051': 50,
 'person_052': 51,
 'person_053': 52,
 'person_054': 53,
 'person_055': 54,
 'person_056': 55,
 'person_057': 56,
 'person_058': 57,
 'person_059': 58,
 'person_060': 59,
 'person_061': 60,
 'person_062': 61,
 'person_063': 62,
 'person_064': 63,
 'person_065': 64,
 'person_066': 65,
 'person_067': 66,
 'person_068': 67,
 'person_069': 68,
 'person_070': 69,
 'person_071': 70,
 'person_072': 71,
 'person_073': 72,
 'person_074': 73,
 'person_075': 74,
 'person_076': 75,
 'person_077': 76,
 'person_078': 77,
 'person_079': 78,
 'person_080': 79,
 'person_081': 80,
 'person_082': 81,
 'person_083': 82,
 'person_084': 83,
 'person_085': 84,
 'person_086': 85,
 'person_087': 86,
 'person_088': 87,
 'person_089': 88,
 'person_090': 89,
 'person_091': 90,
 'person_092': 91,
 'person_093': 92,
 'person_094': 93,
 'person_095': 94,
 'person_096': 95,
 'person_097': 96,
 'person_098': 97,
 'person_099': 98,
 'person_100': 99,
 'person_101': 100,
 'person_102': 101,
 'person_103': 102,
 'person_104': 103,
 'person_105': 104,
 'person_106': 105,
 'person_107': 106,
 'person_108': 107,
 'person_109': 108,
 'person_110': 109,
 'person_111': 110,
 'person_112': 111,
 'person_113': 112,
 'person_114': 113,
 'person_115': 114,
 'person_116': 115,
 'person_117': 116,
 'person_118': 117,
 'person_119': 118,
 'person_120': 119,
 'person_121': 120,
 'person_122': 121,
 'person_123': 122,
 'person_124': 123,
 'person_125': 124,
 'person_126': 125,
 'person_127': 126,
 'person_128': 127,
 'person_129': 128,
 'person_130': 129,
 'person_131': 130,
 'person_132': 131,
 'person_133': 132,
 'person_134': 133,
 'person_135': 134,
 'person_136': 135,
 'person_137': 136,
 'person_138': 137,
 'person_139': 138,}

#app
import subprocess


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print('down-'+percentage_of_completion)

@app.route('/')
def index():
  return render_template('index.html')
@app.route('/model' , methods=['POST'])
def model():
  data="as"

  if flask.request.method == 'POST':
    username = flask.request.values.get('data') 
    image_path = username
    try:
      image_data = keras.preprocessing.image.load_img(image_path, target_size=(224,224))
      image_array = keras.preprocessing.image.img_to_array(image_data)


      image_array = np.expand_dims(image_array, axis=0)

      # Make prediction
      prediction = loaded_model.predict(image_array)
      predicted_label = np.argmax(prediction, axis=1)
      original_label = list(label_to_id.keys())[list(label_to_id.values()).index(predicted_label[0])]
      probability = np.argmax(prediction, axis=-1)
      print(prediction[0][probability])
      if((prediction[0][probability])<0.8):
        data = {"data":"Bad Image", "message":"Alert! Image you have provided is not seen before"}
      else:
        data = {"data":original_label, "message":"Congratulations! Our model has successfully predicted the person."}
    except:
      data = {"data":"Enter Valid Path","message":"Unfortunately! Image path that you have provided is not working"}

  return render_template('model.html', data=data)
if __name__ == "__main__":
  app.run(debug=True)