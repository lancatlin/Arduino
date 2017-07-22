import pygame
from pygame.locals import *
import sys,threading,time,random
import mario,mon

man=mario.man  #建構馬力歐
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
    for m in mon.monster.ms:    #劃出陣列中的每一隻怪物
        screen.blit(m.image,(m.x,m.y))
    pygame.draw.line(screen, [0, 0, 0], (0, 400), (800, 400), 5)
    pygame.display.flip()
pygame.init()
pygame.display.set_caption("First project")
screen=pygame.display.set_mode((800,480))
backgrond=[255,255,255]
screen.fill(backgrond)
man.start()     #啟動馬力歐的程式
pygame.display.flip()
boss=creatmonster() #建構產生怪物的程式
boss.start()
time.sleep(0.01)
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