import game_framework
import main_state
import title_state
import random
from pico2d import *

name = "ResultState"
image = None
bgm = None
font = None
score = 0
art = 0


def get_Time(time):
    global score
    score = time

def enter():
    global image, bgm, font, art
    art = random.randint(0,9999)
    image=load_image('skeleton.png')
    if bgm == None:
        bgm = load_music('gameover.wav')
        bgm.set_volume(64)
        bgm.play(1)
    if font == None:
        font = load_font('ENCR10B.TTF', 36)

def exit():
    global image
    del(image)

def handle_events(frame_time):
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()()
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_SPACE):
                game_framework.change_state(title_state)



def draw(frame_time):
    global score, art
    clear_canvas()
    image.draw(400,150)
    font.draw(250, 550, 'Art: %3.2f' % art, (255, 255, 0))
    font.draw(270, 500, 'Survive: %3.2f' % score, (255, 255, 0))
    font.draw(300, 450, 'Result: %3.2f' % (score + art), (255, 255, 0))
    font.draw(200, 400, 'Press Space to Continue...', (255, 0, 0))

    update_canvas()


def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass






