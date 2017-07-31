import pygame,_thread,time,data
import pygame.key
from pygame.locals import *

class wall():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self._y=y
    def get(self,q,a):
        c=[0,200,400,600]
        for i in range(len(c)):
            c[i]+=self.y
        if c[q]<a<c[q+1]:
            return True
        else:
            return False
    def key(self,key):
        allkey=pygame.key.get_pressed()
        return allkey[key]
