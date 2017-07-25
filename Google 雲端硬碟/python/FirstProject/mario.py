import pygame,threading,time,Data,_thread
from pygame.locals import *
class mario(threading.Thread):
    def __init__(self):     #角色初始化
        threading.Thread.__init__(self)
        self.x=100
        self.y=327
        self.image=pygame.image.load('run.PNG') #圖片原始檔
        self._image = self.image.copy()         #拷貝的圖片(用於旋轉)
        self.angle=0                            #圖片轉動方向
        self.isgo=1     #循環的條件
    def getXY(self):                            #取得角色中心點
        return [self.x+35,self.y+35]
    def rot_center(self,image, angle):          #旋轉圖片
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
    def keydown(self,_key):
        allkey = pygame.key.get_pressed()
        if allkey[_key]:
            return True
        else:
            return False
    def run(self):      #馬力歐主程式
        while self.isgo:
           if self.keydown(K_SPACE):
               self.jump(30)
           self._image = self.rot_center(self.image,20/6*Data.speed)
           time.sleep(0.05)