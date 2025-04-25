import tensorflow as tf
import numpy as np
import pandas as pd

# 加载训练好的模型
model = tf.keras.models.load_model('models/environment_model.h5')

def predict_action(temperature, humidity, soil_moisture):
    input_data = np.array([[temperature, humidity, soil_moisture]])
    prediction = model.predict(input_data)
    return prediction[0]  # 返回决策
