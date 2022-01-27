import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    pygame.display.set_caption("Alien_Invasion_by_Mohyio")
    ai_st = Settings()  # 要使用,应该先赋予其类 (类赋予)
    screen = pygame.display.set_mode((ai_st.screen_width, ai_st.screen_height))
    ship = Ship(screen)
    bg_color = ai_st.bg_color
    while True:
        gf.check_events()
        gf.update_screen(screen.ai_settings, screen, ship)
        """for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()"""
        screen.fill(bg_color)
        ship.blitme()
        pygame.display.flip()


run_game()
