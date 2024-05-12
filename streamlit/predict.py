# Imports
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
from typing import Tuple

# Functions
def predict_disease(image: Image.Image) -> Tuple[str, float]:

    # Load the model
    model = load_model("../models/model_pretrained_10.h5")

    # Preprocess the image
    image = image.resize((256, 256))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image = np.expand_dims(image/255.0, axis=0) # Normalization (same as in training) and adding a dimension for the batch

    prediction = model.predict(image)

    # Classes based on `train_data.class_names` from the notebooks
    classes = ["Bacterial Spot",
               "Early Blight",
               "Late Blight",
               "Leaf Mold",
               "Septoria Leaf Spot",
               "Spider Mites",
               "Target Spot",
               "Yellow Leaf Curl Virus",
               "Mosaic Virus",
               "Healthy"]
    
    prediction_class = classes[np.argmax(prediction)]
    return prediction_class, np.max(prediction)
