import pygame
from core.settings import TILE_SIZE, COLOR_BG, COLOR_WALL, COLOR_SNAKE, COLOR_FOOD

class Renderer:
    def __init__(self, screen_width, screen_height):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.font = pygame.font.SysFont("Arial", 20)

        # Pre-rendered map surface
        self.map_surface = pygame.Surface((screen_width, screen_height))
        self.map_surface.fill(COLOR_BG)

    def build_map_surface(self, map_obj):
        """Render the static map onto a separate surface once."""
        for y, row in enumerate(map_obj.grid):
            for x, tile in enumerate(row):
                if tile == "1":  # wall
                    pygame.draw.rect(
                        self.map_surface,
                        COLOR_WALL,
                        (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    )

    def draw_snake(self, snake):
        for (x, y) in snake.body:
            pygame.draw.rect(
                self.screen,
                COLOR_SNAKE,
                (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            )

    def draw_food(self, food):
        if food.position:
            x, y = food.position
            pygame.draw.rect(
                self.screen,
                COLOR_FOOD,
                (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            )

    def draw_score(self, score):
        text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))

    def draw(self, map_obj, snake, food, score):
        # Draw pre-rendered map
        self.screen.blit(self.map_surface, (0, 0))

        # Draw dynamic objects
        self.draw_snake(snake)
        self.draw_food(food)
        self.draw_score(score)

        pygame.display.flip()
