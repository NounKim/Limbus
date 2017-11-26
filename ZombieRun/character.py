from pico2d import *
import game_framework

class Boy:
    image = None

    def __init__(self):
        self.x, self.y = 330, 90
        self.frame = 0
        self.jumpsw = 0
        self.highest_point = 0
        self.height = 1
        self.count = 0
        self.image = load_image('hero.png')

    def update(self, frame_time):
        self.frame = (self.frame + 1) % 8
        delay(0.01)
        if self.jumpsw == 1:
            self.y += self.height
            self.count += self.height
            if (self.count == 100):
                self.jumpsw = 0
                self.count = 0
        elif self.y > 90:
            self.y -= 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 92, self.x, self.y)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            pass



