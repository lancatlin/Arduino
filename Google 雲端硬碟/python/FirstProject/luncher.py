import pygame
from pygame.locals import *
import sys,time,random,_thread
import mario,mon,Data

Data.man=mario.mario()  #建構馬力歐，儲存在Data
man=Data.man
def creatmonster():     #建構怪物的程式:boss
    while man.isgo:
        Data.ms.append(mon.monster())
        Data.ms[-1].start()
        time.sleep(random.uniform(0.8,1.4))
def repaint():      #刷新頁面
    screen.fill([255, 255, 255])
    screen.blit(man._image, (man.x, man.y))
    for m in Data.ms:    #劃出陣列中的每一隻怪物
        screen.blit(m.image,(m.x,m.y))
    score_font = pygame.font.Font('freesansbold.ttf', 32)   #印出分數score
    score_face = score_font.render('Score:'+str(Data.score), True, (0, 0, 0), (255, 255, 255))
    score_rect = score_face.get_rect()
    score_rect.center = (100, 50)
    screen.blit(score_face,score_rect)
    pygame.draw.line(screen, [0, 0, 0], (0, 400), (800, 400), 5)
    pygame.display.flip()
def scoreUP():             #分數增加的程式:up
    while man.isgo:
        time.sleep(0.1)
        Data.score += 1
pygame.init()
pygame.display.set_caption("Run Run!!")
Data.screen=pygame.display.set_mode((800,480))
screen = Data.screen
backgrond=[255,255,255]
screen.fill(backgrond)
man.start()                                     #啟動馬力歐的程式
pygame.display.flip()
boss=_thread.start_new_thread(creatmonster,())  #建構產生怪物的程式
time.sleep(0.01)
up = _thread.start_new_thread(scoreUP,())       #建構增加分數的程式
while True:                                     #遊戲主循環
    for event in pygame.event.get():
        if event.type == QUIT or man.isgo==False:
            man.isgo=0
            print(Data.score)
            pygame.quit()
            sys.exit
    Data.speed = 6+Data.score/500
    repaint()
pygame.quit()
sys.exit