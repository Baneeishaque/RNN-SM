#!/usr/bin/env python
# -*-coding:utf-8 -*-

'''
Implementation of our pruned RNN-SM algorithm
-------------
Based on paper:
    RNN-SM: Fast Steganalysis of VoIP Streams Using Recurrent Neural Network
-------------
Author: Zinan Lin
Email:  zinanl@andrew.cmu.edu
'''

import numpy as np
import os, pickle, random, datetime

os.environ['KERAS_BACKEND'] = 'theano'
from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM, Reshape, Flatten

FOLDERS = [
    # The folder that contains positive data files.
    {"class": 1, "folder": "g729a_Steg"},
    # The folder that contains negative data files.
    {"class": 0, "folder": "g729a_0"}
]

SAMPLE_LENGTH = 10000  # The sample length (ms)
BATCH_SIZE = 32  # batch size
ITER = 30  # number of iteration
FOLD = 5  # = NUM_SAMPLE / number of testing samples

'''
Get the paths of all files in the folder
'''


def get_file_list(local_folder):
    file_list = []
    for fileItem in os.listdir(local_folder):
        file_list.append(os.path.join(local_folder, fileItem))
    return file_list


'''
Read codeword file
-------------
input
    file_path
        The path to an ASCII file.
        Each line contains three integers: x1 x2 x3, which are the three codewords of the frame.
        There are (number of frame) lines in total. 
output
    the list of codewords
'''


def parse_sample(file_path):
    local_file = open(file_path, 'r')
    lines = local_file.readlines()
    sample = []
    for line in lines:
        line_split = line.strip("\r\n\t").strip().split("\t")
        sample.append(line_split)
    return sample


'''
Save variable in pickle
'''


def save_variable(file_name, variable):
    file_object = open(file_name, "wb")
    pickle.dump(variable, file_object)
    file_object.close()


'''
Pruned RNN-SM training and testing
'''
if __name__ == '__main__':
    all_files = []
    for folder in FOLDERS:
        for item in get_file_list(folder["folder"]):
            all_files.append((item, folder["class"]))

    print("Sample Data : " + str(all_files[0]))
    print("Sample Data : " + str(all_files[1]))
    
    random.shuffle(all_files)
    
    # print("Sample Data After Random : " + str(all_files[0]))
    # print("Sample Data After Random : " + str(all_files[1]))
    
    save_variable('all_files.pkl', all_files)

    all_samples_x = []
    for item in all_files:
        all_samples_x.append((parse_sample(item[0])))

    all_samples_y = []
    for item in all_files:
        all_samples_y.append(item[1])

    print("Sample Data X : " + str(all_samples_x[0]))
    print("Sample Data Y : " + str(all_samples_y[0]))

    # print("Sample Data X : " + str(all_samples_x[1]))
    # print("Sample Data Y : " + str(all_samples_y[1]))

    np_all_samples_x = np.asarray(all_samples_x)
    np_all_samples_y = np.asarray(all_samples_y)

    # print("Sample Data Numpy X : " + str(np_all_samples_x[0]))
    # print("Sample Data Numpy Y : " + str(np_all_samples_y[0]))

    # print("Sample Data Numpy X : " + str(np_all_samples_x[1]))
    # print("Sample Data Numpy Y : " + str(np_all_samples_y[1]))

    save_variable('np_all_samples_x.pkl', np_all_samples_x)
    save_variable('np_all_samples_y.pkl', np_all_samples_y)

    file_num = len(all_files)
    print("Total Files : " + str(file_num))
    
    sub_file_num = int(file_num / FOLD)
    print("Test Files : " + str(sub_file_num))

    x_test = np_all_samples_x[0: sub_file_num]  # The samples for testing
    y_test = np_all_samples_y[0: sub_file_num]  # The label of the samples for testing

    # print("Sample Test X : " + str(x_test[0]))
    # print("Sample Test Y : " + str(y_test[0]))

    # print("Sample Test X : " + str(x_test[1]))
    # print("Sample Test Y : " + str(y_test[1]))

    x_train = np_all_samples_x[sub_file_num: file_num]  # The samples for training
    y_train = np_all_samples_y[sub_file_num: file_num]  # The label of the samples for training

    # print("Sample Train X : " + str(x_train[0]))
    # print("Sample Train Y : " + str(y_train[0]))

    # print("Sample Train X : " + str(x_train[1]))
    # print("Sample Train Y : " + str(y_train[1]))

    time_steps=int(SAMPLE_LENGTH / 10)
    print("Time Steps : " + str(time_steps))

    data_dimension=3
    print("Data Dimension : " + str(data_dimension))

    print("Building model")
    model = Sequential()
    model.add(LSTM(50, input_shape=(time_steps, data_dimension), return_sequences=True))  # first layer
    # model.summary()
    model.add(LSTM(50))  # second layer
    # model.summary()
    model.add(Dense(1))  # output layer
    # model.summary()
    model.add(Activation('sigmoid'))  # activation function
    # model.summary()

    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=["accuracy"])

    # print("Model Input Layer Shapes")
    # print("-------------------------")
    # for layer in model.layers:
    #     print(layer.input_shape)

    # print("Dimen Train X : " + str(x_train.ndim))
    # print("Shape Train X : " + str(x_train.shape))
    
    # print("Train X")
    # print("--------")
    # print(x_train)

    # print("Dimen Train Y : " + str(y_train.ndim))
    # print("Shape Train Y : " + str(y_train.shape))
    
    # x_train=x_train.reshape(x_train.shape[0]/(time_steps*data_dimension),time_steps,data_dimension)
    # y_train=y_train.reshape(y_train.shape[0]/(time_steps*data_dimension),time_steps,data_dimension)

    # print("Dimen Train X Reshape : " + str(x_train.ndim))
    # print("Shape Train X Reshape : " + str(x_train.shape))

    # print("Dimen Train Y Reshape : " + str(y_train.ndim))
    # print("Shape Train Y Reshape : " + str(y_train.shape))

    # print("Sample Train X : " + str(x_train[0]))
    # print("Sample Train X : " + str(x_train[1]))
    
    print("Training")
    for i in range(ITER):
        model.fit(x_train, y_train, batch_size=BATCH_SIZE, nb_epoch=1, validation_data=(x_test, y_test))
        model.save('model_%d.h5' % (i + 1))
