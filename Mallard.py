# -*- coding: utf-8 -*-
"""
Created on Fri Aug  5 12:54:39 2022

@author: eid
"""

import numpy
from numpy import hstack
from numpy import array

from MemoryModel_Movement import MovementMemory

class Mallard():    
    
    N_STEPS = 10
    N_FEATURES = 2
    memory = None
    current_pos = None
    current_history = None
    
    def __init__(self):
        memory_Model = MovementMemory()

        self.memory = memory_Model.train_model()
        pass
    
    def print_curr_hist(self):
        
        print("MALLARD CURR HIST")
        print(self.current_history)
        pass
    
    def set_new_history(self, pos):
        
        h = self.current_history
        for i in range(self.N_STEPS - 1):
            h[i] = h[i+1]
            pass
        h[self.N_STEPS - 1] = pos
        
        pass
    
        
    
    def get_current_pos(self):
        
        n_steps = self.N_STEPS
        n_features = self.N_FEATURES
        h = self.current_history
        tmparr = list()
        for j in range(n_steps):
            tmparr.append(h[j])
        x_input = array(tmparr)
        x_input = x_input.reshape((1, n_steps, n_features))
        yhat = self.memory.predict(x_input, verbose=0)
        self.set_new_history(yhat)
        return yhat
        pass
    
    def set_first_pos(self, first_pos):
        
        lat = list()
        long = list()
        x = first_pos[0] * 1000 - 56400.0
        y = first_pos[1] * 1000 - 13900.0
        for i in range(10):
            lat.append(x)
            long.append(y)
            pass
        
        a_lat = array(lat)
        a_long = array(long)
        a_lat = a_lat.reshape(len(a_lat), 1)
        a_long = a_long.reshape(len(a_long), 1)
        hstack_lat_long = hstack((a_lat, a_long))


        self.current_history = hstack_lat_long
        self.current_pos = self.get_current_pos()
        

        pass

    def set_dataset(self):
        data = numpy.genfromtxt("AdjustedTag3.csv", delimiter=',')
        lat = list()
        long = list()
    #        dist = list()
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
    
    def check_training_results(self, dataset, model):
    #        data = self.getData()
    
        n_steps = self.N_STEPS
        n_features = 2
        result = list()
        print("NEW AVLUES")
        for i in range(len(dataset)-(1+n_steps)):
            tmparr = list()
            for j in range(n_steps):
                tmparr.append(dataset[i+j])

            x_input = array(tmparr)
            x_input = x_input.reshape((1, n_steps, n_features))
            yhat = model.predict(x_input, verbose=0)
            result.append(yhat[0])

            pass
    
        pass
    
    def move(self):
        
        self.current_pos = self.get_current_pos()
        print("CURR POS : ", self.current_pos)
        
        pass
    
    def change(self):
        
        pass
    
    pass


