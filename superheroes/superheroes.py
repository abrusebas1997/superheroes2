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

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def current_health(self):
        return self.current_health

    def attack(self):
        total_attack = 0
        for ability in self.abilities:
            total_attack += ability.attack()
        return total_attack

    def add_armor(self, armor):
        self.abilities.append(armor)

    def defend(self, damage_amt=0):
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return total_block

    def take_damage(self, damage):
        defense = self.defend()
        self.current_health -= damage - defense
        return self.current_health

    def is_alive(self):
        if self.current_health > 0:
            return True
        else:
            return False
            

























if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    # ability = Ability("Debugging Ability", 20)
    # print(ability.name)
    # print(ability.attack())
    #
    # armor = Armor("Debugging Shield", 10)
    # print(armor.name)
    # print(armor.block())
    #
    # my_hero = Hero("Grace Hopper", 200)
    # print(my_hero.name)
    # print(my_hero.current_health)
    #
    # ability = Ability("Great Debugging", 50)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # print(hero.abilities)

    # ability = Ability("Great Debugging", 50)
    # another_ability = Ability("Smarty Pants", 90)
    # hero = Hero("Grace Hopper", 200)
    # hero.add_ability(ability)
    # hero.add_ability(another_ability)
    # print(hero.attack())

    # hero = Hero("Grace Hopper", 200)
    # shield = Armor("Shield", 50)
    # hero.add_armor(shield)
    # hero.take_damage(50)
    # print(hero.current_health)

    hero = Hero("Grace Hopper", 200)
    hero.take_damage(150)
    print(hero.is_alive())
    hero.take_damage(15000)
    print(hero.is_alive())
