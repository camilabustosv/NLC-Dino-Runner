from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HAMMER


class Hammer(Sprite):

    def __init__(self, x_pos, y_pos):
        Sprite.__init__(self)
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.hammer_speed = 4

    def update(self):
        self.rect.x += self.hammer_speed
        if self.rect.x > self.rect.width:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
