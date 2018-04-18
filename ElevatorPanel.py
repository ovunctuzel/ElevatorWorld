from Entity import Entity


class ElevatorPanel(Entity):
    def __init__(self, elevator):
        Entity.__init__(self)
        self.elevator = elevator
        self.button_up = None
        self.button_down = None
        self.button_up_pressed = False
        self.button_down_pressed = False
        self.display = None
        self.floor = None

    def draw(self, canv):
        w = 16
        h = 16
        g = 4
        if self.floor != self.elevator.floors - 1:
            self.button_up = canv.create_polygon(self.x, self.y - h, self.x - w / 2, self.y, self.x + w / 2, self.y)
            canv.tag_bind(self.button_up, '<ButtonPress-1>', self.onClickUp)
        if self.floor != 0:
            self.button_down = canv.create_polygon(self.x, self.y + h + g, self.x - w / 2, self.y + g, self.x + w / 2,
                                                   self.y + g)
            canv.tag_bind(self.button_down, '<ButtonPress-1>', self.onClickDown)
        canv.create_rectangle(self.x + 20, self.y + h/2, self.x + 40, self.y - h/2, fill='black')
        self.display = canv.create_text(self.x+30, self.y, text='*', fill='orange')

    def animate(self, canv):
        if self.button_down_pressed:
            canv.itemconfig(self.button_down, fill='orange')
        else:
            canv.itemconfig(self.button_down, fill='black')
        if self.button_up_pressed:
            canv.itemconfig(self.button_up, fill='orange')
        else:
            canv.itemconfig(self.button_up, fill='black')
        if self.elevator.current_floor != None:
            canv.itemconfig(self.display, text=str(self.elevator.current_floor))

    def step(self):
        if self.elevator.requests[self.floor] == 0:
            self.button_up_pressed = False
            self.button_down_pressed = False

    def onClickUp(self, event):
        if not self.button_up_pressed:
            print "Clicked on Up F:", self.floor
            self.button_up_pressed = True
            if self.elevator.requests[self.floor] == 2 or self.elevator.requests[self.floor] == -1:
                self.elevator.requests[self.floor] = 2
            else:
                self.elevator.requests[self.floor] = 1
            print self.elevator.requests

    def onClickDown(self, event):
        if not self.button_down_pressed:
            print "Clicked on Down F:", self.floor
            self.button_down_pressed = True
            if self.elevator.requests[self.floor] == 2 or self.elevator.requests[self.floor] == 1:
                self.elevator.requests[self.floor] = 2
            else:
                self.elevator.requests[self.floor] = -1
            print self.elevator.requests
