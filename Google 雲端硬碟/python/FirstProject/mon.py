import pygame, threading, time, random


class monster(threading.Thread):
    ms = []

    def __init__(self):
        threading.Thread.__init__(self)
        self.image = pygame.image.load('monster.png')
        r = random.randint(50, 100)
        self.image = pygame.transform.scale(self.image, (r, r))
        self.x = 870
        self.y = 400 - r
        self.speed = 6

    """def isHit(self):
        if self.man.x < self.x < self.man.x + self.man.image.get_width() \
                and self.man.y < self.y < self.man.x + self.man.image.get_height():
            return True
        else:
            return False"""

    def run(self):
        live = 1
        while live:
            time.sleep(0.01)
            self.x -= self.speed

            if self.x < -70:
                live = 0
                monster.ms.remove(self)
