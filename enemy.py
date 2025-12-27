"""Enemy implementation."""

import random
from entity import Entity

class Enemy(Entity):
    """Represents an enemy in the game."""
    def action(self) -> str:
        """Selects a random action for the enemy based on predefined odds.

        Returns:
            str: Selected action, either "attack" or "defense"
        """
        action = random.choices(
            ["attack", "defense"],
            weights=[70, 30],
            k=1
        )[0]
        return action
    