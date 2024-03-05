import numpy as np
import streamlit as st
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

model = load_model('C:\\Users\\aloky\\OneDrive\\Desktop\\Marine_Classification\\Models\\Classification\\marine_model.h5')

class_names = ['Bangus', 'Big Head Carp', 'Black Spotted Barb', 'Catfish', 'Climbing Perch', 'Fourfinger Threadfin', 'Fresherwater Eel', 'Glass Perchlet', 'Goby', 
               'Gold Fish', 'Gourami', 'Grass Crap', 'Green Spotted Puffer', 'Indian Carp', 'Indo Pacific Tarpon', 'Jaguar Fish', 'Janitor Fish', 'Knifefish',
               'Long Snouted Pipefish', 'Mosquito Fish', 'Mudfish', 'Mullet', 'Pangasius', 'Perch', 'Scat Fish', 'Silver Barb', 'Silver Carp', 'Silver Perch', 
               'Snakehead', 'Tenpounder', 'Tilapia']

dangerous_species = ['Green Spotted Puffer', 'Jaguar Fish', 'Janitor Fish', 'Knifefish', 'Long Snouted Pipefish', 'Mosquito Fish', 'Mudfish', 'Snakehead']

st.title('Explore Fishes')
st.markdown('Upload an image of the fish')

fish_image = st.file_uploader("Choose an image", type='jpg')

if fish_image is not None:
    st.image(fish_image, caption='Selected Image', use_column_width=True)
    submit = st.button('Predict')

    if submit:
        file_bytes = np.asarray(bytearray(fish_image.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        opencv_image = cv2.resize(opencv_image, (224, 224))
        opencv_image = preprocess_input(opencv_image) 
        opencv_image = np.expand_dims(opencv_image, axis=0)

        y_pred = model.predict(opencv_image)
        result = class_names[np.argmax(y_pred)]

        st.title(result)

        if result in dangerous_species:
            st.warning(f'The predicted species "{result}" is considered dangerous.')
        else:
            st.info(f'The predicted species "{result}" is not considered dangerous.')
