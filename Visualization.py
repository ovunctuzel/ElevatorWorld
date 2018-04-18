from Tkinter import *
from Elevator import Elevator
from Player import Player
from Building import Building
from ElevatorPanel import ElevatorPanel




def create_panels(elevator):
    for f in range(obj_building.floors):
        obj_panel = ElevatorPanel(elevator)
        obj_panel.x = 100
        obj_panel.y = f*obj_building.floorh+55
        obj_panel.floor = elevator.floors - f - 1
        entities.append(obj_panel)

def draw_entities(canv, entities):
    for entity in entities:
        entity.draw(canv)


def animate_entities(canv, entities):
    for entity in entities:
        if hasattr(entity, 'animate'):
            entity.animate(canv)


def step_entities(entities):
    for entity in entities:
        if hasattr(entity, 'step'):
            entity.step()


def loop():
    step_entities(entities)
    animate_entities(canv, entities)
    canv.after(25, loop)


master = Tk()

canv = Canvas(master, width=800, height=480)
canv.configure(background="#EEEEEE")
canv.pack()

entities = []

obj_building = Building(800, 480)
entities.append(obj_building)

obj_elevator = Elevator()
obj_elevator.x = 5
obj_elevator.y = canv.winfo_reqheight()
obj_elevator.building = obj_building
obj_elevator.set_current_floor(3)
entities.append(obj_elevator)

create_panels(obj_elevator)

# obj_player = Player()
# obj_player.x = 10
# obj_player.y = 80
# entities.append(obj_player)


obj_building.draw(canv)

##########################################
draw_entities(canv, entities)

canv.after(25, loop)
mainloop()
