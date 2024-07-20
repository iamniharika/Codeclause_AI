import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_AVX2_FMA'] = '0'
import numpy as np
import cv2
import matplotlib.pyplot as plt

import tensorflow as tf
# print("TensorFlow version:", tf.__version__)

# mnist = tf.keras.datasets.mnist
# (x_train , y_train), (x_test , y_test) = mnist.load_data()

# x_train = tf.keras.utils.normalize(x_train , axis=1)
# x_test = tf.keras.utils.normalize(x_test , axis=1)

# model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
# model.add(tf.keras.layers.Dense(128 , activation='relu'))
# model.add(tf.keras.layers.Dense(128 , activation='relu'))
# model.add(tf.keras.layers.Dense(10 , activation='softmax'))

# model.compile(optimizer = 'adam' , loss= 'sparse_categorical_crossentropy')

# model.fit(x_train , y_train , epochs = 100)
# model.save('recognize.keras')

model = tf.keras.models.load_model('recognize.keras')
# print("Model loaded:", model)

img_no = 1
while os.path.isfile(f"digitis\\digit{img_no}.png"):
    img = cv2.imread(f"digitis\\digit{img_no}.png", cv2.IMREAD_GRAYSCALE)
    img = np.invert(np.array([img])) /255  # Normalize the image
    img = img.reshape((1, 28, 28))  # Reshape the image to match the model's input shape
    prediction = model.predict(img)
    print("The handwriting predicted is - ", np.argmax(prediction))
    plt.imshow(img[0], cmap='gray')  # Use cmap='gray' to display grayscale images
    plt.show()
    img_no += 1