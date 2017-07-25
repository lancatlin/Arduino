import pygame
from pygame.locals import *
import sys,time,random,_thread
import mario,mon,Data


def creatmonster():     #建構怪物的程式:boss
    global man
    global screen
    global score
    global ms
    global speed
    time.sleep(1.5)
    while Data.man.isgo:
        Data.ms.append(mon.monster())
        Data.ms[-1].start()
        time.sleep(random.uniform(0.8,1.4))
def repaint():      #刷新頁面
    global man
    global screen
    global score
    global ms
    global speed
    Data.screen.fill([255, 255, 255])
    Data.screen.blit(Data.man._image, (Data.man.x, Data.man.y))
    for m in Data.ms:    #劃出陣列中的每一隻怪物
        Data.screen.blit(m.image,(m.x,m.y))
    score_font = pygame.font.Font('freesansbold.ttf', 32)   #印出分數score
    score_face = score_font.render('Score:'+str(Data.score), True, (0, 0, 0), (255, 255, 255))
    score_rect = score_face.get_rect()
    score_rect.center = (100, 50)
    Data.screen.blit(score_face,score_rect)
    pygame.draw.line(Data.screen, [0, 0, 0], (0, 400), (800, 400), 5)
    pygame.display.flip()
def scoreUP():             #分數增加的程式:up
    global man
    global screen
    global score
    global ms
    global speed
    while Data.man.isgo:
        time.sleep(0.1)
        Data.score += 1
def start():
    global man
    global screen
    global score
    global ms
    global speed
    Data.again()
    Data.man = mario.mario()  # 建構馬力歐，儲存在Data
    pygame.init()
    pygame.display.set_caption("Run Run!!")
    Data.screen=pygame.display.set_mode((800,480))
    backgrond=[255,255,255]
    Data.screen.fill(backgrond)
    Data.man.start()                                     #啟動馬力歐的程式
    pygame.display.flip()
    boss=_thread.start_new_thread(creatmonster,())  #建構產生怪物的程式
    time.sleep(0.01)
    up = _thread.start_new_thread(scoreUP,())       #建構增加分數的程式
    while True:                                     #遊戲主循環
        for i in pygame.event.get():
            if i.type == QUIT:
                pygame.quit()
                sys.exit()
        if Data.man._isgo==False:
            print(Data.score)
            time.sleep(1)
            break
        Data.speed = 6+Data.score/500
        repaint()