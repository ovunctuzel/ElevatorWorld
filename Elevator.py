from Entity import Entity
import random

class Elevator(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.floors = 5
        self.current_floor = 1
        self.speed = 1
        self.capacity = 4
        self.building = None
        self.handle = None
        self.panel = None

        self.requests = [0 for i in range(self.floors)]
        # self.requests = [0,0,0,0,0]
        self.state = "Idle"

        self.timer = 0

    def draw(self, canv):
        # Draw elevator
        self.handle = canv.create_rectangle(self.x, self.y-7, self.x+65, self.y-self.building.floorh, fill="#FFFFFF", width=0)

    def animate(self, canv):
        x1, y1, x2, y2 = canv.coords(self.handle)
        canv.move(self.handle, 0, self.y-7 - y2)

    def get_current_floor(self):
        for f in range(1, self.floors+1):
            if self.y == f*self.building.floorh:
                # print "I'm on floor: ", self.floors-f
                return self.floors-f
        return None

    def set_current_floor(self, f):
        self.current_floor = f
        self.y = f*self.building.floorh

    def should_stop(self):
        # print self.current_floor, self.requests, self.state
        # print self.current_floor
        request = self.requests[self.current_floor]
        return request == 2 or (request == 1 and self.state == "GoUp") or (request == -1 and self.state == "GoDown")

    def wait_for_steps(self, time):
        self.timer = time

    def decide(self):
        if any(self.requests[:self.current_floor]) and not (self.state == "GoUp" and any(self.requests[self.current_floor + 1:])):
            self.state = "GoDown"
        elif any(self.requests[self.current_floor + 1:]) and not (self.state == "GoDown" and any(self.requests[:self.current_floor])):
            self.state = "GoUp"
        else:
            self.state = "Idle"

    def step(self):
        # This function gets called each step
        if self.timer > 0:
            self.timer -= 1
            return

        if self.state == "Idle":
            self.decide()

        if self.state == "GoUp":
            self.move(0, -self.speed)
        elif self.state == "GoDown":
            self.move(0, self.speed)

        self.current_floor = self.get_current_floor()
        if self.current_floor is not None and self.should_stop():
            # Clear request
            self.requests[self.current_floor] = 0
            print self.requests
            self.wait_for_steps(100)
            self.decide()








