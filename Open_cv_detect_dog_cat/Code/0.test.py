import cv2
import numpy as np
import os
import caer
import canaro
import tensorflow as tf
from tensorflow.keras.utils import to_categorical #type: ignore
from tensorflow.keras.callbacks import LearningRateScheduler #type: ignore

char_path = r""
channels = 1
picture = [80, 80]
char_dict = {}

for i in os.listdir(char_path):
    char_dict[i] = len(os.listdir(os.path.join(char_path, i)))

char_dict = caer.sort_dict(char_dict, descending=True)

characters = []
for i in char_dict:
    characters.append(i[0])

for i in characters:
    path = os.path.join(char_path, i)
    for j in os.listdir(path):
        path_picture = os.path.join(path, j)
        picture = cv2.imread(path_picture)
        if picture is None:
            cv2.imshow("error image : ", path_picture)

train = caer.preprocess_from_dir(DIR=char_path, classes=characters, IMG_SIZE=picture, channels=channels, isShuffle=True)

feature_set, labels = caer.sep_train(data=train, IMG_SIZE=picture)
labels = caer.normalize(labels)
feature_set = caer.to_categorical(feature_set)