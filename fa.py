import random

class character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    @staticmethod
    def attack(target):
        damage_dealt = random.randint(10,20)
        target.hp -= damage_dealt

hero = character('hero', 100)
monster = character('monster', 90)

while hero.hp > 0 and monster.hp > 0:
    hero.attack(monster)
    print(f'Hero attacks monster. Monster has {monster.hp} HP left')
    monster.attack(hero)
    print(f'Monster attacks monster. Hero has {hero.hp} HP left')

    if hero.hp <= 0:
        print('Monster won!')

    elif monster.hp <= 0:
        print('Hero won!')