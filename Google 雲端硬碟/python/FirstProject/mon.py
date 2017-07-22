import pygame, threading, time, random,mario

class monster(threading.Thread):
    ms = []     #儲存怪物的陣列

    def __init__(self):     #初始化
        threading.Thread.__init__(self)
        self.image = pygame.image.load('monster.png')
        self.r = random.randint(50, 100)     #隨機設定怪物大小
        self.image = pygame.transform.scale(self.image, (self.r, self.r))
        self.x = 870
        self.y = 400 - self.r
        self.speed = 6
    def getXY(self):
        return [self.x+(self.r/2),self.y+(self.r/2)]
    def dist(self,x,y):   #取得與馬力歐之間的距離
        xy=self.getXY()
        result=((xy[0]-x)**2+(xy[1]-y)**2)**0.5
        return result
    def isHit(self):   #如果距離小於五就撞到了(回傳True)
        xy=mario.man.getXY()
        val=self.dist(xy[0],xy[1])
        if(val<35+(self.r/2)):
            return True
        else:
            return False
    def run(self):          #怪物主程式
        live = 1
        while live:
            time.sleep(0.01)
            self.x -= self.speed

            if self.x < -70:    #如果超出畫面
                live = 0
                monster.ms.remove(self)
            if self.isHit():    #如果碰到主角
                live = 0
                mario.man.isgo=False
                monster.ms.remove(self)
