import pygame
from random import uniform as func

pygame.init()
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()

bound = 5
c2s = 30
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

radius = 10
x, y = WIDTH // 2, HEIGHT // 2
vx, vy = func(-5, 5), func(-5, -2)

border_l = bound + radius
border_r = WIDTH - bound - radius
border_u = bound + radius
border_d = HEIGHT - bound - radius

height = 10
width = 80
xp = (WIDTH - width) // 2
yp = HEIGHT - height
vp = 10

score = 0

font = pygame.font.SysFont(None, 40)


def drawWindow():
    win.fill(black)
    pygame.draw.rect(win, white, (0, 0, WIDTH, bound))
    pygame.draw.rect(win, white, (0, 0, bound, HEIGHT))
    pygame.draw.rect(win, white, (WIDTH - bound, 0, bound, HEIGHT))
    pygame.draw.rect(win, white, (xp, yp, width, height))
    pygame.draw.circle(win, green, (int(x), int(y)), radius)
    pygame.display.update()


def drawScore():
    win.fill(black)
    text = font.render(f"Your score: {score}", True, white)
    win.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
    pygame.display.update()
    pygame.time.wait(3000)


run = True
while run:
    clock.tick(c2s)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and xp > bound:
        xp -= vp
    if keys[pygame.K_RIGHT] and xp < WIDTH - bound - width:
        xp += vp

    if x + vx < border_l or x + vx > border_r:
        vx = -vx
    if y + vy < border_u:
        vy = -vy

    if y + vy > yp:
        if xp <= x + vx <= xp + width:
            vy = -vy
            num = 1.5
            vx *= num
            vy *= num
            score += 1
        else:
            run = False

    x += vx
    y += vy

    drawWindow()

drawScore()
pygame.quit()
