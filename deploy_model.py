from flask import Flask,render_template,request,redirect,url_for,send_from_directory
import tensorflow as tf
import os
import cv2
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import numpy as np

model = tf.keras.models.load_model('Resource/TF_DOG_CAT.h5')
result = {0:'CAT',1:'DOG'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = r'C:\Users\vishal verma\PycharmProjects\Flask\Resource\Upload'

@app.route('/prediction/<filename>')
def make_prediction(filename):
    #filename = filename
    image = cv2.imread(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    image = cv2.resize(image,(160,160))
    img_array = img_to_array(image)
    image_np = preprocess_input(img_array)

    image_np = np.expand_dims(image_np, axis=0) #
    prediction = model.predict(image_np)
    return render_template('result.html', filename=filename,pred = result[prediction[0][0]])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/uploader',methods = ['GET','POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        return redirect(url_for('make_prediction', filename=f.filename))

@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__=='__main__':
    app.run(debug=True)