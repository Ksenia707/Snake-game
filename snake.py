import os

import pygame as p
import random

p.init()

GAME_HEIGHT = 600
GAME_WIDTH = 600

YELLOW = (103, 230, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PINK = (241, 156, 187)

screen = p.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
p.display.set_caption('Snake')
clock = p.time.Clock()

font = p.font.SysFont('impact', 45)

def message(msg, color):
    mess = font.render(msg, True, color)
    new_x = GAME_WIDTH // 2 - mess.get_width() // 2
    new_y = GAME_HEIGHT // 2 - mess.get_height() // 2
    screen.blit(mess, (new_x, new_y))

def food():
    x = random.randint(0, GAME_WIDTH - 20)
    y = random.randint(0, GAME_HEIGHT - 20)

    while x % 20 != 0:
        x += 1
    while y % 20 != 0:
        y += 1

    return x, y

def game():
    x, y = 300, 300
    x_step, y_step = 0, 0
    x_food, y_food = food()
    plrs = []
    plr_len = 1
    score = 0

    game_over = False
    game_finish = False
    while not game_over:
        while game_finish:
            screen.fill(PINK)
            message('Press SPACE - new game', (255, 255, 255))

            for event in p.event.get():
                if event.type == p.QUIT:
                    game_over = True
                    game_finish  = False
                elif event.type == p. KEYDOWN and event.key == p.K_SPACE:
                    x, y = 300, 300
                    plrs = []
                    plr_len = 1
                    x_food, y_food = food()
                    score = 0
                    game_finish = False

            p.display.update()

        for event in p.event.get():
            if event.type == p.QUIT:
                game_over = True
            elif event.type == p.KEYDOWN and event.key == p.K_ESCAPE:
                game_over = True
            elif event.type == p.KEYDOWN:
                if event.key == p.K_w:
                    y_step = -20
                    x_step = 0
                elif event.key == p.K_a:
                    y_step = 0
                    x_step = -20
                elif event.key == p.K_d:
                    y_step = 0
                    x_step = 20
                elif event.key == p.K_s:
                    y_step = 20
                    x_step = 0

        x += x_step
        y += y_step

        if y > GAME_HEIGHT:
            game_finish = True
        elif y < 0:
            game_finish = True
        elif x > GAME_HEIGHT:
            game_finish = True
        elif x < 0:
            game_finish = True

        plr_head = []
        plr_head.append(x)
        plr_head.append(y)

        plrs.append(plr_head)
        if len(plrs) > plr_len:
            del plrs[0]

        if x == x_food and y == y_food:
            x_food, y_food = food()
            plr_len += 1
            score += 1

        for n  in plrs[:-1]:
            if n == plr_head:
                game_finish = True

        screen.fill(YELLOW)

        score_text = font.render('SCORE: ' + str(score), True, (255, 255, 255))
        screen.blit(score_text, (20, 20))
        # x1, x2 = 0, 0
        # for i in range(GAME_WIDTH // 2):
        #     p.draw.rect(screen, BLACK, p.Rect(x1, x2, 20, GAME_HEIGHT), 1)
        #     x1 += 20
        #
        # x1 = 0
        # for i in range(GAME_HEIGHT // 2):
        #     p.draw.rect(screen, BLACK, p.Rect(x1, x2, GAME_WIDTH, 20), 1)
        #     x2 += 20

        p.draw.rect(screen, RED, p.Rect(x_food, y_food, 20, 20))

        for n in plrs:
            p.draw.rect(screen, BLACK, p.Rect(n[0], n[1], 20, 20))

        p.draw.rect(screen, BLACK, p.Rect(x, y, 20, 20))

        p.display.update()
        clock.tick(5)

game()
p.quit()