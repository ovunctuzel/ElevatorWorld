from Tkinter import *
import random
from Elevator import Elevator
from NPC import NPC
from Building import Building
from ElevatorPanel import ElevatorPanel


def create_panels(elevator):
    for f in range(obj_building.floors):
        obj_panel = ElevatorPanel(elevator)
        obj_panel.x = 100
        obj_panel.y = f * obj_building.floorh + 55
        obj_panel.floor = elevator.floors - f - 1
        obj_building.panels.append(obj_panel)
        entities.append(obj_panel)


def create_elevator(obj_building):
    obj_elevator = Elevator(obj_building.floors)
    obj_elevator.x = 5
    obj_elevator.building = obj_building
    obj_elevator.set_current_floor(START_FLOOR)
    entities.append(obj_elevator)
    return obj_elevator


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


def spawn_NPCs(elevator, spawn_chance):
    if random.random() > 1 - spawn_chance:
        floor, desired = random.sample(range(obj_elevator.floors), 2)
        obj_NPC = NPC(floor, desired)
        obj_NPC.elevator = elevator
        obj_NPC.draw(canv)
        entities.append(obj_NPC)


def loop():
    # Main loop
    step_entities(entities)
    animate_entities(canv, entities)
    spawn_NPCs(obj_elevator, SPAWN_CHANCE)
    canv.after(25, loop)


# PARAMETERS ############################
CANVAS_HEIGHT = 480
CANVAS_WIDTH = 800
NUM_FLOORS = 5
START_FLOOR = 3
SPAWN_CHANCE = 0.005
#########################################

master = Tk()
canv = Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canv.configure(background="#EEEEEE")
canv.pack()

entities = []

obj_building = Building(CANVAS_WIDTH, CANVAS_HEIGHT, NUM_FLOORS)
entities.append(obj_building)

obj_elevator = create_elevator(obj_building)

create_panels(obj_elevator)
obj_building.draw(canv)

# Draw everything
draw_entities(canv, entities)
# Start looping
canv.after(25, loop)
mainloop()
