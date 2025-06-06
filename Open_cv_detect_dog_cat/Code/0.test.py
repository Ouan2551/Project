import cv2
import os
import canaro
import caer
import tensorflow as tf
from tensorflow.keras.utils import to_categorical #type: ignore
from tensorflow.keras.callbacks import LearningRateScheduler #type: ignore

image_size = (80, 80)
char_path = r""
char_dict = {}
channels = 1

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

train = caer.preprocess_from_dir(DIR=char_path, classes=characters, IMG_SIZE=image_size, channels=channels, isShuffle=True)

feature_set, labels = caer.sep_train(train, IMG_SIZE=image_size)
feature_set = caer.normalize(feature_set)
labels = to_categorical(labels, len(train))

x_train, x_val, labels_train, labels_val = caer.train_val_split(X=feature_set, y=labels, val_ratio=0.2)

data_gen = canaro.generators.imageDataGenerator()
batch_sizes = 16
epoch = 200
train_gen = data_gen.flow(x_train, labels_train, batch_sizes)
model = canaro.createSimpsonsModel(IMG_SIZE=image_size, channels=channels, output_dim=len(characters), loss='binary_crossentropy',
                                decay=1e-16, learning_rate=0.001, momentum=0.9, nesterov=True)

callback_list = [LearningRateScheduler(canaro.lr_schedule)]

training = model.fit(train_gen)