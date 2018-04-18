from Entity import Entity


class ElevatorButton(Entity):
    def __init__(self, elevator):
        Entity.__init__(self)
        self.elevator = elevator
        self.floor = -1
        self.handle = None
        self.pressed = False

    def draw(self, canv):
        r = 11
        self.handle = canv.create_oval(self.x + r, self.y + r, self.x - r, self.y - r, fill='gray', width=0)
        canv.create_text(self.x, self.y, text=str(self.floor), fill='black')

        canv.tag_bind(self.handle, '<ButtonPress-1>', self.onClick)

    def animate(self, canv):
        if self.pressed:
            canv.itemconfig(self.handle, fill='orange')
        else:
            canv.itemconfig(self.handle, fill='gray')

    def step(self):
        if self.elevator.requests[self.floor] == 0:
            self.pressed = False

    def onClick(self, event):
        """ Callback for elevator button pressed by user. """
        if not self.pressed:
            self.pressed = True
            self.elevator.requests[self.floor] = 2
