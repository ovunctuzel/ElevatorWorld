class Entity(object):
    """ Every object that lives in the elevator world is an Entity. Entities can have draw, step, animate methods. """

    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
