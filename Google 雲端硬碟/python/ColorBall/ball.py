import pygame,time,data,_thread

class ball():
    def __init__(self,color,x):
        self.color=data.colors[color]
        self.c=color
        self.x=x
        self.y=-20
        self.p=0
        if x==50:
            self.p=6
        else:
            self.p=-6
        self.live=True
        _thread.start_new_thread(self.start,())
    def start(self):
        while self.live:
            self.y+=1
            self.x+=self.p
            if self.x>760:
                data.touch=self
                time.sleep(0.02)
            elif self.x <0:
                self.p*=-1
            if self.y>820:
                try:
                    del data.balls[0]
                    self.live=False
                except:
                    print(data.balls)
                    print(self)
                    self.live=False
            time.sleep(0.025)