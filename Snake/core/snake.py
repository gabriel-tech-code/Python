from core.enums import Direction

class Snake:
    def __init__(self, start_pos):
        self.body = [start_pos]  # list of (x, y)
        self.direction = Direction.RIGHT
        self.grow_pending = 0

    def set_direction(self, direction: Direction):
        """Prevent reversing direction directly."""
        opposite = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT,
        }

        if direction != opposite[self.direction]:
            self.direction = direction

    def update(self):
        """Move snake forward one tile."""
        head_x, head_y = self.body[0]
        dx, dy = self.direction.value

        new_head = (head_x + dx, head_y + dy)

        # Insert new head
        self.body.insert(0, new_head)

        # Remove tail unless growing
        if self.grow_pending > 0:
            self.grow_pending -= 1
        else:
            self.body.pop()

    def grow(self):
        """Increase length by one."""
        self.grow_pending += 1
