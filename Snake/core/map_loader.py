class Map:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.grid = []
        self.width = 0
        self.height = 0
        self.start_pos = None

        self.load()

    def load(self):
        """Load map file and convert to 2D grid."""
        with open(self.file_path, "r") as f:
            lines = [line.rstrip("\n") for line in f if line.strip() != ""]

        self.height = len(lines)
        self.width = len(lines[0])

        for y, line in enumerate(lines):
            row = []
            for x, char in enumerate(line):
                row.append(char)

                if char == "2":
                    self.start_pos = (x, y)

            self.grid.append(row)

    def is_wall(self, x, y):
        return self.grid[y][x] == "1"

    def is_walkable(self, x, y):
        return self.grid[y][x] in ("0", "2")

    def get_start_position(self):
        return self.start_pos

    def count_playable_tiles(self):
        count = 0
        for row in self.grid:
            for tile in row:
                if tile in ("0", "2"):
                    count += 1
        return count