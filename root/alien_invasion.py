import sys
import pygame

from settings import Settings
ai_st = Settings()      # 要使用,应该先赋予其类 (类赋予)

def run_game():
    pygame.init()
    pygame.display.set_caption("Alien_Invasion_by_Mohyio")
    screen = pygame.display.set_mode((ai_st.screen_witdth,ai_st.screen_height))
    bg_color = ai_st.bg_color
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()

run_game()