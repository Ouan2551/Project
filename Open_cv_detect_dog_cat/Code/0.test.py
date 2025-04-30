import cv2
import os
import caer
import tensorflow as tf
import numpy as np
import gc
import canaro
import scipy
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical #type: ignore
from tensorflow.keras.callbacks import LearningRateScheduler #type: ignore

image = [80,80]
channels = 1
char_path = r"C:\Important files Nannaphat\coding\Project\Open_cv_detect_dog_cat\Data"

char_dict = {}
for char in os.listdir(char_path):
    char_dict[char] = len(os.listdir(os.path.join(char_path, char)))

char_dict = caer.sort_dict(char_dict, descending=True)
# print(char_dict)

characters = {}
for i in char_dict:
    characters[i] = i[0]

print(characters)