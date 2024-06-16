import cv2
import numpy as np
import Constants
import openai
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input

openai.api_key = Constants.api_key

class_names = Constants.class_names
model_path = Constants.model_path
model = load_model(model_path)

def classify(file):
    file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
    opencv_image = cv2.imdecode(file_bytes, 1)
    opencv_image = cv2.resize(opencv_image, (224, 224))
    opencv_image = preprocess_input(opencv_image)
    opencv_image = np.expand_dims(opencv_image, axis=0)

    y_pred = model.predict(opencv_image)

    result = class_names[np.argmax(y_pred)]
    likelihood = np.max(y_pred)  
    result_details = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=f"Is the fish species '{result}' poisonous? Provide details on its toxicity. If it has even a small amount of poison, declare it as poisonous.",
        max_tokens=200
    )
    result_details = result_details.choices[0].text.strip()

    is_poisonous = "poisonous" in result_details.lower()

    label = "poisonous" if is_poisonous else "safe"
    likelihood_percentage = likelihood * 100 

    analysis = f"""
    | Label | Possibility |
    |---|---|
    | {label} | {likelihood_percentage:.1f}% |

    **Explanation**:
    Based on the analysis, the fish species '{result}' is labeled as '{label}' with a likelihood of {likelihood_percentage:.1f}%.
    {result_details}

    If you have any follow-up questions, please feel free to ask!
    """

    return analysis

