# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 14:38:29 2022

@author: eid
"""

from Mallard import Mallard

class Environment():
    
    def __init__(self):
        
        self.m1 = Mallard()
        self.m1.print_curr_hist()
        self.m1.set_first_pos([56.440144, 13.992907])
        self.m1.print_curr_hist()      
        
        self.m2 = Mallard()
        self.m2.print_curr_hist()
        self.m2.set_first_pos([56.440155, 13.992918])
        self.m2.print_curr_hist()
        
        pass
    
    def makeMoves(self):
        
        self.m1.move()
        self.m1.print_curr_hist()   
        self.m2.move()
        self.m2.print_curr_hist() 
        for i in range(12):
            self.m1.move()
            self.m2.move()
            self.m1.print_curr_hist() 
            
        pass
    
    
    pass



env = Environment()
env.makeMoves()

