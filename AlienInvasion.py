# For the first development phase, we’ll make a ship that can move
# right and left and fires bullets when the player presses the spacebar.
# After setting up this behavior, we can create the aliens and refine the
# gameplay
import sys
import pygame
class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,600))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (230,230,230)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type== pygame.QUIT:
                    sys.exit()
            pygame.display.flip(self.bg_color)
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()