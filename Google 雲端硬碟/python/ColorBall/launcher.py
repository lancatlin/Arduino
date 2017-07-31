import pygame,time,sys,data,ball,random,_thread,wall
from pygame.locals import *

def repaint():
    global screen
    screen.fill([20,50,80])
    for i in data.balls:
        pygame.draw.circle(screen,i.color,[i.x,i.y],20,0)
    for w in data.wa:
        for j in range(3):
            pygame.draw.rect(screen,data.colors[j],[w.x,w.y+j*200,30,200])
    pygame.display.flip()
def creatball():
    while True:
        data.balls.append(ball.ball(r(0,2),50))
        time.sleep(r(2,3))
        #data.balls.append(ball.ball(r(0,2),750))
        #time.sleep(2)
def iskey(key):
    allkey=pygame.key.get_pressed()
    return allkey[key]
def creatwall():
    a=780
    while True:
        h=1000
        d=-1000
        for i in data.wa:
            if iskey(K_UP):
                i.y -= 4
                #time.sleep(0.01)
            if iskey(K_DOWN):
                i.y += 4
                #time.sleep(0.01)
            try:
                if i.y > 800 or i.y < -600:
                    data.wa.remove(i)
            except:
                print('無法刪除')
            if i.y <h:
                h = i.y
            if i.y+600 >d:
                d = i.y+600
        if h>0:
            data.wa.append(wall.wall(a, h-600))
        if d<800:
            data.wa.append(wall.wall(a,d))
        time.sleep(0.01)
def touchball():
    if data.touch != None:
        d = data.touch
        for i in data.wa:
            if i.get(d.c, d.y + 20):
                d.p *= -1
                d = None
                break
        if d != None:
            try:
                data.balls.remove(d)
            except:
                x = 0
        data.touch = None
def r(n1,n2):
    return random.randint(n1,n2)
pygame.init()
pygame.display.set_caption('ColorBall')
screen=pygame.display.set_mode([800,800])
_thread.start_new_thread(creatball,())
_thread.start_new_thread(creatwall,())
while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()
            break
    touchball()
    repaint()