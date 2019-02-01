#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pongostr.py
#  

import pygame
from pygame.locals import *
import sys

# inicjacja moduĹĂłw PyGame
pygame.init()
# przygotowanie okna gry
O_SZER, O_WYS = 800, 400
plansza = pygame.display.set_mode((O_SZER, O_WYS), 0, 32)
# tytuĹ okna gry
pygame.display.set_caption('Pong')

PAL_SZER, PAL_WYS, MAKS_V = 100, 20, 10

# paletka gracza 1
# utworzenie powierzchni paletki, wypeĹnienie jej kolorem,
pal1 = pygame.Surface([PAL_SZER, PAL_WYS])
pal1.fill((0, 0, 255))
# ustawienie prostokÄta zawierajÄcego paletkÄ w poczÄtkowej pozycji
pal1_prost = pal1.get_rect()
pal1_prost.x = 350
pal1_prost.y = 360

pal2 = pygame.Surface([PAL_SZER, PAL_WYS])
pal2.fill((255, 0, 0))
# ustawienie prostokÄta zawierajÄcego paletkÄ w poczÄtkowej pozycji
pal2_prost = pal2.get_rect()
pal2_prost.x = 350
pal2_prost.y = 20

pal3 = pygame.Surface([PAL_WYS, PAL_SZER])
pal3.fill((0, 0, 255))
# ustawienie prostokÄta zawierajÄcego paletkÄ w poczÄtkowej pozycji
pal3_prost = pal3.get_rect()
pal3_prost.x = 20
pal3_prost.y = 150

# pÄtla gĹĂłwna programu
while True:
    # obsĹuga zdarzeĹ
    for event in pygame.event.get():
        # przechwyÄ zamkniÄcie okna
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # kolor okna gry, skĹadowe RGB podane w tupli
    plansza.fill((200, 255, 255))
    plansza.blit(pal1, pal1_prost)
    plansza.blit(pal2, pal2_prost)


    # rysowanie okna
    pygame.display.update()
