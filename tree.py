import pygame, sys
from pygame.locals import *
import random
import math
import time

  
pygame.init()
  
FPS = 30#frames per second
fpsClock = pygame.time.Clock()#creates a clock object to control framerates
screen_widht = 1000
screen_height = 600
BLUE = (180, 255, 255)
BROWN = (100, 50, 0)
DARK_BROWN = (75, 25, 0)
GREEN = (0, 150, 70)
DARK_GREEN = (0, 100, 0)
PURPLE = (255, 150, 255)
DARK_PURPLE = (255, 0, 255)

trunk_piece = 10

screen = pygame.display.set_mode((screen_widht, screen_height), 0, 32)
screen.fill(BLUE)

fuzzyness = 0.3

counter = 0


def rotation(move_x, move_y, angle):
    angle_in_radians = math.radians(angle)
    new_move_x = move_x * math.cos(angle_in_radians) - move_y*math.sin(angle_in_radians)
    new_move_y = move_x * math.sin(angle_in_radians) + move_y*math.cos(angle_in_radians)        
    return new_move_x, new_move_y
    

class Branch(object):
    def __init__(self, x, y, move_x, move_y, length):
        self.x = x
        self.y = y
        self.counter = 0
        self.length = length
        self.move_x = move_x
        self.move_y = move_y
        if self.move_x > 1 or self.move_x < -1 and self.move_y > 1 or self.move_y < -1: 
            self.move_x += random.uniform(-fuzzyness, fuzzyness) 
            self.move_y += random.uniform(-fuzzyness, fuzzyness)
        if -1 < self.move_y < 1 and self.move_x > 1 or self.move_x < -1:
            self.move_y += random.uniform(-fuzzyness, fuzzyness)
        if -1 < self.move_x < 1 and self.move_y > 1 or self.move_y:
            self.move_x += random.uniform(-fuzzyness, fuzzyness)  
        
             
    def grow(self):  
#         if self.move_x > 1 or self.move_x < -1 and self.move_y > 1 or self.move_y < -1: 
#             self.move_x += random.uniform(-fuzzyness, fuzzyness) 
#             self.move_y += random.uniform(-fuzzyness, fuzzyness)
#         if -1 < self.move_y < 1 and self.move_x > 1 or self.move_x < -1:
#             self.move_y += random.uniform(-fuzzyness, fuzzyness)
#         if -1 < self.move_x < 1 and self.move_y > 1 or self.move_y:
#             self.move_x += random.uniform(-fuzzyness, fuzzyness)        
        if len(branches) <= 200:
            self.y += self.move_y
            self.x += self.move_x
            self.counter += 1
            pygame.draw.rect(screen, DARK_BROWN, (self.x, self.y, trunk_piece, trunk_piece))
        if len(branches) <= 200:       
            self.y += self.move_y
            self.x += self.move_x
            self.counter += 1
            pygame.draw.rect(screen, BROWN, (self.x, self.y, trunk_piece, trunk_piece))
        if 2500 > len(branches) > 200:
            self.y += self.move_y
            self.x += self.move_x
            self.counter += 1
            pygame.draw.rect(screen, DARK_GREEN, (self.x, self.y, trunk_piece, trunk_piece))
        if 2500 > len(branches) > 200:
            self.y += self.move_y
            self.x += self.move_x
            self.counter += 1
            pygame.draw.rect(screen, GREEN, (self.x, self.y, trunk_piece, trunk_piece))
    
    def split(self):
        self.counter = 0
        self.move_x, self.move_y = rotation(self.move_x, self.move_y, 45)
        child_move_x, child_move_y = rotation(self.move_x, self.move_y, -90)
        self.length -= self.length/3    
        return Branch(self.x, self.y, child_move_x, child_move_y, self.length)
    

branches = []
branches.append(Branch(500, 550, 0, -2, 75))

     
while True:      
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    
    if len(branches) <= 2500:
        for branch in branches:
            branch.grow()
            if branch.counter > branch.length:
                branches.append(branch.split())
    if len(braches) == 2500:
      time.sleep(2)
      screen = pygame.display.set_mode((screen_widht, screen_height), 0, 32)
      screen.fill(BLUE)
      branches = []
      branches.append(Branch(500, 550, 0, -2, 75))
      
       
    pygame.display.update()
    fpsClock.tick(FPS)
