import pygame,threading,time
from pygame.locals import *
from pygame.transform import *

class mario(threading.Thread):
    def __init__(self):     #角色初始化
        threading.Thread.__init__(self)
        self.x=100
        self.y=327
        self.image=pygame.image.load('run.PNG')
        self._image = self.image.copy()
        self.angle=0
        self.isgo=1     #循環的條件
    def rot_center(self,image, angle):
        """rotate an image while keeping its center and size"""
        self.angle -= angle
        orig_rect = image.get_rect()
        rot_image = pygame.transform.rotate(image, self.angle)
        rot_rect = orig_rect.copy()
        rot_rect.center = rot_image.get_rect().center
        rot_image = rot_image.subsurface(rot_rect).copy()
        return rot_image
    def jump(self,h):     #跳躍的程式
        if self.y == 327:
            jump = -1*h
            t = 0
            self.y = 326
            while self.y <= 327:
                time.sleep(0.05)
                self._image = self.rot_center(self.image, 15)
                self.y += jump + t * t/2
                t += 1
            self.y = 327
    def run(self):
        while self.isgo:
           allkey=pygame.key.get_pressed()
           if allkey[K_SPACE]:
               self.jump(30)
               time.sleep(0)
           self._image = self.rot_center(self.image,20)
           time.sleep(0.05)