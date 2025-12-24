from entity import Entity
import random

class Enemy(Entity):
    def action(self) -> str:
        action = random.choices(
            ["attack", "defense"],
            weights=[70, 30],
            k=1
        )[0]
        return action