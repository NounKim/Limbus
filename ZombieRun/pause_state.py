import game_framework
import main_state

from pico2d import *
import time

class Pause:
    def __init__(self):
        self.image = load_image('pause.png')
        self.current_time = time.time()
        self.timer=0

    def draw(self):
        if (self.timer < 2.0):
            self.image.draw(400, 300)
        if (self.timer >= 2.0):
            self.timer = 0

def update(self):
    frame_time = time.time() - self.current_time
    self.timer+=frame_time
    delay(0.01)

def handle_events(self):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.change_state(main_state)

def enter():
    pass


