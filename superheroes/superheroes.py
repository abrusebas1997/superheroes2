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


class Weapon(Ability):
    def attack(self):
        weapon_attack = randint(self.attack_strength//2, self.attack_strength)
        return weapon_attack

class Hero:
    def __init__(self, name, starting_health=100):
        self.abilities = []
        self.armors = []
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.deaths = 0
        self.kills = 0
    def add_kills(self, num_kills):
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        self.deaths += num_deaths

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

    def fight(self, opponent):
        while self.is_alive() == True and opponent.is_alive() == True:
            if len(self.abilities) > 0 or len(opponent.abilities) > 0:
                opponent.take_damage(self.attack())
                self.take_damage(opponent.attack())
                if opponent.is_alive() == False:
                    self.add_kills(1)
                    opponent.add_deaths(1)
                    print(self.name + ' won')
                else:
                    self.add_deaths(1)
                    self.add_kills(1)
                    print(opponent.name + ' won')
            else:
                print("Draw!")
                return False

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
        return 0

    def view_all_heroes(self):
        for hero in self.heroes:
            print('{}'.format(hero.name))
    def add_hero(self, hero):
        self.heroes.append(hero)

    def attack(self, other_Team):
        while len(self.heroes_alive()) > 0 and len(other_team.heroes_alive()) > 0:
            first_team = random.choice(self.heroes_alive())
            second_team = random.choice(other_team.heroes_alive())
            first_team.fight(second_team)
    def heroes_alive(self): #To include opponent and self in heroes list
        heroes_alive = []
        for hero in self.heroes:
            if hero.is_alive():
                heroes_alive.append(hero)
            return heroes_alive



























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

    # hero.take_damage(15000)
    # print(hero.is_alive())

    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 300)
    # ability2 = Ability("Super Eyes", 130)
    # ability3 = Ability("Wizard Wand", 80)
    # ability4 = Ability("Wizard Beard", 20)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)

    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())
