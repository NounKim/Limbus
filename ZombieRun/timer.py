from pico2d import *
import game_framework

class Time:
    def __init__(self):
        self.timer = 0
        Time.font = load_font('ENCR10B.TTF', 16)

    def update(self):
        self.timer += game_framework.frame_time
        delay(0.01)

    def draw(self):
        Time.font.draw(400, 400, 'Time: %3.2f' % self.timer, (255, 255, 0))

