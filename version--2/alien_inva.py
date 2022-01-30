import pygame
import sys

from settings import Settings
from ship import Ship
import game_func as gf


def run_game():
    pygame.init()
    pygame.display.set_caption("Alien_Invasion_by_Mohini")
    ai_st = Settings()
    screen = pygame.display.set_mode((ai_st.screen, width, ai_st.screen_height))
    ship = Ship(screen)
    bg_color = ai_st.bg_color
    while True:
        gf.check_events()
