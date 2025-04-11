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
# import random # use for skip function train data in "load_data" function
# setup image size, channels, character_path
image_size = (80, 80)
channels = 1
character_path = r"D:\Important files Nannaphat\coding\Project\Open_cv_detect_dog_cat\Data"

# import all name character to character_dict
character_dict = {}
for char in os.listdir(character_path):
    character_dict[char] = len(os.listdir(os.path.join(character_path, char)))

for i in character_dict:
    print(character_dict[i])
# sort name
character_dict = caer.sort_dict(character_dict, descending=True)
print(character_dict)

# get characters (i use all of them)
characters = []
count = 0
for char in character_dict:
    characters.append(char[0])
    count += 1
print(characters)

# Test if all image paths are valid
for cls in characters:
    path = os.path.join(character_path, cls)
    for img_name in os.listdir(path):
        full_path = os.path.join(path, img_name)
        img = cv2.imread(full_path)
        if img is None:
            print("Unreadable image:", full_path)

# ------------------------------------------------------------------
# creat training data (not skip some picture that can't read)
train = caer.preprocess_from_dir(DIR=character_path, classes=characters, channels=channels, IMG_SIZE=image_size, isShuffle=True)
print("picture count : ", len(train))

# use this instead for skip picture
# def load_data(character_path, characters, image_size, channels=1):
#     data = []

#     for label, cls in enumerate(characters):
#         path = os.path.join(character_path, cls)
#         for img_name in os.listdir(path):
#             full_path = os.path.join(path, img_name)

#             try:
#                 # Read image
#                 img = cv2.imread(full_path)

#                 if img is None or img.size == 0:
#                     print("Skipping unreadable image:", full_path)
#                     continue

#                 # Convert to grayscale if needed
#                 if channels == 1:
#                     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#                 # Resize image
#                 img = cv2.resize(img, image_size)

#                 data.append([img, label])

#             except Exception as e:
#                 print(f"Error reading {full_path}: {e}")
#                 continue

#     return caer.shuffle(data)

# Replace this:
# train = caer.preprocess_from_dir(DIR=character_path, classes=characters, channels=channels, IMG_SIZE=image_size, isShuffle=True)

# With this:
# train = load_data(character_path, characters, image_size, channels=channels)
# print("picture count:", len(train))
# ------------------------------------------------------------------

# visualize some image in data set
plt.figure(figsize=(30, 30))
plt.imshow(train[0][0], cmap='gray')
plt.show()

# prepare data before training
featureSet, labels = caer.sep_train(train, IMG_SIZE=image_size)
featureSet = caer.normalize(featureSet)
labels = to_categorical(labels, len(characters))

# splitting data into training and validation set
x_train, x_val, y_train, y_val = caer.train_val_split(X=featureSet, y=labels, val_ratio=.2)

# image data generator
data_gen = canaro.generators.imageDataGenerator()
BATCH_SIZES = 32
EPOCHS_val = 100
# train_gen = data_gen.flow(x_train, y_train, BATCH_SIZE = BATCH_SIZES)
train_gen = data_gen.flow(x_train, y_train, BATCH_SIZES)

# creat cnn
model = canaro.models.createSimpsonsModel(IMG_SIZE=image_size, channels=channels, output_dim=len(characters), loss='binary_crossentropy',
                                        decay=1e-6, learning_rate=0.001, momentum=0.9, nesterov=True)
print("______________________________________")
model.summary()

# callback and training section
callback_list = [LearningRateScheduler(canaro.lr_schedule)]

# train model
training = model.fit(train_gen, steps_per_epoch = len(x_train//BATCH_SIZES), EPOCHS = EPOCHS_val, validation_data = (x_val, y_val),
                    validation_steps = len(y_val)//BATCH_SIZES, callbacks = callback_list)