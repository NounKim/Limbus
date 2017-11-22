import random
import json
import os
from pico2d import *

import game_framework
import title_state
import frame_time
import pause_state

boy = None
enemy = None
grass = None
back_ground = None
font = None
time = None
pause_flag=False
timer=0

class Back_ground:
    def __init__(self):
        self.x, self.y = 800,300
        self.image = load_image('back_ground.png')

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x -= 3

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = 330, 90
        self.frame = 0
        self.image = load_image('hero.png')
        self.dir = 1

    def update(self):
        global pause_flag
        if(pause_flag==False):
            self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 92, self.x, self.y)

class Enemy:
    def __init__(self):
        self.x, self.y = random.randint(30,60), 90
        self.frame = 0
        self.image = load_image('enemy.png')
        self.dir = 1

    def update(self):
        global pause_flag
        if(pause_flag==False):
            self.frame = (self.frame + 1) % 6

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 115, self.x, self.y)


class Pause:
    def __init__(self):
        self.image = load_image('pause.png')

    def update(self):
        pass
    def draw(self):
        global  timer
        timer+=1
        if(timer<100):
            self.image.draw(400,300)
        if(timer>500):
            timer=0


def enter():
    global boy,grass,pause,time,enemy,back_ground
    grass=Grass()
    enemy=Enemy()
    boy=Boy()
    pause=Pause()
    back_ground=Back_ground()
    #time=Time()

def exit():
    global boy,grass,pause,time
    del(boy)
    del(grass)
    del(pause)
    del(enemy)
    del(back_ground)
    #del(time)

def handle_events():
    global pause_flag
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()()
        elif event.type==SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type==SDL_KEYDOWN and event.key==SDLK_p:
            pause_flag=1-pause_flag
     #   elif time.now == 0.0:
     #       game_framework.change_state(title_state)

def update():
    boy.update()
    enemy.update()
    back_ground.update()
    delay(0.1)
    #time.update()

def draw():
    global pause_flag
    clear_canvas()
    if(pause_flag):
        pause.draw()
    back_ground.draw()
    grass.draw()
    boy.draw()
    enemy.draw()
    #time.draw()

    update_canvas()





