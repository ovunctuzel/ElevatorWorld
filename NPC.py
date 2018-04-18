from Entity import Entity
import random

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
        self.width = random.randrange(6, 12)
        self.heigth = random.randrange(12, 32)

    def draw(self, canv):
        w = self.width
        h = self.heigth
        col = "#" + str(hex(random.randrange(100,180))[-2:]) + str(hex(random.randrange(100,180))[-2:]) + "DD"
        self.x = 400
        self.y = (self.elevator.floors - self.onF) * self.elevator.building.floorh
        self.handle = canv.create_rectangle(self.x - w / 2, self.y + h / 2, self.x + w / 2, self.y - h / 2,
                                            fill=col, width=0)

    def animate(self, canv):
        x1, y1, x2, y2 = canv.coords(self.handle)
        canv.move(self.handle, self.x - x2, self.y - 5 - y2)

    def decide(self):
        if self.state != "onElevator" and self.onF != self.desiredF:
            self.state = "notDesiredF"
        if self.desiredF == self.onF and self.elevator.stopped:
            if self.state == "onElevator":
                self.elevator.NPC_ct -= 1
            self.state = "onDesiredF"
        if self.state == "notDesiredF":
            if self.x < self.elevator.x + 50:
                self.state = "onElevator"
                self.elevator.NPC_ct += 1
                # Press button on elevator
                self.elevator.requests[self.desiredF] = 2

    def call_elevator(self, dir):
        for panel in self.elevator.building.panels:
            if panel.floor == self.onF:
                if dir == 1:
                    panel.button_up_pressed = True
                elif dir == -1:
                    panel.button_down_pressed = True
        if self.elevator.requests[self.onF] != 0:
            self.elevator.requests[self.onF] = 2
        else:
            self.elevator.requests[self.onF] = dir

    def step(self):
        self.decide()
        # print self.state, self.desiredF, self.onF
        if self.state == "onDesiredF":
            self.x += self.speed
            if self.x > self.elevator.building.width:
                self.alive = False
        elif self.state == "onElevator":
            # Attach to elevator
            self.y = self.elevator.y
            self.x = self.elevator.x + 50
            self.onF = self.elevator.current_floor
        elif self.state == "notDesiredF":
            # Move towards elevator and press button
            if self.elevator.current_floor == self.onF and self.elevator.stopped and self.elevator.max_ct > self.elevator.NPC_ct or self.x > 150:
                self.x -= self.speed
            if self.elevator.current_floor != self.onF and self.x <= 150:
                if self.onF > self.desiredF:
                    # Call elevator DOWN
                    self.call_elevator(-1)
                elif self.onF < self.desiredF:
                    # Call elevator UP
                    self.call_elevator(1)
