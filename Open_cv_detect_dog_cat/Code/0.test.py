import cv2
import numpy as np
import caer
import os
import gc
import canaro
import scipy
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical #type: ignore
from tensorflow.keras.callbacks import LearningRateScheduler #type: ignore

image_size = [80,80]
channel = 1
char_path = ""

char_dict = {}
for char in os.listdir(char_path):
    char_dict[char] = 