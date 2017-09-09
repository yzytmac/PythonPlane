# -*- coding:utf-8 -*-
import pygame
from pygame import *
import time

speed = 50


class HeroPlane(object):
    def __init__(self, screen):
        self.x = 190
        self.maxx = 380
        self.y = 700
        self.maxy = 725
        self.img = pygame.image.load('../feiji/hero.gif')
        self.screen = screen
        self.bullte_list = []
		

    def display(self):
        self.screen.blit(self.img,(self.x,self.y))
        for b in self.bullte_list:
			b.display()

    def up(self):
        if self.y > 0:
            self.y -= speed

    def down(self):
        if self.y < self.maxy:
            self.y += speed

    def left(self):
        if self.x > 0:
            self.x -= speed

    def right(self):
        if self.x < self.maxx:
            self.x += speed
            
    def shoot(self):
        self.bullte_list.append(Bullet(self))
        
            

 
		

class Bullet(object):
	def __init__(self,plane):
		self.x = plane.x+40
		self.y = plane.y-10
		self.screen = plane.screen
		self.img = pygame.image.load('../feiji/bullet.png')
		
	def display(self):
		self.screen.blit(self.img,(self.x,self.y))
		self.y-=5

def PlaneContral(plane):
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
                plane.up()

            # 检测按键是否是d或者right
            elif event.key == K_s or event.key == K_DOWN:
                print('down')
                plane.down()

            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                plane.left()

            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                plane.right()

            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                plane.shoot()


def main():
    # 创建一个窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 创建一个背景
    background = pygame.image.load('../feiji/background.png')

    # 创建一个英雄
    hero = HeroPlane(screen)

    # 将背景贴到窗口
    while True:
        screen.blit(background, (0, 0))
        hero.display()
        PlaneContral(hero)
        pygame.display.update()
        time.sleep(0.01)


if __name__ == '__main__':
    main()
