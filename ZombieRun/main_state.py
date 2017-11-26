import random
import json
import os
from pico2d import *

import game_framework
import title_state
import Timer
import pause_state


grass = None
pause_flag=False

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

def enter():
    global grass
    grass=Grass()


def exit():
    global grass
    del(grass)


def handle_events(frame_time):
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()()
        elif event.type==SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type==SDL_KEYDOWN and event.key==SDLK_p:
            pause_flag = True
            game_framework.push_state(pause_state)

def update(frame_time):
    global pause_flag
    pass

def pause():
    pass

def draw(frame_time):
    global pause_flag
    clear_canvas()
    grass.draw()


    update_canvas()

