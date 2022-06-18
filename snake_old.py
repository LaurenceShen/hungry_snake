import pygame as pg
import sys
import random
import time

screen_size = (800, 800)
screen = pg.display.set_mode(screen_size)
pg.display.set_caption('Snake')

Grey = (192, 192, 192)
Black = (0, 0, 0)
White = (255, 255, 255)

screen.fill(White)
pg.display.flip()


class Snake:
    def __init__(self, image):
        self.pos = []
        for i in range(600, 400, -50):
            self.pos.append((i, 400))
        self.image = image
        self.speed = 50
        self.x = -(self.speed)
        self.y = 0
        for i in range(len(self.pos)):
            screen.blit(self.image, ((self.pos[i])[0], (self.pos[0])[1]))
    def move(self, barrier1, f = 0):
        if ((self.pos[-1][0] + self.x), (self.pos[-1][1] + self.y)) == barrier1.pos: 
            return 0
        pg.draw.rect(screen, White, ((self.pos[0])[0], (self.pos[0])[1], 50, 50))
        Game().draw_background()
        if f == 0:
            self.pos.pop(0)
        self.pos.append(((self.pos[-1][0] + self.x), (self.pos[-1][1]+self.y)))
        for i in self.pos:
            screen.blit(self.image, (i[0], i[1]))
        clock = pg.time.Clock()
        clock.tick(5)#不要一直衝
        if ((self.pos[-1])[0] < 0) or ((self.pos[-1])[0] > 700) or ((self.pos[-1])[1] < 0) or ((self.pos[-1])[1] > 700):
            return False
        if self.pos.count(self.pos[-1]) >= 2:
            return False
        return True


    def change_direction(self, event):
        if (event.key == pg.K_UP) or (event.key == pg.K_w):
            self.x = 0
            self.y = -(self.speed)
        elif (event.key == pg.K_DOWN) or (event.key == pg.K_s):
            self.x = 0
            self.y = (self.speed)
        elif (event.key == pg.K_RIGHT) or (event.key == pg.K_d):
            self.y = 0
            self.x = (self.speed)
        elif (event.key == pg.K_LEFT) or (event.key == pg.K_a):
            self.y = 0
            self.x = -(self.speed)

class Apple:
    def __init__(self, pos):
        image_apple = pg.image.load('apple.png').convert_alpha()
        self.image = image_apple
        self.pos = pos
        screen.blit(self.image, (self.pos[0], self.pos[1]))

class Barrier:
    def __init__(self, pos):
        image_barrier = pg.image.load('barrier.png').convert_alpha()
        self.image = image_barrier
        self.pos = pos
        screen.blit(self.image, (self.pos[0], self.pos[1]))

class Game:
    def __init__(self):
        pg.init()
        self.work = [True, True] 
        self.font = pg.font.SysFont('Times New Roman', 80)
        self.image = pg.image.load('snake.png').convert_alpha()
        self.image2 = pg.image.load('snake2.png').convert_alpha()
    def position(self):
        return (random.choice(range(0, 750, 50)), random.choice(range(0, 750, 50)))

    def draw_background(self):
        for i in range(0, 800, 50):
            pg.draw.line(screen, Grey, (0, i), (800, i) )
            pg.draw.line(screen, Grey, (i, 0), (i, 800) )

    def run(self):
        gameover = (self.font).render('Game Over', True, Black)
        apple = Apple(self.position())
        self.draw_background()
        player = Snake(self.image)
        player2 = Snake(self.image2)
        barrier1 = Barrier(self.position())
        pg.display.flip()

        while False not in self.work:
            self.work[0] = player.move(barrier1)
            self.work[1] = player2.move(barrier1)
            if apple.pos == player.pos[-1]:
                apple.__init__(self.position())
                player.move(barrier1, 1)
            elif apple.pos == player2.pos[-1]:
                apple.__init__(self.position())
                player2.move(barrier1, 1)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                elif event.type == pg.KEYDOWN:
                    if event.key in [pg.K_w, pg.K_a, pg.K_s, pg.K_d]: 
                        player2.change_direction(event)
                    else:
                        player.change_direction(event)
            pg.display.flip()

        screen.blit(gameover, (400 - (gameover.get_width()/2), 400 - (gameover.get_height()/2)))
        pg.display.flip()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        time.sleep(10)
Game().run()
