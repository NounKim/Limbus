# adjust_run_and_action.py : regulate run speed and action speed as well

import random
import time
from pico2d import *

max_time = 60.0

class Time:

    font = None
    image = None

    def __init__(self):
        global max_time
        self.now = max_time
        if Time.font == None:
            Time.font = load_font('ENCR10B.TTF', 16)

    def update(self, frame_time):
        global max_time
        for i in range(600):
            max_time -= 0.1
            time.sleep(0.1)

    def draw(self):
        Time.font.draw(400, 400, 'Time: %3.2f' % max_time(), (255, 255, 0))

