'''
Author: KiwiMax MaxAndFelixZheng@outlook.com
Date: 2023-10-16 19:40:25
LastEditors: MaxAndFelix MaxAndFelixZheng@outlook.com
LastEditTime: 2023-10-17 16:01:42
FilePath: \The-implementation-computer-graphics\Line_drawing_algorithm.py
Description: Line drawing algorithm with 3 algorithms, includiing DDA,mid-point and Bresenham
'''

import time
import pygame
import sys

width = 920  # 画板宽度
height = 640  # 画版高度
isp = False
mode = 0
x1 = y1 = x2 = y2 = -1
ps = (x1, y1)
pe = (x2, y2)
MODE = ["MidPointLine","DDALine","Bresenham"]
clock = pygame.time.Clock()

def swap(a, b):
    return b, a

#Bresenham改进算法
def Bresenham(screen, x1, y1, x2, y2):
    if (x1 > x2): 
        x1, x2 = swap(x1, x2)
        y1, y2 = swap(y1, y2)
    flag = 0
    dx = x2 - x1
    dy = y2 - y1
    x = x1
    y = y1
    if abs(dx) < abs(dy):
        flag = 1
    if flag == 0:
        e = (float)(-dx)
    else:
        e = (float)(-dy)  
    if y1 < y2:
        if flag == 0:
            for i in range(dx):
                pygame.draw.circle(screen, (255, 255, 255), (x, y), 1, 1)
                x = x + 1
                e = e + 2*dy
                if(e>=0):
                    y = y + 1
                    e = e - 2*dx
                time.sleep(0.03)
                pygame.display.update()
        else:   
            for i in range(dy):
                pygame.draw.circle(screen, (255, 255, 255), (x, y), 1, 1)
                y = y + 1
                e = e + 2*dx
                if(e>=0):
                    x = x + 1
                    e = e - 2*dy
                time.sleep(0.03)
                pygame.display.update()
    else:
        e = -e
        if flag == 0:
            for i in range(dx):
                pygame.draw.circle(screen, (255, 255, 255), (x, y), 1, 1)
                x = x + 1
                e = e + 2*dy
                if(e<=0):
                    y = y - 1
                    e = e + 2*dx
                time.sleep(0.03)
                pygame.display.update()
        else:   
            for i in range(-dy):
                pygame.draw.circle(screen, (255, 255, 255), (x, y), 1, 1)
                y = y - 1
                e = e - 2*dx
                if(e<=0):
                    x = x + 1
                    e = e - 2*dy
                time.sleep(0.03)
                pygame.display.update()

# DDA算法画白线:
def DDALine(screen, x1, y1, x2, y2):
    flag = 0
    dx = x2 - x1
    dy = y2 - y1
    if (abs(dx) < abs(dy)): 
        x1, y1 = swap(x1, y1)
        x2, y2 = swap(x2, y2)
        flag = 1
    if (x1 > x2): 
        x1, x2 = swap(x1, x2)
        y1, y2 = swap(y1, y2)
    if y1 < y2 :
        k = (float)(dy / dx)
        y = (float)(y1)
        while x1 <= x2:
            if flag == 0:
                pygame.draw.circle(screen, (255, 255, 255), (x1, (int)(y)), 1, 1)
                time.sleep(0.03)
                pygame.display.update() 
                y = y + k
                x1 = x1 +1
            else:
                pygame.draw.circle(screen, (255, 255, 255), ((int)(y), x1), 1, 1)
                time.sleep(0.03)
                pygame.display.update() 
                y = y + 1/k
                x1 = x1 +1 
            
    else:
        k = (float)(dy / dx)
        y = (float)(y1)
        while x1 <= x2:
            if flag == 0:
                pygame.draw.circle(screen, (255, 255, 255), (x1, (int)(y)), 1, 1)
                time.sleep(0.03)
                pygame.display.update()
                y = y + k
                x1 = x1 + 1
            else:
                pygame.draw.circle(screen, (255, 255, 255), ((int)(y), x1), 1, 1)
                time.sleep(0.03)
                pygame.display.update()
                y = y + 1/k
                x1 = x1 + 1 
            
# 中点划线法画白线
def MidPointLine(screen, x1, y1, x2, y2):
    flag = 0
    dx = x2 - x1
    dy = y2 - y1
    if (abs(dx) < abs(dy)): 
        x1, y1 = swap(x1, y1)
        x2, y2 = swap(x2, y2)
        flag = 1
    if (x1 > x2):
        x1, x2 = swap(x1, x2)
        y1, y2 = swap(y1, y2)
    a = y1 - y2
    b = x2 - x1
    d = 2*a + b
    d1 = 2*a
    d2 = 2*(a + b)
    d2_ = 2*(a - b)
    if (y1 < y2):
        x = x1
        y = y1
        while (x < x2):
            if (d < 0):
                y = y + 1
                x = x + 1
                d = d + d2
            else:
                d = d + d1
                x = x + 1
            if (flag):
                pygame.draw.circle(screen, (255, 255, 255), (y, x), 1, 1)  
            else:
                pygame.draw.circle(screen, (255, 255, 255), (x, y), 1, 1)
            time.sleep(0.03)
            pygame.display.update()
    else:
        x = x2
        y = y2
        while (x > x1):
            if (d < 0):
                y = y + 1
                x = x - 1
                d = d - d2_
            else:
                x = x - 1
                d = d - d1
            if (flag):
                pygame.draw.circle(screen, (255, 255, 255), (y, x), 1, 1)
            else:
                pygame.draw.circle(screen, (255, 255, 255), (x, y), 1, 1)
            time.sleep(0.03)
            pygame.display.update()


pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Line_drawing_algorithm")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if x1 < 0:
                x1, y1 = event.pos
            else:
                x2, y2 = event.pos
            pygame.draw.circle(screen, (255, 255, 255), event.pos, 1, 1)
            print('(', x1, ',', y1, ')', '  (', x2, ',', y2, ')')
            if (x2 > 0):
                isp = True
            if (pygame.mouse.get_pressed()[2]): 
                x1 = y1 = x2 = y2 = -1
                screen.fill((0, 0, 0))
                print("Reset done")

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                screen.fill((0,0,0))
                x1 = y1 = x2 = y2 = -1
                mode = mode - 1
                if mode < 0:
                    mode = 0
            if event.key == pygame.K_UP:
                screen.fill((0,0,0))
                x1 = y1 = x2 = y2 = -1
                mode = mode + 1
                if mode > 2:
                    mode = 2

    if (isp):
        isp = False
        time.sleep(0.5)  
        if mode == 0:
            MidPointLine(screen, x1, y1, x2, y2)
        elif mode == 1:
            DDALine(screen,x1,y1,x2,y2)
        elif mode == 2:
            Bresenham(screen,x1,y1,x2,y2)
        x1 = y1 = x2 = y2 = -1

    txt_font = pygame.font.SysFont(None, 32)
    txt = txt_font.render("mode:"+MODE[mode], True, (255,255,255),(0,0,0))
    txt_rect = txt.get_rect()
    screen.blit(txt,txt_rect)
    pygame.display.update()
    clock.tick(120)

sys.exit()