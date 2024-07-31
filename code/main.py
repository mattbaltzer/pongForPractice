from settings import *
from sprites import *
from groups import AllSprites
import pygame
import json

class Game:
    def __init__(self):
        # pygame setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Pong Practice')
        self.clock = pygame.time.Clock()
        self.running = True

        # Sprite setup
        self.all_sprites = AllSprites()
        self.paddle_sprites = pygame.sprite.Group()
        self.player = Player((self.all_sprites, self.paddle_sprites))
        self.ball = Ball(self.all_sprites, self.paddle_sprites, self.update_score)
        Opponent((self.all_sprites, self.paddle_sprites), self.ball)

        # Creating score dictionary and saving the info
        try:
            with open(join('data', 'score.txt')) as score_file:
                self.score = json.load(score_file)
        except:
            self.score = {'player': 0, 'opponent': 0}
        self.font = pygame.font.Font(None, 160)

    def display_score(self):
        # The player score
        player_surf = self.font.render(str(self.score['player']), True, COLORS['bg detail'])
        player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2 + 100, WINDOW_HEIGHT / 2))
        self.display_surface.blit(player_surf, player_rect)

        # The opponent score
        opponent_surf = self.font.render(str(self.score['opponent']), True, COLORS['bg detail'])
        opponent_rect = opponent_surf.get_frect(center = (WINDOW_WIDTH / 2 - 100, WINDOW_HEIGHT / 2))
        self.display_surface.blit(opponent_surf, opponent_rect)

        # Line separator
        pygame.draw.line(self.display_surface, COLORS['bg detail'], (WINDOW_WIDTH / 2, 0), (WINDOW_WIDTH / 2, WINDOW_HEIGHT), 10)

    def update_score(self, side):
        self.score['player' if side == 'player' else 'opponent'] += 1

    def run(self):
        while self.running:
            dt = self.clock.tick(60) /1000 # limits FPS to 60
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    with open(join('data', 'score.txt'), 'w') as score_file:
                        json.dump(self.score, score_file)

            # Update the game
            self.all_sprites.update(dt)

            # Draw the game
            self.display_surface.fill(COLORS['bg'])
            self.display_score()
            self.all_sprites.draw()
            pygame.display.flip()
        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()