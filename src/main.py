# -*- coding:utf-8 -*-
import pygame
import time

def main():
	#创建一个窗口
	screen = pygame.display.set_mode((480,852),0,32)

	#创建一个背景
	background = pygame.image.load('../feiji/background.png')

	#将背景贴到窗口
	while True:
		screen.blit(background,(0,0))
		pygame.display.update()
		time.sleep(0.1)


if __name__=='__main__':
	main()
