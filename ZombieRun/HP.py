from pico2d import *
import game_framework
import random

class Enemy:
    image = None
    eat_sound = None

    def __init__(self):
        self.x, self.y = random.randint(20, 70), 90
        self.frame = random.randint(0,3)
        self.jump_start = 0
        self.jump_end_flag = 0
        self.highest_point = 0
        self.height = 10
        self.rush_count = 0
        self.rush_event = 0
        self.x_save = 0
        self.rush_end_flag = 0
        if Enemy.image == None:
            Enemy.image = load_image('enemy.png')
        if Enemy.eat_sound == None:
            Enemy.eat_sound = load_wav('bite.wav')
            Enemy.eat_sound.set_volume(32)

    def eat(self, character):
        self.eat_sound.play()

    def update(self, frame_time):
        self.frame = (self.frame + 1) % 6
        self.rush_count +=1

        if self.rush_count == 30:
            self.x_save = self.x
            self.rush_event = random.randint(0,1)
            if self.rush_event == 0:
                self.rush_count = 0

        if self.rush_event == 1:
            self.rush_end_flag = 1
            self.x += 13
            if self.x >= 900:
                self.x = -50
                self.rush_event = 0

        if self.x < self.x_save:
            self.x += 1
            self.x = min(self.x, self.x_save)
            if self.x == self.x_save:
                self.rush_end_flag = 0
                self.rush_count = 0

        if self.jump_start == 1:
            self.y += 10
            if self.y > 250:
                self.jump_start = 0

        if self.jump_start != 1:
            self.y -= 10
            self.y = max(self.y,90)
            if self.y == 90:
                self.jump_end_flag = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 115, self.x, self.y)

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.jump_end_flag != 1:
                if self.rush_end_flag != 1:
                    self.jump_start = random.randint(0,1)

        if (event.type, event.key) == (SDL_KEYUP, SDLK_SPACE):
            self.jump_start = 0
            self.jump_end_flag = 1





