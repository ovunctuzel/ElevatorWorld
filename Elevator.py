from Entity import Entity


class Elevator(Entity):
    def __init__(self, floors=5):
        Entity.__init__(self)
        self.floors = floors
        self.current_floor = 1
        self.speed = 1
        self.max_ct = 4
        self.NPC_ct = 0
        self.stopped = True
        self.building = None
        self.handle = None
        self.panel = None
        self.requests = [0 for i in range(self.floors)]
        self.state = "Idle"

        self.timer = 0

    def draw(self, canv):
        # Draw elevator
        self.handle = canv.create_rectangle(self.x, self.y - 7, self.x + 65, self.y - self.building.floorh,
                                            fill="#FFFFFF", width=0)

    def animate(self, canv):
        x1, y1, x2, y2 = canv.coords(self.handle)
        canv.move(self.handle, 0, self.y - 7 - y2)

    def get_current_floor(self):
        """ Return current floor based on y coordinate. Take caution if 1 is not a multiple of self.speed. """
        for f in range(1, self.floors + 1):
            if self.y == f * self.building.floorh:
                return self.floors - f
        return None

    def set_current_floor(self, f):
        """ Set current floor. Avoid setting current floor directly. """
        self.current_floor = f
        self.y = f * self.building.floorh

    def should_stop(self):
        """ Check if the elevator has to stop on the current floor. """
        request = self.requests[self.current_floor]
        if self.state == "GoUp":
            if any(self.requests[self.current_floor + 1:]):
                return request in [1, 2]
            else:
                return request in [-1, 1, 2]
        if self.state == "GoDown":
            if any(self.requests[:self.current_floor]):
                return request in [-1, 2]
            else:
                return request in [-1, 1, 2]
        else:
            return [2]

    def wait_for_steps(self, time):
        """ Take no action for 'time' time steps. """
        self.timer = time

    def decide(self):
        """ Transition from one state to another. """
        if any(self.requests[:self.current_floor]) and not (
                        self.state == "GoUp" and any(self.requests[self.current_floor + 1:])):
            self.state = "GoDown"
        elif any(self.requests[self.current_floor + 1:]) and not (
                        self.state == "GoDown" and any(self.requests[:self.current_floor])):
            self.state = "GoUp"
        else:
            self.state = "Idle"

    def step(self):
        """ Elevator logic. Gets called every time step. """

        # Return if wait_for_steps not completed
        if self.timer > 0:
            self.timer -= 1
            self.stopped = True
            return
        self.stopped = False

        if self.state == "Idle":
            self.decide()

        # State to movement commands
        if self.state == "GoUp":
            self.move(0, -self.speed)
        elif self.state == "GoDown":
            self.move(0, self.speed)

        # Check if the elevator needs to stop
        self.current_floor = self.get_current_floor()
        if self.current_floor is not None and self.should_stop():
            # Clear request
            self.requests[self.current_floor] = 0
            self.wait_for_steps(100)
            self.decide()
