import random
class Player():
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage
    def attack(self, target):
        target.hp -= self.damage

class Monster():
    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage
    def attack(self, target):
        target.hp -= self.damage

skalny_troll = Monster(80, random.randrange(1,6) * 6)
arek_bandyta = Player(20, random.randrange(1,6) * 2 + 2)

while arek_bandyta.hp > 0 and skalny_troll.hp > 0:
    arek_bandyta.attack(skalny_troll)
    arek_bandyta.attack(skalny_troll)
    skalny_troll.attack(arek_bandyta)

if(arek_bandyta.hp > 0):
    print("Wygrał Arek")
else:
    print('Wygrał troll')