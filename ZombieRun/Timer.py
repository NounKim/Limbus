from pico2d import *
import time

class Time:
    def __init__(self):
        self.current_time = time.time()
        self.timer = 0

    def update(self):
        frame_time = time.time() - self.current_time
        self.timer += frame_time
        delay(0.01)