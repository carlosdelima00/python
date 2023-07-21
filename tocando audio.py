import pygame
import random
pygame.init()
music = ['test.mp3.mp3','tek it.mp3']
pygame.mixer.music.load(random.choice(music))
pygame.mixer.music.play()
input()
pygame.event.wait()