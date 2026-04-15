import pygame 


class LSystem:
    def __init__(self, axiom, rules):
        self.axiom = axiom
        self.rules = rules

    def generate(self, iterations):
        current_string = self.axiom
        for _ in range(iterations):
            next_string = ""
            for char in current_string:
                next_string += self.rules.get(char, char)
            current_string = next_string
        return current_string

def main():
    pygame.init()
    screen_size = (800, 600)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("lightblue")
        pygame.display.flip()
    pygame.quit()
        

main()




# https://www.youtube.com/watch?v=QuwvbXdY9eY