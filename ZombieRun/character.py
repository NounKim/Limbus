from pico2d import *

class Boy:
    image = None

    def __init__(self):
        self.x, self.y = 330, 90
        self.frame = 0
        self.highest_point = 0
        self.image = load_image('hero.png')

    def update(self):
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 92, self.x, self.y)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.y < 120:
                self.y += 1
            elif self.y == 120:
                self.highest_point =1
            elif self.highest_point == 1:
                if self.y > 90:
                    self.y -= 1


