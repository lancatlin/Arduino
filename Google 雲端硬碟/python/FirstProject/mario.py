import pygame,threading,time
from pygame.locals import *

class mario(threading.Thread):
    def __init__(self):     #角色初始化
        threading.Thread.__init__(self)
        self.x=100
        self.y=315
        self.image=pygame.image.load('mario.png')
        self.isgo=1     #循環的條件

    def jump(self):     #跳躍的程式
        if self.y == 315:
            jump = -30
            t = 0
            self.y = 314
            while self.y <= 315:
                time.sleep(0.05)
                self.y += jump + t * t/2
                t += 1
            self.y = 315
    def run(self):
        while self.isgo:
           allkey=pygame.key.get_pressed()
           if allkey[K_SPACE]:
               self.jump()
               time.sleep(0)
