import random

from pico2d import *

class Back_ground:
    image = None;
    def __init__(self):
        self.bgm = load_music('ruin-wind.wav')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()
        self.x, self.y = 800,300
        if Back_ground.image == None:
            Back_ground.image = load_image('back_ground.png')

    def update(self, frame_time):
        self.x -= frame_time*10
        if self.x <= 0:
            self.x = 800

    def draw(self):
        self.image.draw(self.x, self.y)

    # fill here


class Land:
    image = None
    def __init__(self):
        self.x, self.y = 800,30
        if Land.image == None:
            Land.image = load_image('grass.png')

    def update(self, frame_time):
        self.x -= frame_time*100
        if self.x <= 0:
            print('x')
            self.x = 800

    def draw(self):
        self.image.draw(self.x, self.y)
