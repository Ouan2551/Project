import cv2
import numpy as np
import os
import caer
import gc
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import LearningRateScheduler
import canaro
import scipy

# change image size before process
image_size = (80, 80) # best value for data set
channels = 1
# path file picture for train
char_path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\17.Deep_computer_vision(simpsons)\simpsons_data_set\simpsons_dataset'

# input all name simpsons family
char_dict = {}
for char in os.listdir(char_path):
    char_dict[char] = len(os.listdir(os.path.join(char_path, char)))
# The `for i in char_dict:` loop is iterating over the keys of the `char_dict` dictionary. In each
# iteration, `i` represents a key in the dictionary, which in this case is the name of a character
# from the Simpsons family. This loop is used to extract the character names and process them further
# in the code.
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
# use tensorflow library
labels = to_categorical(labels, len(characters))

# training and validation data => model train and test yourself on this
x_train, x_val, y_train, y_val = caer.train_val_split(X=featureSet, y=labels, val_ratio=.2)
# at val_ratio = .2 mean 20% of data go to validation set, 80% of data to training set

# delete some data will not use again (but I not want to remove)
# del train
# del featureSet
# del labels
# gc.collect()

# Image data generator => made some of random data
data_gen = canaro.generators.imageDataGenerator()
BATCH_SIZE = 32
EPOCHS = 10
train_gen = data_gen.flow(x_train, y_train, batch_size = BATCH_SIZE)

# Creating model
model = canaro.models.createSimpsonsModel(IMG_SIZE=image_size, channels=channels, output_dim=len(characters)
                                        , loss='binary_crossentropy', decay=1e-6, learning_rate=0.001,
                                        momentum=0.9, nesterov=True)
print("____________________________________")
model.summary()

# creat callback list => contain something like learning rate
callbacks_list = [LearningRateScheduler(canaro.lr_schedule)]

# train model
training = model.fit(train_gen, steps_per_epoch=len(x_train//BATCH_SIZE), epochs=EPOCHS, validation_data = (x_val, y_val),
                    validation_steps = len(y_val)//BATCH_SIZE, callbacks = callbacks_list)

# test how good of model
test_path = r'D:\Important files Nannaphat\coding\Project\Machine_Learning\python+opencv\tutorial_youtube\17.Deep_computer_vision(simpsons)\simpsons_data_set\kaggle_simpson_testset\kaggle_simpson_testset\abraham_grampa_simpson_0.jpg'
image_test = cv2.imread(test_path)
# change image_test to make it how you change and prepare for data set
def prepare(image=image_test):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, dsize=image_size)
    image = caer.reshape(image, IMG_SIZE=image_size, channels=1)
    return image

# predict image
prediction = model.predict(prepare(image_test)) # call function prepare image
print(prediction)
print(characters[np.argmax(prediction[0])]) # this line use for get real value not like array from prediction