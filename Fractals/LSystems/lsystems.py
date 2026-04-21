import pygame
import sys
import math

# -------------------------
# Parse L-System file
# -------------------------
def load_lsystem(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]

    axiom = lines[0]
    iterations = int(lines[1])

    rules = {}
    i = 2
    while i < len(lines) - 1:
        parts = lines[i].split()
        if len(parts) == 2:
            rules[parts[0]] = parts[1]
        i += 1

    angle = float(lines[-1])
    return axiom, iterations, rules, angle


# -------------------------
# Generate L-System string
# -------------------------
def generate_lsystem(axiom, rules, iterations):
    current = axiom
    for _ in range(iterations):
        next_string = ""
        for char in current:
            next_string += rules.get(char, char)
        current = next_string
    return current


# -------------------------
# Draw L-System
# -------------------------
class LSystemDrawer:
    def __init__(self, instructions, start_pos, length, angle, ratio):
        self.instructions = instructions
        self.index = 0

        self.x, self.y = start_pos
        self.direction = -90

        self.length = length
        self.angle = angle
        self.ratio = ratio

        self.stack = []

        self.total_steps = sum(1 for c in instructions if c in ['F', 'G'])
        self.step_count = 0

    def step(self, screen, steps_per_frame=5):
        for _ in range(steps_per_frame):
            if self.index >= len(self.instructions):
                return  # done drawing

            cmd = self.instructions[self.index]

            # 🌈 gradient
            t = self.step_count / max(1, self.total_steps)
            color = (
                int(255 * (1 - t)),
                int(255 * t),
                int(255 * t)
            )

            if cmd in ['F', 'G']:
                new_x = self.x + self.length * math.cos(math.radians(self.direction))
                new_y = self.y + self.length * math.sin(math.radians(self.direction))

                width = max(1, int(self.length / 10))
                pygame.draw.line(screen, color, (self.x, self.y), (new_x, new_y), width)

                self.x, self.y = new_x, new_y
                self.step_count += 1

            elif cmd == '+':
                self.direction += self.angle

            elif cmd == '-':
                self.direction -= self.angle

            elif cmd == '[':
                # save state INCLUDING length
                self.stack.append((self.x, self.y, self.direction, self.length))
                self.length *= self.ratio 

            elif cmd == ']':
                # restore state
                self.x, self.y, self.direction, self.length = self.stack.pop()

            self.index += 1
# -------------------------
# Main
# -------------------------
def main():
    if len(sys.argv) < 8:
        print("Usage: python lsystems.py file width height start_x start_y length ratio")
        return

    filename = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    start_x = float(sys.argv[4])
    start_y = float(sys.argv[5])
    length = float(sys.argv[6])
    ratio = float(sys.argv[7])

    axiom, iterations, rules, angle = load_lsystem(filename)
    instructions = generate_lsystem(axiom, rules, iterations)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("L-System Fractals")

    clock = pygame.time.Clock()
    running = True

    drawer = LSystemDrawer(instructions,(start_x, start_y),
    length,angle,ratio)

    screen.fill((0, 0, 0))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        drawer.step(screen, steps_per_frame=5)

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()




if __name__ == "__main__":
    main()