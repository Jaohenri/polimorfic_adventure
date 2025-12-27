"""Main character implementation."""

from entity import Entity

class Character(Entity):
    """Represents a character in the game."""

    def special_ability(self) -> float:
        """Uses a special ability to perform an attack.

        Returns:
            float: Damage caused by the special ability.
        """
        damage = self.strength * 2
        print(f'\n{self.name} has attacked using a special ability causing {damage} damage.\n')
        return damage
    