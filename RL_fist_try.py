#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 14:03:30 2018

@author: cens
"""

import time
import random

class room(object):
     def __init__(self, location):        
        self.location = location
        (x,y) = self.location
        self.score = 0
        self.finish = ((x,y) == (2,2)) or ((x,y) == (1,0))
        self.start = ((x,y) == (0,0))
        self.reward = ((x,y) == (2,2)) -((x,y) == (1,0))
        
class Agent(object):
    
    
    def __init__(self,alpha):
        self.CurrentRoom = (0,0)
        self.PreviousRoom = (0,0)
        self.NextRoom = (0,0)
        
        self.table = {(x,y): None for x in range(4) for y in range(4)}
        for i in self.table.keys():
            self.table[i] = room(i)
        self.alpha = alpha  #alpha is learning rate for the agent, that means 
        # how fast an agent catch up with latest changes in the environment
    
    def ramble(self):

        while(True):   
  
            if (self.table[self.CurrentRoom].finish == False):
                self.action(self.CurrentRoom)
                self.update()
            else:
                if self.CurrentRoom == (2,2):
                    reward = +1
                elif self.CurrentRoom == (1,0):
                    reward = -1
                else:
                    reward = 0
                self.NextRoom = (0,0)
                self.table[self.CurrentRoom].score =+ (reward)
                
                break
            
            
    def update(self):        
        if self.CurrentRoom == (2,2):
            reward = +1
        elif self.CurrentRoom == (1,0):
            reward = -1
        else:
            reward = 0
        print(self.CurrentRoom)
        self.table[self.PreviousRoom].score = self.table[self.PreviousRoom].score*(1-self.alpha)\
            (reward + self.table[self.CurrentRoom].score )* self.alpha
        
        
        
    def action(self, CurrentRoom):
        
        
        maximum = -1
        maxList = []
        for newroom in CurrentNeighbors((self.CurrentRoom)):
            if self.table[newroom].score > maximum: 
                maxList.append(newroom)
        self.NextRoom = random.choice(maxList)
              
        self.PreviousRoom = self.CurrentRoom
        self.CurrentRoom = self.NextRoom
        #print(self.NextRoom)
        
        
        
        
def CurrentNeighbors(location):
    (x,y) = location
    neighbors = []
    neighbors.extend( [(x+v,y+h) for v in [-1,1] for h in [0]] ) 
    neighbors.extend( [(x+v,y+h) for v in [0] for h in [-1,1]] ) 
    validNeighbors = []
    for (x,y) in neighbors:
        if x not in [-1,4] and y not in [-1,4]:
            validNeighbors.append((x,y))

    return validNeighbors  
 
def game(alpha):
    agent = Agent(alpha)
    for round in range(10):
        agent.ramble()
        scoreMatrix = [[agent.table[(x,y)].score for x in range(4)] for y in range(4)]
        print(scoreMatrix)
        
    scoreMatrix = [[agent.table[(x,y)].score for x in range(4)] for y in range(4)]
    return scoreMatrix

if __name__ == '__main__':
        
    start_time = time.time()
    matrix = game(0.9)
    #print(matrix)
    for i in range(4):
        print(' '.join(["{:.4f}".format(matrix[i][j]) for j in range(4)]))


    print("--- %.5f seconds ---" % (time.time() - start_time))
