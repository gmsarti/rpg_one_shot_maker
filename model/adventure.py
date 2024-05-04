from dataclasses import dataclass, field
from random import choice
import json
from pathlib import Path


# from ..setup import MODEL_DATA_PATH
import dices


@dataclass
class Adventure:
    title: str = None
    hook: str = None
    location: str = None
    encounters: list[str] = field(default_factory=list)
    
    def generate_encounter(self):
        ...
        
    
    def central_tension(self):
        ...

    def generate_hook(self):
        # TODO arrumar o path aqui
        with open(Path.cwd() / "model" / "data" / "adventure_hooks.json", "r") as f:
            data = json.load(f)
        self.hook = f"{choice(data['subjects'])} {choice(data['verbs'])}"


    def generate_location(self):
        with open(Path.cwd() / "model" / "data" / 'adventure_locations.json', 'r') as f:
            data = json.load(f)
        adjective_category = choice(list(data['adjectives'].keys()))
        adjective = choice(data['adjectives'][adjective_category])

        place_category = choice(list(data['places'].keys()))
        place = choice(data['places'][place_category])

        object_creature_category = choice(list(data['objects_creatures'].keys()))
        object_creature = choice(data['objects_creatures'][object_creature_category])

        self.location = f"{adjective} {place} of {object_creature}"

    def generate_twist(self):
        # You could add a list of twists like in the previous examples
        self.twist = "A seemingly minor item holds great power"  

if __name__ == "__main__":
    adventure = Adventure(title="The Shadow Orb")  # Set a title
    adventure.generate_hook()
    adventure.generate_location()
    adventure.generate_twist()

    print(adventure) 
