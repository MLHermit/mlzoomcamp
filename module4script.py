import pandas as pd
import numpy as np
import pickle as pkl
from flask import Flask, request, jsonify
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
 
with open(r"C:\Users\Abdullahi Mujaheed\Desktop\mlzoom\mlzoomcamp\models.bin", 'rb') as f_in:
    vect, model = pkl.load(f_in)

app = Flask('first_deploy')

@app.route('/deployment', methods = ['POST'])
def transform_predict():
    data = request.get_json
    try:
        train_dict = vect.transform(data).toarray()
        output = model.predict(train_dict)

        return jsonify({'predictions': output.tolist()})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug= True, host= '0.0.0.0', port = 9999)