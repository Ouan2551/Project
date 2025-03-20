import cv2
import numpy as np
import os
import caer
import gc
import matplotlib.pyplot as plt
import tensorflow as tf

# change image size before process
image_size = (80, 80) # best value for data set
channels = 1
# path file picture for train
char_path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\17.Deep_computer_vision(simpsons)\simpsons_data_set\simpsons_dataset'

# input all name simpsons family
char_dict = {}
for char in os.listdir(char_path):
    char_dict[char] = len(os.listdir(os.path.join(char_path, char)))
for i in char_dict:
    print(char_dict[i])
    
# sort in descending order
char_dict = caer.sort_dict(char_dict, descending=True)
print(char_dict)

# gray name of character
characters = []
count = 0
for i in char_dict:
    characters.append(i[0])
    count += 1
    if count >= 10:
        break
    
print(characters)

# creat training data
train = caer.preprocess_from_dir(DIR=char_path, classes=characters, channels=channels,IMG_SIZE=image_size, isShuffle=True)

# check how many picture in train
print("picture count : ", len(train))

# visualize image in data set
# (use matplotlib not open cv because open cv not display correctly in jupyter notebook)
plt.figure(figsize=(30,30))
plt.imshow(train[0][0], cmap='gray') # select some image
plt.show()

# separate picture into features and labels
featureSet, labels = caer.sep_train(train, IMG_SIZE=image_size)

# normalize featuresSet => (0,1) (normalize for faster learn of model)
featureSet = caer.normalize(featureSet) # convert from numerical integer to binary class vector