import random
from random import randint

class Ability:
    def __init__(self, name, attack_strenght):
        self.name = name
        self.attack_strenght = attack_strenght

    def attack(self):
        full_attack = self.attack_strenght
        attack = random.randint(0, full_attack)
        return attack

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block(self):
        block = random.randint(0, self.max_block)
        return block
