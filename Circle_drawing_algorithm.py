'''
:@Author: KiwiMax
:@Date: 2023/10/18 00:48:24
:@LastEditors: KiwiMax
:@LastEditTime: 2023/10/18 00:48:24
:Description: Circle and ellipse drawing algorithm with 3+1(False) algorithms, including mid-point and Bresenham
:Copyright: Copyright (©)}) 2023 KiwiMax. All rights reserved.
'''
import time
import pygame
import sys
from math import sqrt

def swap(a, b):
    return b, a
width = 920  # 画板宽度
height = 640  # 画版高度

clock = pygame.time.Clock()
def circle_point(screen,x,y,dx,dy):
    pygame.draw.circle(screen, (255, 255, 255), (x+dx, y+dy), 1, 1)
    time.sleep(0.001)
    pygame.display.update()
    pygame.draw.circle(screen, (255, 255, 255), (x+dy, y+dx), 1, 1)
    time.sleep(0.001)
    pygame.display.update()
    pygame.draw.circle(screen, (255, 255, 255), (x-dx, y+dy), 1, 1)
    time.sleep(0.001)
    pygame.display.update()
    pygame.draw.circle(screen, (255, 255, 255), (x+dy, y-dx), 1, 1)
    time.sleep(0.001)
    pygame.display.update()
    pygame.draw.circle(screen, (255, 255, 255), (x+dx, y-dy), 1, 1)
    time.sleep(0.001)
    pygame.display.update()
    pygame.draw.circle(screen, (255, 255, 255), (x-dy, y+dx), 1, 1)
    time.sleep(0.001)
    pygame.display.update()
    pygame.draw.circle(screen, (255, 255, 255), (x-dx, y-dy), 1, 1)
    time.sleep(0.001)
    pygame.display.update()
    pygame.draw.circle(screen, (255, 255, 255), (x-dy, y-dx), 1, 1)
    time.sleep(0.001)
    pygame.display.update()

def mid_point_circle(screen, x1, y1, x2, y2):
    R = (int)(sqrt((x2-x1)**2+(y2-y1)**2))
    x = 0
    y = R
    d = 1 - R
    circle_point(screen,x1,y1,x,y)
    while(x<=y):
        if d < 0:
            d = d + 2*x +3
        else:
            d = d + 2*(x-y) +5
            y = y -1
        x = x +1
        circle_point(screen,x1,y1,x,y)

def bresenham_circle(screen,x1,y1,x2,y2):
    R = (int)(sqrt((x2-x1)**2+(y2-y1)**2))
    x = 0
    y = R
    delta1 = 2*x - 2*y +2
    circle_point(screen,x1,y1,x,y)
    while y >= x:
        if delta1 > 0:
            if delta1 - 2*x -1 > 0:
                y = y - 1
                delta1 = delta1 - 2*y +1
            else:
                x = x + 1
                y = y - 1
                delta1 = delta1 + 2*x - 2*y +2
        elif delta1 < 0:
            if delta1 + 2*y -1 <= 0:
                x = x + 1
                delta1 = delta1 + 2*x +1
            else:
                x = x + 1
                y = y - 1
                delta1 = delta1 + 2*x - 2*y +2
        else:
            x = x + 1
            y = y - 1
            delta1 = delta1 + 2*x - 2*y +2
        circle_point(screen,x1,y1,x,y)
def ellipse_point(screen,x0,y0,dx,dy):
    pygame.draw.circle(screen, (255, 255, 255), (x0+dx, y0+dy), 1, 1)
    time.sleep(0.001)
    pygame.display.update()
    pygame.draw.circle(screen, (255, 255, 255), (x0-dx, y0+dy), 1, 1)
    time.sleep(0.001)
    pygame.display.update()
    pygame.draw.circle(screen, (255, 255, 255), (x0+dx, y0-dy), 1, 1)
    time.sleep(0.001)
    pygame.display.update()
    pygame.draw.circle(screen, (255, 255, 255), (x0-dx, y0-dy), 1, 1)
    time.sleep(0.001)
    pygame.display.update()
def mid_point_ellipse_horizontal(screen,x1,y1,x2,y2,x3,y3):
    l1 = sqrt(((x3-x1)**2)+((y3-y1)**2))
    l2 = sqrt(((x3-x2)**2)+((y3-y2)**2))
    l3 = sqrt(((x2-x1)**2)+((y2-y1)**2))
    c = l3/2
    a = ((l1+l2)/2)
    b = (sqrt(a**2-c**2))
    x = 0
    y = (int)(b)
    d = 2*b**2*x+b**2-a**2*y+a**2/4
    ellipse_point(screen,(int)((x1+x2)/2),(int)((y1+y2)/2),x,y)
    while b**2*x < a**2*y:
        if d > 0:
            d = d + 2*b**2*x + 3*b**2 - 2*a**2*y + a**2*2
            x = x+1
            y = y-1
        else:
            d = d + 2*b**2*x + 3*b**2
            x = x+1
        ellipse_point(screen,(int)((x1+x2)/2),(int)((y1+y2)/2),x,y)
    4
    while y>=0:
        if d > 0:
            d = d - 2*a**2*y + a**2*3
            y = y - 1
        else:
            d = d + 2*b**2*x + b**2*2 - 2*a**2*y + a**2*3
            x = x + 1
            y = y - 1
        ellipse_point(screen,(int)((x1+x2)/2),(int)((y1+y2)/2),x,y)

def mid_point_ellipse_vetical(screen,x1,y1,x2,y2,x3,y3):
    l1 = sqrt(((x3-x1)**2)+((y3-y1)**2))
    l2 = sqrt(((x3-x2)**2)+((y3-y2)**2))
    l3 = sqrt(((x2-x1)**2)+((y2-y1)**2))
    c = l3/2
    a = ((l1+l2)/2)
    b = (sqrt(a**2-c**2))
    x = 0
    y = (int)(a)
    d = 2*a**2*x+a**2-b**2*y+b**2/4
    ellipse_point(screen,(int)((x1+x2)/2),(int)((y1+y2)/2),x,y)
    while a**2*x < b**2*y:
        if d > 0:
            d = d + 2*a**2*x + 3*a**2 - 2*b**2*y + b**2*2
            x = x+1
            y = y-1
        else:
            d = d + 2*a**2*x + 3*a**2
            x = x+1
        ellipse_point(screen,(int)((x1+x2)/2),(int)((y1+y2)/2),x,y)
    d = a**2*x + a**2/4 - 2*b**2*y + b**2
    while y>=0:
        
        if d > 0:
            d = d - 2*b**2*y + b**2*3
            y = y - 1
        else:
            d = d + 2*a**2*x + a**2*2 - 2*b**2*y + b**2*3
            x = x + 1
            y = y - 1
        ellipse_point(screen,(int)((x1+x2)/2),(int)((y1+y2)/2),x,y)
                   

def BresenhamEllipse(screen,x1,y1,x2,y2,x3,y3):
    l1 = (sqrt((x3-x1)**2+(y3-y1)**2))
    l2 = (sqrt((x2-x1)**2+(y2-y1)**2))
    l3 = (sqrt((x2-x1)**2+(y2-y1)**2))
    a = ((l1+l2)/2)
    b = (sqrt(a**2+(l3**2)/4))
    x = 0
    y = b
    ellipse_point(screen,(int)((x1+x2)/2),(int)((y1+y2)/2),x,y)
    delta1 = 2*(b**2)*x + b**2 - 2*(a**2)*y +a**2 
    while y>=0:
        if delta1 > 0:
            if delta1 - (2*(b**2)*x + b**2) > 0:
                y = y - 1
                delta1 = delta1 -(2*(a**2)*y) + a**2
            else:
                x = x + 1
                y = y - 1
                delta1 = delta1 +(2*(b**2)*x) + b**2 -(2*(a**2)*y) + a**2
        elif delta1 < 0:
            if delta1 - (2*(a**2)*y - a**2) <= 0:
                x = x + 1
                delta1 = delta1 +(2*(b**2)*x) + b**2 
            else:
                x = x + 1
                y = y - 1
                delta1 = delta1 +(2*(b**2)*x) + b**2 -(2*(a**2)*y) + a**2
        else:
            x = x + 1
            y = y - 1
            delta1 = delta1 +(2*(b**2)*x) + b**2 -(2*(a**2)*y) + a**2
        ellipse_point(screen,(int)((x1+x2)/2),(int)((y1+y2)/2),x,y)


def main():
    mode = 0
    MODE = ["MidPointCircle","BresenhamCircle","MidPointEllipse(Horizontal)","MidPointEllipse(Vertical)"]
    isp = False
    x1 = y1 = x2 = y2 = x3 = y3 = -1
    dot1 = (x1,y1)
    dot2 = (x2,y2)
    dot3 = (x3,y3)
    R = 0.0
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Circle_drawing_algorithm")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if x1 < 0:
                    x1, y1 = event.pos
                elif x2 < 0:
                    x2, y2 = event.pos
                else:
                    x3, y3 = event.pos
                if mode == 2 and x2 != -1 and x3 == -1:
                    pygame.draw.circle(screen, (255, 255, 255), (x2,y1), 1, 1)
                elif mode == 3 and x2 != -1 and x3 == -1:
                    pygame.draw.circle(screen, (255, 255, 255), (x1,y2), 1, 1)
                else:
                    pygame.draw.circle(screen, (255, 255, 255), event.pos, 1, 1)
                print('(', x1, ',', y1, ')', '  (', x2, ',', y2, ')', '(', x3, ',', y3, ')')
            if (mode != 2 and mode != 3 and x2 > 0) or ((mode == 2 or mode ==3) and x3 > 0):
                isp = True
            if (pygame.mouse.get_pressed()[2]): 
                x1 = y1 = x2 = y2 = x3 = y3 = -1
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
                    if mode > 3:
                        mode = 3
        if (isp):
            isp = False
            time.sleep(0.5)  
            if mode == 0:
                mid_point_circle(screen, x1, y1, x2, y2)
            elif mode == 1:
                bresenham_circle(screen, x1, y1, x2, y2)
            elif mode == 2:
                mid_point_ellipse_horizontal(screen, x1, y1, x2, y1, x3, y3)
            elif mode == 3:
                mid_point_ellipse_vetical(screen, x1, y1, x1, y2, x3, y3)
            x1 = y1 = x2 = y2 = x3 = y3= -1

        txt_font = pygame.font.SysFont(None, 32)
        txt = txt_font.render("mode:"+MODE[mode], True, (255,255,255),(0,0,0))
        txt_rect = txt.get_rect()
        screen.blit(txt,txt_rect)
        pygame.display.update()
        
        # clock.tick(120)
if __name__ == "__main__":
    main()