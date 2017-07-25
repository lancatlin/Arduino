import pygame,time,luncher,sys,_thread,Data
from pygame.locals import *
white=[255,255,255]
black=[0,0,0]
yellow=[255,255,0]

pygame.init()
screen = pygame.display.set_mode((800,480))
pygame.display.set_caption('Roaling Jump')

def keydown(_key):
    for i in pygame.event.get():
        if i.type == KEYDOWN:
            return True
        if i.type == QUIT:
            pygame.quit()
            sys.exit()
    return False
def txt(string,big,color,xy):
    f1=pygame.font.Font('freesansbold.ttf',big)
    fc1=f1.render(string,True,color[0],color[1])
    fr1=fc1.get_rect()
    fr1.center=xy
    return [fc1,fr1]
def welcome(score):
    a=txt('Roaling Jump',80,(black,white),(400,100))
    s=txt('last score:'+score,50,(black,white),(600,200))
    r=open('score.txt','r')
    x = 1
    c = []
    for i in r.read().split():
        b = txt(str(x) + ':' + i, 50, (black, white), (200, 130 + x * 60))
        c.append(b)
        x += 1
    while True:
        screen.fill(white)
        screen.blit(a[0],a[1])
        screen.blit(s[0],s[1])
        for j in c:
            screen.blit(j[0],j[1])
        if keydown(K_SPACE):
            print('start')
            break
        pygame.display.flip()
        time.sleep(0.05)
def ap(s):
    rs=open('score.txt','r')
    a=[]
    for i in rs.read().split():
        a.append(int(i))
    a.append(s)
    a.sort()
    a.reverse()
    del a[-1]
    result=''
    for i in range(len(a)):
        if i != len(a):
            result+=str(a[i])+' '
        else:
            result+=str(a[i])
    print(result)
    w=open('score.txt','w')
    w.write(result)
    rs.close()
    w.close()
s='0'
while True:
    welcome(s)
    luncher.start()
    s=str(Data.score)
    ap(Data.score)