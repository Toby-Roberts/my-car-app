'''
models.py
Defines the data models for the app.
'''


CATEGORIES = { 
    "economy":  {"label": "Economy"     , "value": 15000},
    "sedan":    {"label": "Sedan"       , "value": 30000},
    "suv":      {"label": "SUV"         , "value": 45000},
    "ute":      {"label": "Ute"         , "value": 50000},
    "sports":   {"label": "Sports Car"  , "value": 70000},
    "luxury":   {"label": "Luxury"      , "value": 90000},
    "supercar": {"label": "Supercar"    , "value": 250000},
    "exotic":   {"label": "Exotic"      , "value": 500000},
}


def create_car(name, category_key):
    """Create a car object with a name and category."""
    # Validate category key
    if category_key not in CATEGORIES:
        raise ValueError(f"Invalid category: {category_key}")
    # Get specific details
    category = CATEGORIES[category_key]
    # Create and return the car object
    return {
        "name": name,                   #economy 
        "category": category["label"],      #Economy   
        "value": category["value"],         #15000
    }