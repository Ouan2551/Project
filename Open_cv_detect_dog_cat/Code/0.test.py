import cv2
import numpy as np
import canaro
import os
import tensorflow as tf
import caer
from tensorflow.keras.utils import to_categorical #type: ignore
from tensorflow.keras.callbacks import LearningRateScheduler #type: ignore

images = [80, 80]
char_path = r""
channels = 1

characters = {}
for i in os.listdir(char_path):
    characters[i] = len(os.listdir(os.path.join(char_path, i)))
    
characters = caer.sort_dict(characters, descending=True)

for i in characters:
    path = os.path.join(char_path, i)
    for img_name in os.listdir(path):
        fullpath = os.path.join(path, img_name)
        image = cv2.imread(fullpath)
        if image is None:
            print("error : ", fullpath)

train = caer.preprocess_from_dir(DIR=char_path, classes=characters, channels=channels, IMG_SIZE=images, isShuffle=True)

feature_set, labels = caer.sep_train(train, IMG_SIZE=image)
feature_set = caer.normalize(feature_set)
labels = to_categorical(labels, len(characters))