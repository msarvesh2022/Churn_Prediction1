from flask import Flask , render_template , request
import pandas as pd 
import numpy as np
import pickle
import os

<<<<<<< HEAD
application = Flask(__name__)
app = application
=======
application= Flask(__name__)
app=application
>>>>>>> 0d9f04e1a1acf45b0dc25ca5eba5c031d6ed1ccf


import os
import pickle

# Get the absolute path to the pkl file
pkl_file_path = os.path.join(os.path.dirname(__file__), 'churn_prediction.pkl')

# Load the model using the absolute path
model = pickle.load(open(pkl_file_path, 'rb'))





@app.route('/')

def home():
    return render_template('index.html')


@app.route('/predict',methods= ['GET','POST'])

def churn():
    
    age_var= int(request.form.get('age'))
    sex_var = request.form.get('gender')
    location_var= request.form.get('location')
    month_var = int(request.form.get('month'))
    bill_var = int(request.form.get('bill'))
    gb_var = int(request.form.get("gb"))
    
    result= model.predict([[age_var,sex_var,location_var,month_var,bill_var,gb_var]])
    output = int(result[0])
    
    if output == 1:
        return "<h1>Customer will cancel the subscription</h1>"
    else :
        return "<h1>Customer will remain</h1>"


if __name__=="__main__":

    app.run("0.0.0.0")
