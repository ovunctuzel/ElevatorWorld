from Tkinter import *
import random
from Elevator import Elevator
from NPC import NPC
from Building import Building
from ElevatorPanel import ElevatorPanel
from ElevatorButtons import ElevatorButton


def create_panels(elevator):
    """ Create elevator panels for each floor. Each panel has a display and two buttons. """
    for f in range(obj_building.floors):
        obj_panel = ElevatorPanel(elevator)
        obj_panel.x = 100
        obj_panel.y = f * obj_building.floorh + 55
        obj_panel.floor = elevator.floors - f - 1
        obj_building.panels.append(obj_panel)
        entities.append(obj_panel)


def create_elevator(obj_building):
    """ Create and return the elevator object. """
    obj_elevator = Elevator(obj_building.floors)
    obj_elevator.x = 5
    obj_elevator.building = obj_building
    obj_elevator.set_current_floor(START_FLOOR)
    entities.append(obj_elevator)
    return obj_elevator


def create_buttons(elevator):
    """ Create elevator buttons for manual operation. """
    for f in range(obj_building.floors):
        obj_button = ElevatorButton(elevator)
        obj_button.floor = elevator.floors - f - 1
        obj_button.x = obj_building.width - obj_building.floors * 30 + obj_button.floor * 30
        obj_button.y = 25
        entities.append(obj_button)


def draw_entities(canv, entities):
    """ Draw every entity. Call once for each drawable object. """
    for entity in entities:
        entity.draw(canv)


def animate_entities(canv, entities):
    """ Animate every entity. """
    for entity in entities:
        if hasattr(entity, 'animate'):
            entity.animate(canv)


def step_entities(entities):
    """ Step every entity. """
    for entity in entities:
        if hasattr(entity, 'step'):
            entity.step()


def spawn_NPCs(elevator, spawn_chance):
    """
    Randomly spawn NPCs on random floors, with random desired floors.
    :param elevator: The elevator object.
    :param spawn_chance: Probability of spawning an NPC at each time step.
    """
    if random.random() > 1 - spawn_chance:
        floor, desired = random.sample(range(obj_elevator.floors), 2)
        obj_NPC = NPC(floor, desired)
        obj_NPC.elevator = elevator
        obj_NPC.draw(canv)
        entities.append(obj_NPC)


def init_canvas():
    """ Initialize Tk canvas. """
    master = Tk()
    canv = Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canv.configure(background="#EEEEEE")
    canv.master.title("Elevator World by Ovunc Tuzel")
    canv.pack()
    return canv


def loop():
    """ Instructions that occur each time step goes here. """
    step_entities(entities)
    animate_entities(canv, entities)
    spawn_NPCs(obj_elevator, SPAWN_CHANCE)
    canv.after(25, loop)


if __name__ == "__main__":
    # PARAMETERS ############################
    CANVAS_HEIGHT = 480
    CANVAS_WIDTH = 800
    NUM_FLOORS = 5
    START_FLOOR = 3
    SPAWN_CHANCE = 0.005
    #########################################

    canv = init_canvas()

    # Initialize entity list
    entities = []
    obj_building = Building(CANVAS_WIDTH, CANVAS_HEIGHT, NUM_FLOORS)
    entities.append(obj_building)

    obj_elevator = create_elevator(obj_building)

    create_panels(obj_elevator)
    create_buttons(obj_elevator)
    obj_building.draw(canv)

    # Draw everything
    draw_entities(canv, entities)

    # Start looping
    canv.after(25, loop)
    mainloop()
