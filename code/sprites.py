from settings import *
from random import choice, uniform

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        
        # Player image
        self.image = pygame.Surface(SIZE['paddle'], pygame.SRCALPHA)
        # When we draw the rectangle, we want to get a tuple for the position and the size. By default, we utilize the top left position.
        pygame.draw.rect(self.image, COLORS['paddle'], pygame.FRect((0,0), SIZE['paddle']), 0, 3)

        # Player rectangle and movement
        self.rect = self.image.get_frect(center = POS['player'])
        self.direction = 0
        self.speed = SPEED['player']
        
    def move(self, dt):
        self.rect.centery += self.direction * self.speed * dt
        self.rect.top = 0 if self.rect.top < 0 else self.rect.top
        self.rect.bottom = WINDOW_HEIGHT if self.rect.bottom > WINDOW_HEIGHT else self.rect.bottom

    def get_direction(self):
        keys = pygame.key.get_pressed()
        self.direction = int(keys[pygame.K_s]) - int(keys[pygame.K_w])

    # def collision(self):
    #     pass

    def update(self, dt):
        self.get_direction()
        self.move(dt)

class Ball(pygame.sprite.Sprite):
    def __init__(self, groups, paddle_sprites):
        super().__init__(groups)
        
        # Ball image
        self.image = pygame.Surface(SIZE['ball'], pygame.SRCALPHA)
        # To draw the circle, we're getting the width and cutting it in half, then we grab the height and cut it in half, finally we get a radius that starts at the center and touches the outer surface. 
        pygame.draw.circle(self.image, COLORS['ball'], (SIZE['ball'][0] / 2,SIZE['ball'][1] / 2 ), SIZE['ball'][0] / 2)
    
        # Rectangle and movement
        self.rect = self.image.get_frect(center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        # Using choice and uniform to create two random values for the x and y of the ball
        self.direction = pygame.Vector2(choice((1, -1)), uniform(0.7, 0.8) * choice((-1, 1)))

    def move(self, dt):
        self.rect.center += self.direction * SPEED['ball'] * dt

    def wall_collision(self):
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1

        if self.rect.bottom >= WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            self.direction.y *= -1

        if self.rect.right >= WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
            self.direction.x *= -1

        if self.rect.left <= 0:
            self.rect.left = 0
            self.direction.x *= -1


    def update(self, dt):
        self.wall_collision()
        self.move(dt)