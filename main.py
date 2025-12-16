from character import Character
from enemy import Enemy
import os

if __name__ == '__main__':
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    warrior = Character('Warrior',100,20)
    while True:
        try:
            difficulty = int(input('Please seletc your difficulty\n\n1 - Easy\n2 - Medium\n3 - Hard\n\nSelect the number of your difficulty: '))
            clear_screen()
            clear_screen()
            if difficulty == 1:
                enemy = Enemy('Enemy',80, 15)
                break
            elif difficulty == 2:
                enemy = Enemy('Enemy',100, 18)
                break
            elif difficulty == 3:
                enemy = Enemy('Enemy',110, 20)
                break
            else:
                print('Invalid difficulty, please select a valid option')
        except ValueError:
            print('Please enter a number (1, 2 or 3).\n')


print('\nWelcome to the turn based game!')
    
while warrior.life_points > 0 or enemy.life_points > 0:


    print("\n--- Player's turn ---\n")
    while True:
        try:
            player_action = int(input('Choose your action:\n\n' \
            '1. Attack\n' \
            '2. Defend\n' \
            '3. Use Special Ability\n\n' \
            'Please input the number of your action:'))
            if player_action == 1:
                damage = warrior.attack()
                enemy.receive_damage(damage)
                break
            elif player_action == 2:
                warrior.defense()
                break
            elif player_action == 3:
                damage = warrior.special_ability()
                enemy.receive_damage(damage)
                break
            else:
                print('Invalid action, please select a valid option')
        except ValueError:
            print('Please enter a number (1, 2 or 3).\n')
    
    if enemy.life_points <= 0:
        break

    print("\n--- Enemy's turn ---")
    enemy_action = enemy.action()
    if enemy_action == "attack":
        damage = enemy.attack()
        warrior.receive_damage(damage)
    elif enemy_action == "defense":
        enemy.defense()

print ("\n--- End of the game ---\n")
if warrior.life_points > 0:
    print(f"Congratulations {warrior.name}. You won!!\n")
elif enemy.life_points > 0:
    print(f"Game over. {enemy.name} won!!\n")