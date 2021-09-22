from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HEART


class Live(Sprite):
    def __init__(self, POS_X = 50):
        self.image = HEART
        self.rect = self.image.get_rect()
        self.rect_x = POS_X
        self.rect_y = 30

    def draw(self, screen):
        screen.blit(self.image,(self.rect_x, self.rect_y))
