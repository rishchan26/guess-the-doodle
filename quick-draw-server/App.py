import flask
from flask_cors import CORS
from tensorflow import keras
import tensorflow as tf
import cv2
import numpy as np
import base64

app = flask.Flask(__name__)
CORS(app)

print('Loaded modules')

class_name_list = np.load('classes.npy')
class_name_list = list(class_name_list)
model = keras.models.load_model('model.h5')

def data_uri_to_cv2_img(uri):
    encoded_data = uri.split(',')[1]
    nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    return img

def preprocess_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    dst = cv2.cornerHarris(gray,2,3,0.04)
    minX = img.shape[0]
    maxX = 0
    minY = img.shape[1]
    maxY = 0
    for i in range(dst.shape[0]):
        for j in range(dst.shape[1]):
            if dst[i][j] != 0:
                minX = min(minX, i)
                maxX = max(maxX, i)
                minY = min(minY, j)
                maxY = max(maxY, j)

    X1 = minX - 20
    X2 = maxX + 20 
    Y1 = minY - 20 
    Y2 = maxY + 20
    if minX <= 20:
        X1 = 0
    if maxX >= 280:
        X2 = 300
    if minY <= 20:
        Y1 = 0
    if maxY >= 280:
        Y2 = 300
    img = img[X1:X2, Y1:Y2]
    size = max(img.shape[0], img.shape[1])
    img = cv2.resize(img, (size, size), cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype('float32')
    img = cv2.resize(img, (28, 28), cv2.INTER_AREA)
    img = 255.0 - img
    img = img.reshape(28, 28, 1)
    img = img / 255.0
    return img



def model_predict(img):
    img = np.expand_dims(img, axis=0)
    predictions = model.predict(img)
    result_dict = {}
    for p in predictions.argsort().reshape(-1)[-5:]:
        result_dict[class_name_list[p]] = predictions.reshape(-1)[p] * 100
    return result_dict

@app.route("/predict", methods=["POST"])
def predict():
    image_uri = flask.request.values['imgBase64']
    img = data_uri_to_cv2_img(image_uri)
    img = preprocess_image(img)
    print(img.shape)
    result = model_predict(img)
    return flask.jsonify(result)
# start the flask app, allow remote connections
app.run()