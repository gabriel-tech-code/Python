import pygame
from graphics.menu import Menu, MapSelectionMenu, GameOverMenu
from graphics.renderer import Renderer
from core.game import Game
from core.settings import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    while True:
        pygame.init()   # <-- IMPORTANT

        # Main menu
        menu = Menu(SCREEN_WIDTH, SCREEN_HEIGHT)
        start_game = menu.run()
        if not start_game:
            pygame.quit()
            break

        # Map selection
        map_menu = MapSelectionMenu(SCREEN_WIDTH, SCREEN_HEIGHT)
        selected_map = map_menu.run()
        if selected_map is None:
            pygame.quit()
            break

        # Start game
        renderer = Renderer(SCREEN_WIDTH, SCREEN_HEIGHT)
        game = Game(f"maps/{selected_map}", renderer)
        game.run()   # <-- DOES NOT CALL pygame.quit()

        # Game over menu
        over_menu = GameOverMenu(SCREEN_WIDTH, SCREEN_HEIGHT, win=game.win)
        result = over_menu.run()

        if result == "quit":
            pygame.quit()
            break
        # else restart loop

if __name__ == "__main__":
    main()
