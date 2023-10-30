'''
:@Author: KiwiMax
:@Date: 2023/10/30 23:16:21
:@LastEditors: KiwiMax
:@LastEditTime: 2023/10/30 23:16:21
:Description: Area-filling algorithm including the recursion of flood_fill and scan line fill
:Copyright: Copyright (©)}) 2023 KiwiMax. All rights reserved.
'''
import pygame
import sys
import time
sys.setrecursionlimit(100000) #默认1000，难以填充较小区域 报错：maximum recursion depth exceeded
#所有代码基于边界表示法
class Stack:
    '''
    用列表来构建stack
    '''
    def __init__(self):
        self.list = []

    def isEmpty(self):
        return len(self.list) == 0

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def top(self):
        if not self.isEmpty():
            return self.list[len(self.list) - 1]

    def size(self):
        return len(self.list)


def flood_fill(screen, pixel, newColor, boundaryColor):
    '''种子填充算法主程序'''
    try:
        currentColor = screen.get_at(pixel)
        if ((currentColor != newColor) and (currentColor != boundaryColor)):  
            screen.set_at(pixel, newColor) 
            pygame.display.update()  
            px = pixel[0]
            py = pixel[1]
            flood_fill(screen,(px - 1, py),newColor,boundaryColor)  
            flood_fill(screen,(px, py - 1),newColor,boundaryColor)
            flood_fill(screen,(px + 1, py),newColor,boundaryColor)
            flood_fill(screen,(px, py + 1),newColor,boundaryColor)
    except Exception as error:
        print(error)
        sys.exit(0)
def scan_line_fill(screen, pixel, newColor, boundaryColor):
    '''扫描线填充算法主程序'''
    try:
        s = Stack()
        s.push(pixel)
        while s.isEmpty()!=True:
            point = s.top()
            s.pop()
            x = point[0]
            y = point[1]
            xr,xl=0,0
            if screen.get_at((x,y))==newColor:
                continue
            #向左
            while True:
                currentColor = screen.get_at((x,y))
                if currentColor == boundaryColor:
                    xl = x + 1
                    break
                screen.set_at((x,y), newColor) 
                pygame.display.update()  
                x = x - 1 
            x = point[0] + 1
            #向右
            while True:
                currentColor = screen.get_at((x,y))
                if currentColor == boundaryColor:
                    xr = x - 1
                    break
                screen.set_at((x,y), newColor) 
                pygame.display.update()  
                x = x + 1
            x = xl
            y = y + 1
            while x<=xr:
                spanNeedFill = False
                while screen.get_at((x,y)) != boundaryColor:
                    spanNeedFill = True
                    x = x + 1
                if(spanNeedFill):
                    s.push((x-1,y))
                    spanNeedFill = False
                while(screen.get_at((x,y))==boundaryColor or screen.get_at((x,y))==newColor) and x<=xr:
                    x = x + 1
            x = xl
            y = y - 2
            while x<=xr:
                spanNeedFill = False
                while screen.get_at((x,y))!=boundaryColor:
                    spanNeedFill = True
                    x = x + 1
                if(spanNeedFill):
                    s.push((x-1,y))
                    spanNeedFill = False
                while(screen.get_at((x,y))==boundaryColor or screen.get_at((x,y))==newColor) and x<=xr:
                    x = x + 1
    except Exception as error:
        print(error)
        sys.exit(0)
def main():
    mode = 0
    MODE = ["flood_fill","scan_line_fill"]
    WIDTH = 920
    HEIGHT = 640
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pixels = []  
    isdone = False  # 取点是否完成
    isStart = False # 画完整封闭图形是否开始
    start = 0

    # 颜色设置
    FILLCOLOR = (222, 132, 56)
    BOUNDARYCOLOR = (121, 212, 110)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (pygame.mouse.get_pressed()[0]) and not isdone:
                    pos = pygame.mouse.get_pos()
                    pixels.append(pos)
                    screen.set_at(pos, BOUNDARYCOLOR)
                    length = len(pixels)
                    print("Left btn ", pos, len(pixels), pixels)
                    if isStart == False:
                        isStart = True
                        start = length - 1
                    else:
                        pygame.draw.line(screen, BOUNDARYCOLOR, pixels[length - 2],pixels[length - 1], 2)
                if (pygame.mouse.get_pressed()[2]) and not isdone:
                    if len(pixels) - start > 2:
                        length = len(pixels)
                        pygame.draw.line(screen, BOUNDARYCOLOR, pixels[length - 1],
                                        pixels[start], 2)
                        isStart = False
                        print("Right btn")
                    else:
                        print("Need more points")
                if (pygame.mouse.get_pressed()[0]) and isdone and mode == 0:
                    pos = pygame.mouse.get_pos()
                    flood_fill(screen,pos,FILLCOLOR,BOUNDARYCOLOR)   
                    txt_font = pygame.font.SysFont(None, 32)
                    txt = txt_font.render("Complete! Press Tab to retry.", True, (255,255,255),(0,0,0))
                    txt_rect = txt.get_rect()
                    screen.blit(txt,txt_rect)
                    pygame.display.update()
                if (pygame.mouse.get_pressed()[0]) and isdone and mode == 1:
                    pos = pygame.mouse.get_pos()
                    scan_line_fill(screen,pos,FILLCOLOR,BOUNDARYCOLOR)  
                    txt_font = pygame.font.SysFont(None, 32)
                    txt = txt_font.render("Complete! Press Tab to retry.", True, (255,255,255),(0,0,0))
                    txt_rect = txt.get_rect()
                    screen.blit(txt,txt_rect)
                    pygame.display.update()
            if event.type == pygame.KEYDOWN and len(pixels)==0:
                if event.key == pygame.K_DOWN:
                    screen.fill((0,0,0))
                    mode = mode - 1
                    if mode < 0:
                        mode = 0
                if event.key == pygame.K_UP:
                    screen.fill((0,0,0))
                    mode = mode + 1
                    if mode > 1:
                        mode = 1
            if event.type == pygame.KEYDOWN and not isdone:
                if isStart != False:
                    print("Points Collecting dosen't complete")
                elif event.key == pygame.K_RETURN:
                    isdone = True
                    print("Enter btn,please choose the seed pixel")
            if event.type == pygame.KEYDOWN:  
                if event.key == pygame.K_TAB:
                    isdone = False 
                    isStart = False 
                    start = 0
                    pixels.clear()
                    screen.fill((0, 0, 0))
                    print("Reset done")
        txt_font = pygame.font.SysFont(None, 32)
        txt = txt_font.render("mode:"+MODE[mode], True, (255,255,255),(0,0,0))
        txt_rect = txt.get_rect(center=(100,620))
        screen.blit(txt,txt_rect)
        pygame.display.update()

if __name__ == "__main__":
    main()  