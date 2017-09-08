# -*- coding:utf-8 -*-
import pygame
from pygame import *
import time


def main():
    # 创建一个窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 创建一个背景
    background = pygame.image.load('../feiji/background.png')

    # 创建一个英雄
    hero = pygame.image.load('../feiji/hero.gif')

    x = 190
    maxx = 380
    y = 700
    maxy = 725
    speed = 50

    # 将背景贴到窗口
    while True:
        screen.blit(background, (0, 0))
        screen.blit(hero, (x, y))

        # 获取事件，比如按键等
        for event in pygame.event.get():

            # 判断是否是点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()
            # 判断是否是按下了键
            elif event.type == KEYDOWN:
                # 检测按键是否是a或者left
                if event.key == K_w or event.key == K_UP:
                    print('up')
                    if y > 0:
                        y -= speed

                # 检测按键是否是d或者right
                elif event.key == K_s or event.key == K_DOWN:
                    print('down')
                    if y < maxy:
                        y += speed

                # 检测按键是否是a或者left
                if event.key == K_a or event.key == K_LEFT:
                    print('left')
                    if x > 0:
                        x -= speed

                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    if x < maxx:
                        x += speed

                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')

        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
