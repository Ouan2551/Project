import cv2
import numpy as np
import caer
import canaro
import tensorflow as tf
import os
from tensorflow.keras.utils import to_categorical #type: ignore
from tensorflow.keras.callbacks import LearningRateScheduler #type: ignore

char_path = r""
image_size = (80,80)
channels = 1
char_dict = {}

for i in os.listdir(char_path):
    char_dict[i] = len(os.listdir(os.path.join(char_path, i)))

char_dict = caer.sort_dict(char_dict, descending=True)

characters = []
for i in char_dict:
    characters.append(i[0])

for i in os.listdir(char_path):
    path = os.path.join(char_path, i)
    for j in os.listdir(path):
        path_image = os.path.join(path, j)
        image = cv2.imread(path_image)
        if image is None:
            cv2.imshow("can't read image : ", path_image)

train = caer.preprocess_from_dir(DIR=char_dict, classes=characters, IMG_SIZE=image_size, channels=channels, isShuffle=True)

feature_set, labels = caer.sep_train(train, IMG_SIZE=image_size)
feature_set = caer.normalize(feature_set)
labels = to_categorical(labels, len(train))

x_train, x_val, labels_train, labels_val = caer.train_val_split(X=feature_set, y=labels, val_ratio=0.2)

data_gen = canaro.generators.imageDataGenerator()
batch_size = 50
epochs_val = 200
train_gen = data_gen.flow(x_train, labels_train, batch_size)

model = canaro.models.createSimpsonsModel(IMG_SIZE=image_size, channels=channels, output_dim=len(characters), loss='binary_crossentropy',
                                        decay=1e-6, learning_rate=0.001, momentum=0.9, nesterov=True)
model.summary()

callbacks_list = [LearningRateScheduler(canaro.lr_schedule)]
training = model.fit(train_gen, steps_per_epoch = len(x_train//batch_size), epochs = epochs_val, validation_data = (x_val, labels_val)
                    , validation_steps = len(x_val//batch_size), callbacks = callbacks_list)