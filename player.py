import pygame

from bullet import Bullet


class Player:
    def __init__(self, x, y, color, controls, direction):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 70
        self.color = color

        self.hp = 100
        self.speed = 5

        self.controls = controls
        self.direction = direction

        self.shoot_cooldown = 0

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, keys, screen_width, screen_height):
        if keys[self.controls["up"]] and self.y > 0:
            self.y = self.y - self.speed

        if keys[self.controls["down"]] and self.y < screen_height - self.height:
            self.y = self.y + self.speed

        if keys[self.controls["left"]] and self.x > 0:
            self.x = self.x - self.speed

        if keys[self.controls["right"]] and self.x < screen_width - self.width:
            self.x = self.x + self.speed

    def update_cooldown(self):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown = self.shoot_cooldown - 1

    def can_shoot(self):
        return self.shoot_cooldown == 0

    def shoot(self):
        self.shoot_cooldown = 20

        if self.direction == 1:
            bullet_x = self.x + self.width
        else:
            bullet_x = self.x

        bullet_y = self.y + self.height // 2

        return Bullet(bullet_x, bullet_y, self.direction)

    def take_damage(self, damage):
        self.hp = self.hp - damage

        if self.hp < 0:
            self.hp = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.get_rect())
