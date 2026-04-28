import random

class Food:
    def __init__(self, map_ref):
        self.map = map_ref
        self.position = None

    def spawn(self, snake_body=None):
        """Spawn food on a random walkable tile not occupied by the snake."""
        valid_tiles = self._get_valid_tiles(snake_body)

        if not valid_tiles:
            # No valid tiles left — snake fills the map
            self.position = None
            return

        self.position = random.choice(valid_tiles)

    def _get_valid_tiles(self, snake_body):
        """Return all walkable tiles that are not walls or snake body."""
        valid = []

        for y in range(self.map.height):
            for x in range(self.map.width):

                # Must be walkable
                if not self.map.is_walkable(x, y):
                    continue

                # Must not be on snake
                if snake_body and (x, y) in snake_body:
                    continue

                valid.append((x, y))

        return valid
