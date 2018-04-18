from Entity import Entity


class NPC(Entity):
    def __init__(self, floor, desired):
        Entity.__init__(self)
        self.speed = 5
        self.handle = None
        self.desiredF = desired
        self.onF = floor
        self.elevator = None
        self.state = ""
        self.alive = True

    def draw(self, canv):
        w = 8
        h = 24
        self.x = 400
        self.y = (self.elevator.floors-self.onF)*self.elevator.building.floorh
        self.handle = canv.create_rectangle(self.x-w/2, self.y+h/2, self.x+w/2, self.y-h/2, fill="#2277DD", width=0)

    def animate(self, canv):
        x1, y1, x2, y2 = canv.coords(self.handle)
        canv.move(self.handle, self.x - x2, self.y - 5 - y2)

    def decide(self):
        if self.state != "onElevator" and self.onF != self.desiredF:
            self.state = "notDesiredF"
        if self.desiredF == self.onF:
            self.state = "onDesiredF"
        if self.state == "notDesiredF":
            if self.x < self.elevator.x+50:
                self.state = "onElevator"
                # Press button on elevator
                self.elevator.requests[self.desiredF] = 2

    def step(self):
        self.decide()
        # print self.state, self.desiredF, self.onF
        if self.state == "onDesiredF":
            self.x += self.speed
            if self.x > self.elevator.building.width:
                self.alive = False
        elif self.state == "onElevator":
            # Force the elevator to stop at desired floor

            # Attach to elevator
            self.y = self.elevator.y
            self.x = self.elevator.x+50
            self.onF = self.elevator.current_floor
        elif self.state == "notDesiredF":
            # Move towards elevator and press button
            if self.elevator.current_floor == self.onF or self.x > 150:
                self.x -= self.speed
            if self.elevator.current_floor != self.onF and self.x <= 150:
                if self.onF > self.desiredF:
                    # I wanna go down
                    self.elevator.requests[self.onF] = -1
                    print self.elevator.requests
                elif self.onF < self.desiredF:
                    # I wanna go up
                    self.elevator.requests[self.onF] = 1
                    print self.elevator.requests
