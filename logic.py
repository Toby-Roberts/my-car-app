'''
logic.py
All the logic for the app. 
'''

GARAGE_SIZE = 3 # Max num of cars in the garage

def can_claim(garage):
    """Check if the garage has space for more cars."""
    return len(garage) < GARAGE_SIZE

def claim_car(garage, car):
    """Add a car to the garage if there is space."""
    return garage + [car]

def total_value(garage):
    """Calculate the total value of the cars in the garage."""
    value = 0
    for car in garage: 
        value += car["value"]
    return value

def display_garage(garage):
    """Return a list of car names in the garage."""
    slots = garage.copy()
    while len(slots) < GARAGE_SIZE:
        slots.append(None)  # Fill empty slots with None
    return slots

def reset_garage():
    """Reset the garage to an empty state."""
    return []