from bullet import Bullet

class Red_Bullet(Bullet):
    __num_red_bullets_left = 10
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction) # also can be Bullet.__init__(self, x, y, direction)
        self.color = (255, 0, 0)
        self.speed = 8
        self.damage = 20
        Red_Bullet.__num_red_bullets_left -= 1
    def get_num_red_bullets_left(self):
        return Red_Bullet.__num_red_bullets_left