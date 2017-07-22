import pygame, threading, time, random
import luncher

class monster(threading.Thread):
    ms = []     #儲存怪物的陣列

    def __init__(self):     #初始化
        threading.Thread.__init__(self)
        self.image = pygame.image.load('monster.png')
        r = random.randint(50, 100)     #隨機設定怪物大小
        self.image = pygame.transform.scale(self.image, (r, r))
        self.x = 870
        self.y = 400 - r
        self.speed = 6
    def dist(self,x,y):     #取得與馬力歐之間的距離
        result=((self.x-x)**2+(self.y-y)**2)**0.5
        print(result)
        return result
    def isHit(self):        #如果距離小於五就撞到了(回傳True)
        val=self.dist(luncher.man.x,luncher.man.y)
        if(val<15):
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
                monster.ms.remove(self)
