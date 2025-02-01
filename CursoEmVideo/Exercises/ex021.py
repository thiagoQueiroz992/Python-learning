"""EXERCÍCIO 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3."""

import pygame
from time import sleep
pygame.init()
pygame.mixer.music.load('ex021music.mp3')
pygame.mixer.music.play()

sleep(64)

pygame.event.wait(10)