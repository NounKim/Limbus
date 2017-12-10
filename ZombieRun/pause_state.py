import game_framework
import main_state

from pico2d import *
import time

class Pause:
    def __init__(self):
        self.image = load_image('pause.png')
        self.timer = 0


def draw(frame_time):
    if (pause.timer < 2.0):
        pause.image.draw(400, 300)
    if (pause.timer >= 2.0):
        pause.timer = 0
        update_canvas()


def update(frame_time):
    pause.timer += frame_time
    update_canvas()


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.change_state(main_state)

def enter():
    global pause
    pause=Pause()

def exit():
    global pause
    del pause

def pause():
    pass

def resume():
    pass


