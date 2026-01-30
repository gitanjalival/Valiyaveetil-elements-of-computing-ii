# main.py
# Main game simulation file

# Import all character classes from the characters folder
from characters.character import Character
from characters.warrior import Warrior
from characters.mage import Mage
from characters.healer import Healer
from characters.rogue import Rogue
from characters.archer import Archer


def battle_round(character, target):
    """
    Simulates a single round of battle between two characters.

    Args:
        character (Character): The character performing the action.
        target (Character): The target of the action.
    """
    # Display the character's information
    print("\nBefore round info:")
    print(character.display_info())
    print(target.display_info())

    print("\nAction taken:")
    # Check the character's type and perform the corresponding action
    if isinstance(character, Rogue):  # If the character is a Rogue
        print(character.sneak_attack(target))  # Perform a sneak attack
    elif isinstance(character, Mage):  # If the character is a Mage
        print(character.cast_spell(50))  # Cast a spell (using 50 mana)
    elif isinstance(character, Healer):  # If the character is a Healer
        print(character.heal(target))  # Heal the target
    elif isinstance(character, Archer): #If the characer is an Archer
        print(character.fire_arrow(target))
    elif isinstance(character, Warrior):  # If the character is a Warrior
        print(f"{character.name} displays their strength: {character.strength}")  # Display the warrior's strength

    print("\nAfter round info:")
    print(character.display_info())
    print(target.display_info())


# Main game execution
if __name__ == "__main__":
    print("=" * 50)
    print("Welcome to the RPG Battle Simulator!")
    print("=" * 50)

    # Create characters
    print("\nCreating characters...")
    steve = Character("Steve", 1, 100)
    jane = Warrior("Jane", 5, 500, 1000)
    gandalf = Mage("Gandalf", 10, 1000, 999)
    joe = Healer("Joe", 3, 200, 299)
    paul = Rogue("Paul", 20, 980, 900, 10)
    archie = Archer("Archie", 7, 250, 100, 1)
    print("Characters created!")
    print(f"  - {steve.display_info()}")
    print(f"  - {jane.display_info()}")
    print(f"  - {gandalf.display_info()}")
    print(f"  - {joe.display_info()}")
    print(f"  - {paul.display_info()}")
    print(f"  - {archie.display_info()}")

    # Simulate some battle rounds
    print("\n" + "=" * 50)
    print("Starting Battle Simulation!")
    print("=" * 50)

    # Round 1: Healer heals Steve
    print("\n--- ROUND 1 ---")
    battle_round(joe, steve)

    # Round 2: Rogue attacks Steve
    print("\n--- ROUND 2 ---")
    battle_round(paul, steve)

    # Round 3: Gandalf casts a spell
    print("\n--- ROUND 3 ---")
    battle_round(gandalf, steve)

    # Round 4: Archie attacks Steve
    print("\n--- ROUND 4 ---")
    battle_round(archie, steve)

    # Round 5: Archie attacks Steve again (but has no arrows)
    print("\n--- ROUND 5 ---")
    battle_round(archie, steve)


    print("\n" + "=" * 50)
    print("Battle Simulation Complete!")
    print("=" * 50)
