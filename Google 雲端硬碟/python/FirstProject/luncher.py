import pygame
from pygame.locals import *
import sys,threading,time,random
import mario,mon

man=mario.mario()  #建構馬力歐
class creatmonster(threading.Thread):       #建構怪物
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        self.islive=1
        while self.islive:
            mon.monster.ms.append(mon.monster())
            mon.monster.ms[-1].start()
            time.sleep(random.uniform(0.8,1.6))
def repaint():      #刷新頁面
    screen.fill([255, 255, 255])
    screen.blit(man._image, (man.x, man.y))
    for m in mon.monster.ms:
        screen.blit(m.image,(m.x,m.y))
    pygame.draw.line(screen, [0, 0, 0], (0, 400), (800, 400), 5)
    pygame.display.flip()
pygame.init()
pygame.display.set_caption("First project")
screen=pygame.display.set_mode((800,480))
backgrond=[255,255,255]
screen.fill(backgrond)
man.start()
pygame.display.flip()
boss=creatmonster()
boss.start()
while True:     #遊戲主循環
    for event in pygame.event.get():
        if event.type == QUIT:
            man.isgo=0
            boss.islive=0
            print(mon.monster.ms)
            pygame.quit()
            sys.exit

    repaint()
pygame.quit()
sys.exit