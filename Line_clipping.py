'''
:@Author: KiwiMax
:@Date: 2023/10/30 23:16:31
:@LastEditors: KiwiMax
:@LastEditTime: 2023/10/30 23:16:31
:Description: The algorithm of Liang_Baskey line clip 
:Copyright: Copyright (©)}) 2023 KiwiMax. All rights reserved.
'''
import pygame
import sys
import time
u1=0.0
u2=0.0   
# 颜色设置

border_x1,border_y1,border_x2,border_y2=-1,-1,-1,-1
LINECOLOR = (222, 132, 56)
BORDERCOLOR = (83, 94, 114)
LINE2COLOR = (99, 154, 114)
pixels = []
Lines = []  
lines = []
start_line = 0
def borderDraw(screen):
    global border_x1,border_y1,border_x2,border_y2
    pygame.draw.line(screen, BORDERCOLOR, (border_x1,border_y1),(border_x1,border_y2), 2)
    pygame.draw.line(screen, BORDERCOLOR, (border_x1,border_y2),(border_x2,border_y2), 2)
    pygame.draw.line(screen, BORDERCOLOR, (border_x2,border_y2),(border_x2,border_y1), 2)
    pygame.draw.line(screen, BORDERCOLOR, (border_x2,border_y1),(border_x1,border_y1), 2)
    for i in range(0,len(lines)):
        (x1,y1,x2,y2) = lines[i]
        pygame.draw.line(screen, LINE2COLOR, (x1,y1),(x2,y2), 2)
    for i in range(start_line,len(Lines)):
        (x1,y1,x2,y2) = Lines[i]
        pygame.draw.line(screen, LINECOLOR, (x1,y1),(x2,y2), 2)
    pygame.display.update()
def ClipT(p,q):
    global u1 
    global u2
    if p<0:
        r=(float)(q/p)
        if r>u2:
            return False
        if r>u1:
            u1=r
    elif p>0:
        r=(float)(q/p)
        if r<u1:
            return False
        if r<u2:
            u2=r
    else:
        return q>=0
    return True
def LB_LineClip(screen,x1,y1,x2,y2,XL,XR,YB,YT):
    global u1 
    global u2
    u1,u2=0.0,1.0
    dx = (float)(x2-x1)
    dy = (float)(y2-y1)
    if ClipT(-dx,x1-XL):
        if ClipT(dx,XR-x1):
            if ClipT(-dy,y1-YB):
                if ClipT(dy,YT-y1):
                    lines.append((x1+u1*dx,y1+u1*dy,x1+u2*dx,y1+u2*dy))
                    pygame.draw.line(screen, LINE2COLOR, (x1+u1*dx,y1+u1*dy),(x1+u2*dx,y1+u2*dy), 2)
                    pygame.display.update()
def main():
    mode = 0
    MODE = ["Liang_Barskey"]
    WIDTH = 920
    HEIGHT = 640
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    global start_line
    border_complete = False
    global border_x1,border_y1,border_x2,border_y2
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pressed()[0]) and border_complete:
                    pos = pygame.mouse.get_pos()
                    pixels.append(pos)
                    length = len(pixels)
                    if length == 2:
                        Lines.append((pixels[0][0],pixels[0][1],pixels[1][0],pixels[1][1]))
                        pygame.draw.line(screen, LINECOLOR, pixels[0],pixels[1], 2)
                        pixels.clear()
                        pygame.display.update()
                
                if (pygame.mouse.get_pressed()[0]) and not border_complete:
                    if border_x1!=-1:
                        border_x2,border_y2=pygame.mouse.get_pos()
                        border_complete=True
                        borderDraw(screen)
                        pygame.display.update()
                    else:
                        border_x1,border_y1=pygame.mouse.get_pos()
            if event.type == pygame.KEYDOWN and len(Lines)!=0:
                if event.key == pygame.K_RETURN :
                    screen.fill((0, 0, 0))
                    borderDraw(screen)
                    for (x1,y1,x2,y2) in Lines:
                        start_line = start_line + 1
                        screen.fill((0, 0, 0))
                        borderDraw(screen)
                        LB_LineClip(screen,x1,y1,x2,y2,border_x1,border_x2,border_y1,border_y2)
                        time.sleep(1)
                        
                    txt_font = pygame.font.SysFont(None, 32)
                    txt = txt_font.render("Complete! Press Tab to retry.", True, (255,255,255),(0,0,0))
                    txt_rect = txt.get_rect()
                    screen.blit(txt,txt_rect)
                    pygame.display.update()
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_TAB:
                    border_complete = False
                    pixels.clear()
                    Lines.clear()
                    lines.clear()
                    start_line = 0
                    screen.fill((0, 0, 0))
                    border_x1,border_y1,border_x2,border_y2=-1,-1,-1,-1
                    print("Reset done")
        txt_font = pygame.font.SysFont(None, 32)
        txt = txt_font.render("mode:"+MODE[mode], True, (255,255,255),(0,0,0))
        txt_rect = txt.get_rect(center=(150,620))
        screen.blit(txt,txt_rect)
        pygame.display.update()

if __name__ == "__main__":
    main()  