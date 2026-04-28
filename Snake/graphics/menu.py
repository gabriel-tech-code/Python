import pygame
import os
from core.settings import COLOR_BG


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
class Menu:
    def __init__(self, screen_width, screen_height):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.font_title = pygame.font.SysFont("Arial", 48)
        self.font_option = pygame.font.SysFont("Arial", 24)

        self.running = True

    def draw(self):
        self.screen.fill(COLOR_BG)

        title = self.font_title.render("SNAKE GAME", True, (255, 255, 255))
        start = self.font_option.render("Press ENTER to Start", True, (200, 200, 200))

        title_rect = title.get_rect(center=(self.screen.get_width() // 2, 150))
        start_rect = start.get_rect(center=(self.screen.get_width() // 2, 300))

        self.screen.blit(title, title_rect)
        self.screen.blit(start, start_rect)

        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return True

            self.draw()

        return False


# ---------------------------------------------------------
# MAP SELECTION MENU
# ---------------------------------------------------------
class MapSelectionMenu:
    def __init__(self, screen_width, screen_height, maps_folder="maps"):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.font_title = pygame.font.SysFont("Arial", 40)
        self.font_option = pygame.font.SysFont("Arial", 24)

        self.maps_folder = maps_folder
        self.map_files = self.load_map_files()

        self.selected_index = 0
        self.running = True

    def load_map_files(self):
        files = [f for f in os.listdir(self.maps_folder) if f.endswith(".txt")]
        return files

    def draw(self):
        self.screen.fill(COLOR_BG)

        title = self.font_title.render("Select a Map", True, (255, 255, 255))
        title_rect = title.get_rect(center=(self.screen.get_width() // 2, 80))
        self.screen.blit(title, title_rect)

        start_y = 160
        for i, map_name in enumerate(self.map_files):
            color = (255, 255, 0) if i == self.selected_index else (200, 200, 200)
            text = self.font_option.render(map_name, True, color)
            rect = text.get_rect(center=(self.screen.get_width() // 2, start_y + i * 40))
            self.screen.blit(text, rect)

        pygame.display.flip()

    def run(self):
        if not self.map_files:
            return None

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return None

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected_index = (self.selected_index - 1) % len(self.map_files)

                    elif event.key == pygame.K_DOWN:
                        self.selected_index = (self.selected_index + 1) % len(self.map_files)

                    elif event.key == pygame.K_RETURN:
                        return self.map_files[self.selected_index]

            self.draw()

        return None


# ---------------------------------------------------------
# GAME OVER MENU
# ---------------------------------------------------------
class GameOverMenu:
    def __init__(self, screen_width, screen_height, win=False):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.font_title = pygame.font.SysFont("Arial", 48)
        self.font_option = pygame.font.SysFont("Arial", 24)

        self.win = win
        self.running = True

    def draw(self):
        self.screen.fill((0, 0, 0))

        title_text = "YOU WIN!" if self.win else "GAME OVER"
        title_color = (0, 255, 0) if self.win else (255, 0, 0)

        title = self.font_title.render(title_text, True, title_color)
        restart = self.font_option.render("Press ENTER to Restart", True, (200, 200, 200))
        quit_text = self.font_option.render("Press ESC to Quit", True, (200, 200, 200))

        title_rect = title.get_rect(center=(self.screen.get_width() // 2, 150))
        restart_rect = restart.get_rect(center=(self.screen.get_width() // 2, 300))
        quit_rect = quit_text.get_rect(center=(self.screen.get_width() // 2, 350))

        self.screen.blit(title, title_rect)
        self.screen.blit(restart, restart_rect)
        self.screen.blit(quit_text, quit_rect)

        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return "restart"
                    if event.key == pygame.K_ESCAPE:
                        return "quit"

            self.draw()

        return "quit"
