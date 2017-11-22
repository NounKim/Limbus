from pico2d import *

class Pause:
    def __init__(self):
        self.image = load_image('pause.png')

    def update(self):
        pass

    def draw(self):
        global timer
        timer += 1
        if (timer < 100):
            self.image.draw(400, 300)
        if (timer > 500):
            timer = 0
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            pause_flag = 1 - pause_flag