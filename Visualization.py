from Tkinter import *
import random
from Elevator import Elevator
from Player import Player
from NPC import NPC
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

def spawn_NPCs(elevator):
    if random.random() > 0.99:
        floor, desired = random.sample(range(obj_elevator.floors), 2)
        obj_NPC = NPC(floor, desired)
        obj_NPC.elevator = elevator
        obj_NPC.draw(canv)
        entities.append(obj_NPC)


def loop():
    step_entities(entities)
    animate_entities(canv, entities)
    spawn_NPCs(obj_elevator)
    canv.after(25, loop)


master = Tk()

canv = Canvas(master, width=800, height=600)
canv.configure(background="#EEEEEE")
canv.pack()

entities = []

obj_building = Building(800, 600, 7)
entities.append(obj_building)

obj_elevator = Elevator(obj_building.floors)
obj_elevator.x = 5
obj_elevator.y = canv.winfo_reqheight()
obj_elevator.building = obj_building
obj_elevator.set_current_floor(4)
entities.append(obj_elevator)

create_panels(obj_elevator)

# obj_NPC = NPC(2, 4)
# obj_NPC.elevator = obj_elevator
# entities.append(obj_NPC)
#
# obj_NPC = NPC(4, 1)
# obj_NPC.elevator = obj_elevator
# entities.append(obj_NPC)
#
# obj_NPC = NPC(3, 2)
# obj_NPC.elevator = obj_elevator
# entities.append(obj_NPC)

# spawn_NPCs()

obj_building.draw(canv)

##########################################
draw_entities(canv, entities)

canv.after(25, loop)
mainloop()
