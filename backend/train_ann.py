import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
import joblib

df = pd.read_csv("error_dataset.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df['message']).toarray()

encoder = LabelEncoder()
y = encoder.fit_transform(df['label'])
y_cat = to_categorical(y)

joblib.dump(vectorizer, 'vectorizer.pkl')
joblib.dump(encoder, 'label_encoder.pkl')

model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(y_cat.shape[1], activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(X, y_cat, epochs=20, verbose=1)

model.save('ann_model.h5')

print("ANN trained successfully")
