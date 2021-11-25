import pygame
from menu.Game import Game

g = Game()

while g.running:
    # g.window.blit(g.back_ground, (g.DISPLAY_W / 2, g.DISPLAY_H / 2))
    g.curr_menu.display_menu()
    g.game_loop()
