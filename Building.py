from Entity import Entity


class Building(Entity):
    def __init__(self, w, h, floors):
        Entity.__init__(self)
        self.floors = floors
        self.height = h
        self.width = w
        self.floorh = self.height / self.floors
        self.panels = []

    def draw(self, canv):
        # Draw building

        for i in range(self.floors):
            x = self.x
            y = self.y + (i + 1) * self.floorh
            canv.create_rectangle(x, y, x + self.width, y - 5, fill="#555555", width=0)
        # Draw floor numbers
            canv.create_text(100, y-self.floorh*0.75, text="F"+str(self.floors-i-1), font=('Verdana', '12'))
        # Draw elevator shaft
            canv.create_rectangle(x, self.height, x + 75, 0, fill="#555555", width=0)
