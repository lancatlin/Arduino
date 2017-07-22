import pygame
from pygame.locals import *
import sys,time,random,_thread
import mario,mon

man=mario.man  #建構馬力歐
def creatmonster():
    while man.isgo:
        mon.monster.ms.append(mon.monster())
        mon.monster.ms[-1].start()
        time.sleep(random.uniform(0.8,1.6))
def repaint():      #刷新頁面
    screen.fill([255, 255, 255])
    screen.blit(man._image, (man.x, man.y))
    for m in mon.monster.ms:    #劃出陣列中的每一隻怪物
        screen.blit(m.image,(m.x,m.y))
    score_font = pygame.font.Font('freesansbold.ttf', 32)
    score_face = score_font.render('Score:'+str(mario.score), True, (0, 0, 0), (255, 255, 255))
    score_rect = score_face.get_rect()
    score_rect.center = (100, 50)
    screen.blit(score_face,score_rect)
    pygame.draw.line(screen, [0, 0, 0], (0, 400), (800, 400), 5)
    pygame.display.flip()
def scoreUP():
    while man.isgo:
        time.sleep(0.1)
        mario.score += 1
        print(mario.score)
pygame.init()
pygame.display.set_caption("First project")
screen=pygame.display.set_mode((800,480))
backgrond=[255,255,255]
screen.fill(backgrond)
man.start()     #啟動馬力歐的程式
pygame.display.flip()
boss=_thread.start_new_thread(creatmonster,())#建構產生怪物的程式
time.sleep(0.01)
up = _thread.start_new_thread(scoreUP,())
while True:     #遊戲主循環
    for event in pygame.event.get():
        if event.type == QUIT or man.isgo==False:
            man.isgo=0
            print(mon.monster.ms)
            pygame.quit()
            sys.exit

    repaint()
print(mario.score)
pygame.quit()
sys.exit