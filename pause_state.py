import game_framework
import main_state
from pico2d import *

name = "PauseState"
image = None
cnt = 0

def enter():
    global image
    open_canvas()
    image = load_image('pause.png')

def exit():
    global image
    del(image)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN and 'p':
            game_framework.pop_state(main_state)

def update():
    global cnt
    cnt+=1
    if cnt>100:
        cnt=0

def draw():
    global  image
    clear_canvas()
    if cnt > 50:
      image.draw(400,300)
      delay(0.01)
    update_canvas()

def pause(): pass


def resume(): pass






