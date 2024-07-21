import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 760)
        self.rect.y = random.randint(0, 100)
        self.speed = random.randint(1, 3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 600:
            self.rect.y = random.randint(-100, -40)
            self.rect.x = random.randint(0, 760)
