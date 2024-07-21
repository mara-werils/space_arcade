import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Arcade")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
        pygame.draw.circle(self.image, GREEN, (25, 25), 25)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > HEIGHT:
            self.rect.y = -50
            self.rect.x = random.randint(0, WIDTH - self.rect.width)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.bottom = y
        self.speed = -10

    def update(self):
        self.rect.y += self.speed
        if self.rect.bottom < 0:
            self.kill()

def draw_text(surface, text, size, x, y):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(5):
    enemy = Enemy(random.randint(0, WIDTH - 50), random.randint(-100, -40))
    all_sprites.add(enemy)
    enemies.add(enemy)

score = 0
win_score = 10

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    all_sprites.update()

    hits = pygame.sprite.groupcollide(bullets, enemies, True, True)
    for hit in hits:
        score += 1
        enemy = Enemy(random.randint(0, WIDTH - 50), random.randint(-100, -40))
        all_sprites.add(enemy)
        enemies.add(enemy)

    if score >= win_score:
        running = False

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    draw_text(screen, f'Score: {score}', 18, WIDTH // 2, 10)
    draw_text(screen, f'Target: {win_score}', 18, WIDTH // 2, 30)
    pygame.display.flip()

screen.fill((0, 0, 0))
draw_text(screen, 'You Win!', 64, WIDTH // 2, HEIGHT // 2)
pygame.display.flip()
pygame.time.wait(3000)

pygame.quit()
