import pygame

class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.width = 15
        self.height = 8

        self.color = (240, 210, 60)
        self.speed = 8
        self.damage = 10
        self.direction = direction

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        self.x = self.x + self.speed * self.direction

    def is_off_screen(self, screen_width):
        return self.x < 0 or self.x > screen_width

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.get_rect())
