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
    return False
def txt(string,big,color,xy):
    f1=pygame.font.Font('freesansbold.ttf',big)
    fc1=f1.render(string,True,color[0],color[1])
    fr1=fc1.get_rect()
    fr1.center=xy
    return [fc1,fr1]
def welcome(score):
    a=txt('Roaling Jump',80,(black,white),(400,240))
    s=txt('last score:'+score,50,(black,white),(400,360))
    while True:
        screen.fill(white)
        screen.blit(a[0],a[1])
        screen.blit(s[0],s[1])
        if keydown(K_SPACE):
            print('I got it')
            break
        for i in pygame.event.get():
            if i.type == QUIT:
                print('quit')
                pygame.quit()
                sys.exit()
                break
        pygame.display.flip()
        time.sleep(0.05)
s='0'
while True:
    welcome(s)
    luncher.start()
    s=str(Data.score)