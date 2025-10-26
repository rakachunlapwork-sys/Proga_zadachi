import random
import time

class Person:
    def __init__(self, name, attack, health):
        self.name = name
        self.attack_power = attack
        self.health = health

class Dragon(Person):
    def __init__(self, name, attack, health, kick_power, fire_power, choice):
        super().__init__(name, attack, health)
        self.kick_power = kick_power
        self.fire_power = fire_power
        self.choice = choice

    def kick(self, damage):
        Knight.health-= damage
        for i in range(5, 0):
            time.sleep(1)
            Knight.attack-=2

    def fireball(self, damage):
        Knight.health-= damage
        for i in range(5, 0):
            time.sleep(1)
            Knight.health-=2
    

class Knight(Person):
    def __init__(self, name, attack, health, choice):
        super().__init__(name, attack, health)
        self.choice = choice

    def hit(self, power, who):
        if who==Dragon.name:
            Dragon.health-=power
        elif who==Gollem.name:
            Gollem.health-=power
    
    def item_hit(self, power, who):
        if who==Dragon.name:
            Dragon.health-=power
        elif who==Gollem.name:
            Gollem.health-=power

class Gollem(Person):
    def __init__(self, name, attack, health, choice):
        super().__init__(name, attack, health)
        self.choice = choice

    def hit(self, power):
        Knight.health-=power
    
    def jump(self, power):
        Knight.health-=power
        for i in range(5, 0):
            time.sleep(1)
            Knight.attack-=1
    

class Woolf(Person):
    def __init__(self, name, attack, health, choice):
        super().__init__(name, attack, health)
        self.choice = choice

    def bite(self, power, who):
        if who==Dragon.name:
            Dragon.health-=power
        elif who==Gollem.name:
            Gollem.health-=power
    
    def auf(self, who):
        if who==Dragon.name:
            for i in range(5, 0):
                time.sleep(1)
                Dragon.attack-=1
        elif who==Gollem.name:
            for i in range(5, 0):
                time.sleep(1)
                Gollem.attack-=2

