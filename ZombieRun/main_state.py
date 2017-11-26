
from pico2d import *

import game_framework
import title_state
import timer
from character import Boy
import pause_state


character = None
grass = None
back_ground = None
pause_flag=False

def create_world():
    global character, grass, back_ground
    grass = Grass()
    back_ground = Back_ground
    character = Boy()

def destroy_world():
    global character
    global grass
    global back_ground

    del(grass)
    del(back_ground)
    del(character)

class Grass:
    def __init__(self):
        self.x, self.y = 800,300
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self, frame_time):
        self.x -= 3

class Back_ground:
    def __init__(self):
        self.x, self.y = 800,300
        self.image = load_image('back_ground.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self, frame_time):
        self.x -= 3

def enter():
    game_framework.reset_time()
    create_world()

def exit():
    destroy_world()
    close_canvas

def handle_events(frame_time):
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()()
        elif event.type==SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type==SDL_KEYDOWN and event.key==SDLK_p:
            game_framework.push_state(pause_state)
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            character.jumpsw = 1


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False
    return True

def update(frame_time):
    character.update(frame_time)
    grass.update(frame_time)
    back_ground.update(frame_time)

    #if collide(character,enemys):
    #    pass

def pause():
    pass

def draw(frame_time):
    clear_canvas()
    character.draw()
    character.draw_bb()
    grass.draw()
    back_ground.draw()

    update_canvas()

