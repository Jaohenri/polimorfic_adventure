class Entity:

    def __init__(self, name, life_points, strenght):
        self.name = name
        self.life_points = life_points
        self.strenght = strenght
        self.defending = False
    
    def attack(self):
        damage = self.strenght
        print(f'\n{self.name} is attacking, causing {damage} of damage ')
        return damage

    def defense(self):
        self.defending = True
        print (f'\n{self.name} is defending and will cut the next damage taken in half.')
    
    def receive_damage(self, damage):
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

