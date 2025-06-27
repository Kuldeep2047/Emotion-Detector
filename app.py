import os
from flask import Flask, render_template, request, jsonify
import cv2
import numpy as np
from keras.models import load_model
import base64
import io
from PIL import Image

app = Flask(__name__)
model_path = os.path.join(os.path.dirname(__file__), "fer2013_mini_XCEPTION.102-0.66.hdf5")
model = load_model(model_path, compile=False)

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json.get('image', None)
    if not data:
        print("No image data received.")
        return jsonify({'emotion': 'Error: No image'})

    image_data = base64.b64decode(data.split(',')[1])
    image = Image.open(io.BytesIO(image_data)).convert('RGB')
    frame = np.array(image)
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    print("Face(s) detected:", len(faces))

    result = "No Face"
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_gray = cv2.resize(roi_gray, (64, 64))
        roi = roi_gray.astype("float") / 255.0
        roi = np.expand_dims(roi, axis=0)
        roi = np.expand_dims(roi, axis=-1)
        prediction = model.predict(roi, verbose=0)[0]
        result = emotion_labels[np.argmax(prediction)]
        break

    return jsonify({'emotion': result})


if __name__ == '__main__':
    app.run(debug=True)
