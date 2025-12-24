from entity import Entity

class Character(Entity):
    def special_ability(self) -> float:
        damage = self.strength * 2
        print(f'\n{self.name} has attacked using a special ability causing {damage} damage.\n')
        return damage
    