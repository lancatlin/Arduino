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
def rot_center(image, angle):          #旋轉圖片
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image
def welcome(score):
    a=txt('Roaling Jump',90,(black,white),(400,100))
    s=txt('last score:'+score,50,(black,white),(550,430))
    image = pygame.image.load('run.PNG')  # 圖片原始檔
    image=pygame.transform.scale(image,(180,180))
    _image = image.copy()  # 拷貝的圖片(用於旋轉)
    r=open('score.txt','r')
    x = 1
    c = []
    for i in r.read().split():
        b = txt(str(x) + ':' + i, 45, (black, white), (200, 130 + x * 60))
        c.append(b)
        x += 1
    angle=0
    while True:
        screen.fill(white)
        screen.blit(a[0],a[1])
        screen.blit(s[0],s[1])
        for j in c:
            screen.blit(j[0],j[1])
        _image=rot_center(image,angle)
        angle-=2
        screen.blit(_image,(450,180))
        if keydown(K_SPACE):
            print('start')
            break
        pygame.display.flip()
        time.sleep(0.01)
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