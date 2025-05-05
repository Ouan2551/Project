import cv2
import numpy as np
import tensorflow as tf
import canaro
import os
import matplotlib.pyplot as plt
import caer
from tensorflow.keras.utils import to_categorical #type: ignore
from tensorflow.keras.callbacks import LearningRateScheduler #type: ignore

picture_size = [80, 80]
channels = 1
char_path = r""

char_dict = {}
for i in os.listdir(char_path):
    char_dict[i] = len(os.listdir(os.path.join(char_path, i)))
    
char_dict = caer.sort_dict(char_dict, descending=True)

characters = []
for i in char_dict:
    characters.append(i[0])