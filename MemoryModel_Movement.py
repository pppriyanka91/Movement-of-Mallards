# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 12:09:44 2022

@author: eid
"""

# Representation of Mallars' memory for moving

import numpy
from numpy import hstack
from numpy import array
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Conv1D
from tensorflow.keras.layers import MaxPooling1D

EPOCHS = 100
N_STEPS = 10

class MovementMemory():
    
    def __init__(self):

        pass
    
    def set_dataset(self):
        data = numpy.genfromtxt("AdjustedTag3.csv", delimiter=',')
        lat = list()
        long = list()
        i = 1
        for rows in data:
            lat.append(rows[2]* 1000 -56400.0)
            long.append(rows[3]*1000 - 13900.0)
            i = i + 1
            pass
        seq_lat = array(lat)
        seq_long = array(long)
        seq_lat = seq_lat.reshape((len(seq_lat), 1))
        seq_long = seq_long.reshape((len(seq_long), 1))

        dataset = hstack((seq_lat, seq_long))
        return dataset
    
    # split a multivariate sequence into samples
    def split_sequences(self, sequences, n_steps):
        X, y = list(), list()
        for i in range(len(sequences)):
             end_ix = i + n_steps

             if end_ix > len(sequences)-1:
                 break

             seq_x, seq_y = sequences[i:end_ix, :], sequences[end_ix, :]

             X.append(seq_x)
             y.append(seq_y)
        return array(X), array(y)   
    
    def train_model(self):
        n_steps = N_STEPS
        dataset = self.set_dataset()
        X, y = self.split_sequences(dataset, n_steps)
        
        n_features = X.shape[2]
        print("N_Features ", n_features)
        # define model
        model = Sequential()
        model.add(Conv1D(filters=128, kernel_size=2, activation='relu', input_shape=(n_steps, n_features)))
        model.add(MaxPooling1D(pool_size=2, strides = 1, padding = 'same' ))
        model.add(Flatten())
        model.add(Dense(1000, activation='relu'))
        model.add(Dense(n_features))
        model.compile(optimizer='adam', loss='mse')
        
        # fit model
        model.fit(X, y, epochs=EPOCHS, verbose=0)
        return model
    
   