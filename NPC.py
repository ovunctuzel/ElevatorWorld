from Entity import Entity


class Player(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.speed = 0.1

    def draw(self, canv):
        w = 8
        h = 24
        canv.create_rectangle(self.x-w/2, self.y+h/2, self.x+w/2, self.y-h/2, fill="black", width=0)