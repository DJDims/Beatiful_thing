import pygame
import random
import math

rd = 5
conn_range = 200
WHITE = (255, 255, 255)
ORANGE = (214, 82, 0)
PURPLE = (0, 0, 0)
BLACK = (29, 29, 29)
cent = (50,40)
balls_count = 30

width = 1366
height = 768

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Что-то красивое")
screen.fill(BLACK)
clock = pygame.time.Clock()
pygame.display.update()

class my_circle():

    counter = 0

    def __init__(self, x1, y1, sx, sy):
        self.x_cur = x1
        self.y_cur = y1
        self.x_speed = sx
        self.y_speed = sy
        my_circle.counter += 1

    def drawing(self):
        pygame.draw.circle(screen, WHITE, (self.x_cur, self.y_cur), rd)

    def flight(self):
        self.x_cur += self.x_speed
        self.x_last = self.x_cur
        self.y_cur += self.y_speed
        self.y_last = self.y_cur

    def __del__(self):
        my_circle.counter -=1

def g_nnull():
    val = random.randint(-3, 3)
    if val == 0:
        val += 1
    return val

def vector(x1, y1, x2, y2):
    if x2 > x1:
        vx = x2-x1
    else:
        vx = x1-x2
    
    if y2 > y1:
        vy = y2-y1
    else:
        vy = y1-y2
    return round(math.sqrt(pow(vx, 2) + pow(vy, 2)))

done = True

obects = [my_circle(random.randint(0, width), random.randint(0, height), g_nnull(), g_nnull()) for i in range(balls_count)] #создаем массив точек

while done:
    for a in pygame.event.get():
        if a.type == pygame.QUIT:
            done = False
        elif a.type == pygame.KEYDOWN:
            if a.key == pygame.K_ESCAPE:
                done = False

    screen.fill(BLACK) #очистка экрана
    for i in obects:    #опрашивая все объекты
        i.drawing()     #рисуем
        i.flight()      #летим

        if i.x_cur < 0 or i.x_cur > width or i.y_cur < 0 or i.y_cur > height:   #если объект вышел за пределы экрана
            obects.remove(i)    #удаляем
            obects.append(my_circle(random.randint(0, width), random.randint(0, height), g_nnull(), g_nnull())) #создаем новую точку

        for j in range(len(obects)-1):
            verctor_length = vector(i.x_cur, i.y_cur, obects[j+1].x_cur, obects[j+1].y_cur)
            if verctor_length <= conn_range:
                pygame.draw.aaline(screen, ORANGE, (i.x_cur, i.y_cur), (obects[j+1].x_cur, obects[j+1].y_cur), 2)
    pygame.display.update() #обновить экран

    clock.tick(60)
pygame.quit()
