import random

from pico2d import *

class Water:
    image = None;
    def __init__(self):
        self.x, self.y = random.randint(200, 790), 60
        if Water.image == None:
            Water.image = load_image('water.png')

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def update(self, frame_time):

        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    # fill here


class Tuna_can:
    image = None
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 500
        self.move_speed = random.randint(50,120)
        self.sw=0
        if Tuna_can.image == None:
            Tuna_can.image = load_image('tuna_can.png')

    def update(self, frame_time):
        self.y -= frame_time * self.fall_speed

    def stop(self):
        self.move_speed = 0

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

            # fill here