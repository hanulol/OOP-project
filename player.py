import pygame

from bullet import Bullet
from red_bullet import Red_Bullet
from yellow_bullet import Yellow_Bullet

class Player:
    def __init__(self, x, y, color, controls, direction):
        self.num_bullets = 15
        self.inital_cool_time = 20
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
        
        if keys[self.controls["shoot"]]:
            if self.can_shoot():
                return self.shoot()
            
        if keys[self.controls["reload"]] and self.num_bullets < 15:
            self.reload()

        if keys[self.controls["red_bullet"]]:
            if self.can_shoot_red_bullet():
                return self.shoot_red_bullet()
            
        if keys[self.controls["yellow_bullet"]]:
            if self.can_shoot():
                return self.shoot_yellow_bullet()

    def update_cooldown(self):
        if self.shoot_cooldown > 0:
            self.shoot_cooldown = self.shoot_cooldown - 1

    def can_shoot(self):
        if self.shoot_cooldown == 0 and self.num_bullets > 0:
            return True
        else:
            return False

    def shoot(self):
        self.shoot_cooldown = self.inital_cool_time
        self.num_bullets = self.num_bullets - 1

        if self.direction == 1:
            bullet_x = self.x + self.width
        else:
            bullet_x = self.x

        bullet_y = self.y + self.height // 2

        return Bullet(bullet_x, bullet_y, self.direction)
    
    def can_shoot_red_bullet(self):
        if self.shoot_cooldown == 0 and Red_Bullet.get_num_red_bullets_left(self) > 0:
            return True
        else:
            return False
    
    def shoot_red_bullet(self):
        self.shoot_cooldown = self.inital_cool_time

        if self.direction == 1:
            bullet_x = self.x + self.width
        else:
            bullet_x = self.x

        bullet_y = self.y + self.height // 2

        return Red_Bullet(bullet_x, bullet_y, self.direction)
    
    def shoot_yellow_bullet(self):
        self.shoot_cooldown = self.inital_cool_time

        if self.direction == 1:
            bullet_x = self.x + self.width
        else:
            bullet_x = self.x

        bullet_y = self.y + self.height // 2

        return Yellow_Bullet(bullet_x, bullet_y, self.direction)
    def reload(self):
        self.shoot_cooldown = 200
        self.num_bullets = 15

    def take_damage(self, damage):
        self.hp = self.hp - damage

        if self.hp < 0:
            self.hp = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.get_rect())
