from .warrior import Warrior

class Archer(Warrior):
    
    def __init__(self, name, level, health, strength,arrows):
        """
        Represents an Archer character, inheriting from Warrior.
        
        Attributes:
        name (str): The archer's name.
        level (int): The archer's level.
        health (int): The archer's current health.
        strength (int): The archer's strength.
        arrows (int): The archer's arrows.
        """
        super().__init__(name, level, health, strength)
        self.arrows = arrows
    
    def fire_arrow(self, target):
        """
        Attack the target with a fire arrow.

        Args:
            target (Character): The character to attack.

        Returns:
            str: A message indicating the attack action.
        """      
        if (self.arrows > 0):
            self.arrows-= 1
            target.health -= self.strength
            return f'The archer {self.name} hit the target {target.name} with {self.strength} damage'
        else:
            return f"The archer {self.name} is out of arrows"