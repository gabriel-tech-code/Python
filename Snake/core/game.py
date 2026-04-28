import pygame
from core.settings import FPS
from core.enums import Direction
from core.snake import Snake
from core.food import Food
from core.map_loader import Map

class Game:
    def __init__(self, map_path, renderer):
        self.clock = pygame.time.Clock()

        self.map = Map(map_path)
        self.snake = Snake(self.map.get_start_position())
        self.food = Food(self.map)
        self.food.spawn(self.snake.body)

        self.renderer = renderer
        self.renderer.build_map_surface(self.map)

        self.running = True
        self.score = 0

        # Count playable tiles (0 and 2)
        self.playable_tiles = self.map.count_playable_tiles()

        # Win when snake fills all but 5 tiles
        self.win_length = self.playable_tiles - 5
        self.win = False

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.set_direction(Direction.UP)
                elif event.key == pygame.K_DOWN:
                    self.snake.set_direction(Direction.DOWN)
                elif event.key == pygame.K_LEFT:
                    self.snake.set_direction(Direction.LEFT)
                elif event.key == pygame.K_RIGHT:
                    self.snake.set_direction(Direction.RIGHT)

    def check_collisions(self):
        head_x, head_y = self.snake.body[0]

        # Bounds check (IMPORTANT)
        if head_x < 0 or head_x >= self.map.width or head_y < 0 or head_y >= self.map.height:
            self.running = False
            return

        # Wall collision
        if self.map.is_wall(head_x, head_y):
            self.running = False
            return

        # Self collision
        if (head_x, head_y) in self.snake.body[1:]:
            self.running = False
            return

    def update(self):
        self.snake.update()
        self.check_collisions()

        if not self.running:
            return

        # Food eaten
        if self.snake.body[0] == self.food.position:
            self.snake.grow()
            self.score += 1
            self.food.spawn(self.snake.body)

        # Win condition
        if len(self.snake.body) >= self.win_length:
            self.running = False
            self.win = True
            return

    def render(self):
        self.renderer.draw(self.map, self.snake, self.food, self.score)

    def run(self):
        while self.running:
            self.handle_input()
            self.update()
            self.render()
            self.clock.tick(FPS)

    pygame.quit()
