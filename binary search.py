# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 23:32:41 2021

@author: Dell
"""
import random

class Node:
    def __init__(self,data=None):
        self.left=None
        self.right=None
        self.data=data
        
    def add(self,data):
        
        if self.data:
            if data<self.data:
                if self.left is None:
                    self.left=Node(data)
                else :
                     self.left.add(data)
            elif data>self.data:
                if self.right is None:
                    self.right=Node(data)
                else :
                    self.right.add(data)
        else :
                self.data=data
            
            
          


def printer():
   
    root=Node(87)
 
    for i in range(10):
     n = random.randint(2,80)
     root.add(n)
     print(n)
    print('###################################################')   
 
    looker=root.data
    while looker is not None:
     print(looker)
      
     root=root.left 
     looker=root.data
printer()