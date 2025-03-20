import cv2
import numpy as np
import os
import canaro
import caer
import gc

# change image size before process
image_size = (80, 80) # best value for data set
channels = 1
char_path = r''