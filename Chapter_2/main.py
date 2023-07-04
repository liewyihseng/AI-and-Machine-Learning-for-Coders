import keras
import tensorflow as tf
from keras import Sequential
from keras.layers import Dense


class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get('accuracy') > 0.95:
            print("\nReached 95% so stopping training")
            self.model.stop_training = True


data = tf.keras.datasets.fashion_mnist

callbacks = myCallback()

(training_images, training_labels), (test_images, test_labels) = data.load_data()
training_images = training_images / 255.0
test_images = test_images / 255.0

model = Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    Dense(units=128, activation=tf.nn.relu),
    Dense(units=10, activation=tf.nn.softmax)
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=50, callbacks=[callbacks])

model.evaluate(test_images, test_labels)

classifications = model.predict(test_images)
print(classifications[0])
print(test_labels[0])
