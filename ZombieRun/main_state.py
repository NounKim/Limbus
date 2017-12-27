
from pico2d import *

import game_framework
import title_state
import result_state
import timer
from character import Boy, Death
from enemys import Enemy
from land import Back_ground, Land, City
import pause_state
import json


character = None
enemy = None
back_ground = None
land = None
city = None
pause_flag=False
death = None
time = None
font = None

def create_world():
    global character, back_ground, land, enemy, city, death, time

    character = Boy()
    death = Death(character)
    enemy = [Enemy() for i in range(5)]
    back_ground = Back_ground()
    land = Land()
    city = City()
    time = get_time()

def destroy_world():
    global character, back_ground, land, enemy, city, death

    del(character)
    del(enemy)
    del(back_ground)
    del(land)
    del(city)
    del(death)

def enter():
    global font
    #game_framework.reset_time()
    create_world()
    if font == None:
        font = load_font('ENCR10B.TTF', 24)

def exit():
    destroy_world()
    close_canvas

def handle_events(frame_time):
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        elif event.type==SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type==SDL_KEYDOWN and event.key==SDLK_p:
            game_framework.push_state(pause_state)
        else:
            character.handle_event(event)
            for mob in enemy:
                mob.handle_event(event)

def update(frame_time):
    global time
    time -= -get_time()
    character.update(frame_time)
    death.update(character)

    for mob in enemy:
        if collide(character, mob):
            character.hurt(mob)

    for mob in enemy:
        mob.update(frame_time)

    for mob in enemy:
        if collide(character, mob):
            mob.eat(character)

    back_ground.update(frame_time)
    land.update(frame_time)
    city.update(frame_time)

    if collide(character, death):
        result_state.get_Time(time)
        game_framework.change_state(result_state)
    #if collide(character,enemys):
    #    pass

def pause():
    pass

def resume():
    pass

def draw(frame_time):
    clear_canvas()
    back_ground.draw()
    font.draw(330, 500, 'Time: %3.2f' % (time/10), (255, 50, 50))
    city.draw()
    land.draw()
    death.draw()

    character.draw()
    for mob in enemy:
        mob.draw()

    update_canvas()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

