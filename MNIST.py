import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import cv2
import tensorflow as tf
import os

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis = 1) #x_train = (60,000, 28, 28)
x_test = tf.keras.utils.normalize(x_test, axis = 1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape= (28,28)))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(128, activation='relu'))
model.add(tf.keras.layers.Dense(10,activation="softmax"))

model.compile(optimizer= 'adam', loss = 'sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs = 3)

image_number = 0

while os.path.isfile(f"nural nine/{image_number}.jpg"):
    try:
        img = cv2.imread(f"nural nine/{image_number}.jpg")[:,:,0]
        img = np.invert(np.array([img]))
        prediction = model.predict(img)
        print(f"This digit is probably a {np.argmax(prediction)}")
        plt.imshow(img[0], cmap=plt.cm.binary)
        plt.show()
    except:
        print("Error")
    finally:
        image_number += 1

loss,accuracy = model.evaluate(x_test,y_test)
print(loss)
print(accuracy)
