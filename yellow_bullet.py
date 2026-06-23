from bullet import Bullet

class Yellow_Bullet(Bullet):
    def __init__(self, x, y, direction):
        super().__init__(x, y, direction) # also can be Bullet.__init__(self, x, y, direction)
        self.color = (255, 255, 0)
        self.speed = 25
        self.damage = 5