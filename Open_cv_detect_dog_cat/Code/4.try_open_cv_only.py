import cv2
import numpy as np
import os
import caer
import gc
import canaro
import scipy
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.utils import to_categorical # type: ignore
from tensorflow.keras.callbacks import LearningRateScheduler # type: ignore

# setup image size, channels, character_path
image_size = (80, 80)
channels = 1
character_path = 