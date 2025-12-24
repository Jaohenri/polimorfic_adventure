"""
Base entity implementation
"""
class Entity:
    """
    Represents a Entity in the game
    """
    def __init__(self, name: str, life_points: int, strength: float) -> None:
        """
        Initializes a entity instance.

        Args:
            name: Name of the entity
            life_points: Quantity of life points of the entity
            strength: Quantity of strength points of the entity
        """
        self.name = name
        self.life_points = life_points
        self.strength = strength
        self.defending = False

    def attack(self) -> float:
        """"""
        damage = self.strength
        print(f'\n{self.name} is attacking, causing {damage} of damage ')
        return damage

    def defense(self) -> str:
        self.defending = True
        print (f'\n{self.name} is defending and will cut the next damage taken in half.')
    
    def receive_damage(self, damage: float) -> None:
        if self.defending:
            damage //= 2
            print (f'{self.name} has reduced damage taken by half. Damage suffered is {damage}.')
            self.life_points -= damage
            self.defending = False
        else:
            print(f'{self.name} has taken {damage} damage.')
            self.life_points -= damage

            if self.life_points <= 0:
                print(f'{self.name} was defeated.')
        if self.life_points > 0:
            print(f'{self.name} now has {self.life_points} life points.')

