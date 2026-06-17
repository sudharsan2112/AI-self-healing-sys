from tensorflow.keras.models import load_model
import joblib
import numpy as np

model = load_model('ann_model.h5')
vectorizer = joblib.load('vectorizer.pkl')
encoder = joblib.load('label_encoder.pkl')

def predict_error(log_message):
    vector = vectorizer.transform([log_message]).toarray()
    prediction = model.predict(vector)

    class_index = np.argmax(prediction)
    label = encoder.inverse_transform([class_index])[0]

    return label
