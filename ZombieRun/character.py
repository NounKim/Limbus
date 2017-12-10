from pico2d import *
import game_framework

class Boy:
    image = None
    sound = None

    def __init__(self):
        self.x, self.y = 330, 90
        self.frame = 0
        self.jump_start = 0
        self.jump_end_flag = 0
        self.highest_point = 0
        self.height = 10
        self.count = 0
        self.sound_end = 0
        self.sound_count = 0
        self.sound_count2_start = 0
        self.sound_count2 = 0
        if Boy.image == None:
            Boy.image = load_image('hero.png')
        if Boy.sound == None:
            Boy.sound = load_wav('running-pant.wav')
            Boy.sound.set_volume(64)
            Boy.sound.repeat_play()


    def hurt(self, mob):
        self.sound_end = 1
        self.sound_count = 0
        self.sound_count2_start = 0
        self.sound_count2 = 0
        Boy.sound = load_wav('scream.wav')
        Boy.sound.set_volume(32)
        self.sound.play()

    def update(self, frame_time):
        self.frame = (self.frame + 1) % 8
        delay(0.05)

        if self.sound_end == 1:
            self.sound_count += 1

        if self.sound_count == 50:
            self.sound_end = 0
            self.sound_count = 0
            self.sound_count2_start = 1
            Boy.sound = load_wav('crying.wav')
            Boy.sound.set_volume(64)
            Boy.sound.repeat_play()

        if self.sound_count2_start == 1:
            self.sound_count2 += 1

        if self.sound_count2 == 250:
            self.sound_count2_start = 0
            self.sound_count2 = 0
            Boy.sound = load_wav('running-pant.wav')
            Boy.sound.set_volume(64)
            Boy.sound.repeat_play()

        if self.jump_start == 1:
            self.y += 15
            if self.y > 270:
                self.jump_start = 0

        if self.jump_start != 1:
            self.y -= 15
            self.y = max(self.y,90)
            if self.y == 90:
                self.jump_end_flag = 0

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 92, self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y - 30, self.x + 20, self.y + 30

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.jump_end_flag != 1:
                self.jump_start = 1

        if (event.type, event.key) == (SDL_KEYUP, SDLK_SPACE):
            self.jump_start = 0
            self.jump_end_flag = 1





