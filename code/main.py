from settings import *
import pygame
from sprites import *

class Game:
    def __init__(self):
        # pygame setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Pong Practice')
        self.clock = pygame.time.Clock()
        self.running = True

        # Sprite setup
        self.all_sprites = pygame.sprite.Group()
        self.paddle_sprites = pygame.sprite.Group()
        self.player = Player((self.all_sprites, self.paddle_sprites))
        self.ball = Ball(self.all_sprites, self.paddle_sprites)
        Opponent((self.all_sprites, self.paddle_sprites), self.ball)

    def run(self):
        while self.running:
            dt = self.clock.tick(60) /1000 # limits FPS to 60
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            

            # Update the game
            self.all_sprites.update(dt)

            # Draw the game
            self.display_surface.fill(COLORS['bg'])
            self.all_sprites.draw(self.display_surface)
            pygame.display.flip()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()