#Desafio 21 - Faça um programa em python que abra e reproduza o audio de um arquivo mp3

import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('Switchfoot.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick()



