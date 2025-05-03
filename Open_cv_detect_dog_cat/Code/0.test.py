import cv2
import numpy as np
import os
import caer
import canaro
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.utils import to_categorical #type: ignore
from tensorflow.keras.callbacks import LearningRateSchedule #type: ignore

image_size = [80,80]
channels = 1
char_path = r""

