import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        radius=25
        self.image = pygame.Surface((radius*2,radius*2),pygame.SRCALPHA)
        pygame.draw.circle(self.image,(0,255,0),(radius,radius),radius)
        self.rect = self.image.get_rect()
        self.rect.centerx = 400
        self.rect.bottom = 580
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

    def draw(self,screen):
        screen.blit(self.image,self.rect.topleft)